"""Opt-in contextual reading packets. Read-only; never execution/adoption authority."""
import argparse,hashlib,json,math,re
from pathlib import Path,PurePosixPath

ID='GOV-CTX-001'; VERSION='1.0'
BOOTSTRAP=['00_START_CHAT.md','10_PROMPT_OPERACIONAL_MASTER.md','20_PROJECT_CONTEXT.local.md','30_GOVERNANCE.local.md','40_PROJECT_DECISION_LOG.local.md','50_ARTIFACT_REGISTRY.local.md','60_EVIDENCE_INDEX.local.md','70_WORKSTREAM_REGISTRY.local.md']
class ContextError(ValueError): pass
def unique(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ContextError('DUPLICATE_JSON_KEY')
        result[key]=value
    return result
def contained(root,ref):
    if not isinstance(ref,str) or not ref or ref!=ref.strip() or '\\' in ref or ':' in ref:
        raise ContextError('INVALID_REFERENCE')
    p=PurePosixPath(ref)
    if p.is_absolute() or str(p)!=ref or any(x in {'.','..'} for x in p.parts): raise ContextError('INVALID_REFERENCE')
    target=(root/ref).resolve()
    if not target.is_relative_to(root): raise ContextError('REFERENCE_ESCAPE')
    return target
def load_json(root,ref):
    try:
        return json.loads(contained(root,ref).read_text(encoding='utf-8-sig'),object_pairs_hook=unique,
                          parse_float=finite_float,parse_constant=lambda _:(_ for _ in ()).throw(ContextError('NONFINITE_JSON')))
    except (OSError,UnicodeError,json.JSONDecodeError): raise ContextError('JSON_READ') from None
def finite_float(text):
    value=float(text)
    if not math.isfinite(value): raise ContextError('NONFINITE_JSON')
    return value
def headings(text):
    return [m.group(0) for m in re.finditer(r'^#{1,6} [^\n]+',text,re.M)]
def section(text,heading):
    matches=list(re.finditer(r'^'+re.escape(heading)+r'$',text,re.M))
    if len(matches)!=1: raise ContextError('MISSING_OR_AMBIGUOUS_SECTION')
    level=len(heading)-len(heading.lstrip('#')); start=matches[0].start();end=len(text)
    later=re.search(r'^#{1,'+str(level)+r'} ',text[matches[0].end():],re.M)
    if later: end=matches[0].end()+later.start()
    return text[start:end]
def select(text,selectors):
    if not isinstance(selectors,list) or not selectors or any(not isinstance(x,str) for x in selectors): raise ContextError('INVALID_SELECTORS')
    parts=[]
    for s in selectors:
        if s=='*': parts.append(text)
        elif s=='@headings': parts.append('\n'.join(headings(text))+'\n')
        elif s=='@tables': parts.append('\n'.join(line for line in text.splitlines() if line.startswith('|'))+'\n')
        elif s.startswith('#'): parts.append(section(text,s))
        else: raise ContextError('INVALID_SELECTOR')
    return '\n'.join(parts)
def registry_row(text,wid):
    rows=[]
    for line in text.splitlines():
        cells=[x.strip().strip('`') for x in line.split('|')[1:-1]]
        if cells and cells[0]==wid: rows.append(cells)
    if len(rows)!=1 or len(rows[0])<9: raise ContextError('WORKSTREAM_ROUTE_AMBIGUOUS')
    return rows[0]
def packet(runtime,phase,activity=None,workstream=None,access='READ_ONLY'):
    root=Path(runtime).resolve();manifest=load_json(root,'runtime-manifest.json')
    if manifest.get('bootstrap_files')!=BOOTSTRAP: raise ContextError('BOOTSTRAP_ORDER')
    binding=manifest.get('context_loading')
    if not isinstance(binding,dict) or binding.get('id')!=ID or binding.get('version')!=VERSION: raise ContextError('CONTEXT_NOT_ADOPTED')
    profile=load_json(root,binding.get('profile'))
    if profile.get('contract_id')!=ID or profile.get('version')!=VERSION: raise ContextError('PROFILE_VERSION')
    if not isinstance(binding.get('adoption_decision'),str) or not binding['adoption_decision'].strip(): raise ContextError('ADOPTION_REFERENCE_REQUIRED')
    if access not in {'READ_ONLY','READ_WRITE','UNAVAILABLE'}: raise ContextError('ACCESS_MODE')
    plan=profile.get('bootstrap');modules=profile.get('modules');activities=profile.get('activities')
    if not isinstance(plan,list) or [x.get('path') for x in plan if isinstance(x,dict)]!=BOOTSTRAP: raise ContextError('BOOTSTRAP_PLAN')
    if plan[1].get('selectors')!=['*']: raise ContextError('MASTER_MUST_REMAIN_FULL')
    if not isinstance(modules,dict) or not isinstance(activities,dict): raise ContextError('MODULE_MAP')
    # Every section omitted from an indexed normative source must remain reachable.
    for item in plan:
        if not item.get('normative_index'): continue
        text=contained(root,item['path']).read_text(encoding='utf-8')
        direct=item.get('selectors',[]);covered=[]
        for entries in modules.values():
            if not isinstance(entries,list): raise ContextError('MODULE_ENTRIES')
            covered.extend(s for entry in entries if entry.get('path')==item['path'] for s in entry.get('selectors',[]))
        all_selectors=direct+covered
        if '*' not in all_selectors:
            for h in headings(text):
                if h.startswith('## ') and not any(h in headings(select(text,[s])) for s in all_selectors if s not in {'@headings','@tables'}):
                    raise ContextError('UNROUTED_NORMATIVE_SECTION')
    sources=[];seen=set();raw_bytes={}
    def append(item,role):
        if not isinstance(item,dict): raise ContextError('SOURCE_ENTRY')
        ref=item.get('path');selectors=item.get('selectors');key=(ref,json.dumps(selectors))
        if key in seen: return
        seen.add(key)
        try: raw=contained(root,ref).read_bytes();text=raw.decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
        except (OSError,UnicodeError): raise ContextError('SOURCE_READ') from None
        raw_bytes[ref]=len(raw)
        sources.append({'path':ref,'sha256':hashlib.sha256(raw).hexdigest(),'role':role,
                        'selectors':selectors,'content':select(text,selectors)})
    gates=[];loaded=[]
    if phase=='bootstrap':
        for item in plan: append(item,'bootstrap')
    elif phase=='context':
        if activity not in activities: raise ContextError('UNKNOWN_ACTIVITY')
        required=profile.get('required_for_all',[])+activities[activity]
        if not isinstance(required,list): raise ContextError('ACTIVITY_MODULES')
        if workstream:
            if not re.fullmatch(r'WS-\d{8}-\d{3}-[a-z0-9-]+',workstream): raise ContextError('WORKSTREAM_ID')
            registry_ref=manifest.get('workstream_registry');row=registry_row(contained(root,registry_ref).read_text(encoding='utf-8'),workstream)
            state=load_json(root,row[8]);route=row[7]
            if state.get('workstream_id')!=workstream or state.get('operator_alias')!=row[2] or state.get('status')!=row[6]: raise ContextError('REGISTRY_STATE_MISMATCH')
            state_contract=manifest.get('workstream_contract',{})
            if state_contract:
                current=load_json(root,state_contract['profile']);special=current.get('current_handoffs',{}).get(workstream)
                if special:
                    if special.get('path')!=route: raise ContextError('CONTRACT_ROUTE_MISMATCH')
                    gates.append(special.get('entry_gate'))
            append({'path':row[8],'selectors':['*']},'current-state')
            append({'path':route,'selectors':['*']},'explicit-current-handoff')
            handoff=sources[-1]['content']
            actions=re.findall(r'^(?:\*\*NEXT ACTION:\*\*|NEXT ACTION:) (.+)$',handoff,re.M)
            expected=state.get('next_action') if state.get('next_action') is not None else 'NONE'
            if actions!=[expected]: raise ContextError('STATE_HANDOFF_ACTION_MISMATCH')
            required=required+profile.get('workstream_modules',{}).get(workstream,[])
        for name in dict.fromkeys(required):
            if name not in modules: raise ContextError('UNKNOWN_MODULE')
            loaded.append(name)
            for item in modules[name]: append(item,'context-module:'+name)
    else: raise ContextError('PHASE')
    return {'contract_id':ID,'version':VERSION,'phase':phase,'activity':activity,'access':access,
            'workstream':workstream,'authority':'READING_PACKET_ONLY','execution_authorized':False,
            'adoption_verified':False,'writes':False,'entry_gates':gates,'loaded_modules':loaded,
            'source_file_bytes':sum(raw_bytes.values()),
            'emitted_content_bytes':sum(len(s['content'].encode('utf-8')) for s in sources),'sources':sources}
def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('phase',choices=['bootstrap','context']);p.add_argument('--activity');p.add_argument('--workstream')
    p.add_argument('--access',choices=['READ_ONLY','READ_WRITE','UNAVAILABLE'],default='READ_ONLY');args=p.parse_args()
    try: report=packet(args.runtime,args.phase,args.activity,args.workstream,args.access)
    except (ContextError,OSError,TypeError,KeyError) as exc:
        print(json.dumps({'assessment':'FAIL','code':str(exc) if isinstance(exc,ContextError) else 'INVALID_CONFIGURATION','writes':False,'execution_authorized':False}));raise SystemExit(1)
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
