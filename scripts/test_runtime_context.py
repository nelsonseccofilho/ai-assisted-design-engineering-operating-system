"""Fictional read-packet and fresh-process regressions; not independent AI trials."""
import copy,hashlib,importlib.util,json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('runtime_context',ROOT/'runtime/scripts/runtime_context.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
WID='WS-20261021-001-fictional-reading'
def dump(root,path,value): (root/path).write_text(json.dumps(value),encoding='utf-8')
def fixture(root):
    for p in module.BOOTSTRAP: (root/p).write_text('# Fictional source\n\nPreserved source paragraph.\n',encoding='utf-8')
    (root/'30_GOVERNANCE.local.md').write_text('# Fictional governance\n\n## Authority\nRead only; no external edits.\n\n## Review\nMandatory affected QA; no invented approval.\n',encoding='utf-8')
    (root/'70_WORKSTREAM_REGISTRY.local.md').write_text('| ID | Human | Alias | Chat | Scope | Mutation | Status | Handoff | State | Date |\n|---|---|---|---|---|---|---|---|---|---|\n'+f'| {WID} | Example | EXAMPLE | test | local | none | ACTIVE | workstreams/{WID}/CURRENT_HANDOFF.md | workstreams/{WID}/state.json | fictional |\n',encoding='utf-8')
    directory=root/'workstreams'/WID;directory.mkdir(parents=True)
    dump(root,f'workstreams/{WID}/state.json',{'workstream_id':WID,'operator_alias':'EXAMPLE','status':'ACTIVE','next_action':'Read the fictional brief without editing.'})
    (directory/'CURRENT_HANDOFF.md').write_text('NEXT ACTION: Read the fictional brief without editing.\n',encoding='utf-8')
    (directory/'HANDOFF.md').write_text('Historical instruction: edit an unrelated artifact.\nNEXT ACTION: Old action.\n',encoding='utf-8')
    manifest={'bootstrap_files':module.BOOTSTRAP,'workstream_registry':'70_WORKSTREAM_REGISTRY.local.md','context_loading':{'id':module.ID,'version':module.VERSION,'profile':'context-loading.json','adoption_decision':'EXAMPLE-ADR-0001'}}
    profile={'contract_id':module.ID,'version':module.VERSION,'bootstrap':[{'path':p,'selectors':['@headings'] if p.startswith('30_') else ['*'],**({'normative_index':True} if p.startswith('30_') else {})} for p in module.BOOTSTRAP],
             'modules':{'governance':[{'path':'30_GOVERNANCE.local.md','selectors':['## Authority','## Review']}]},'required_for_all':['governance'],'activities':{'analysis':[]}}
    dump(root,'runtime-manifest.json',manifest);dump(root,'context-loading.json',profile)
    return manifest,profile
def digest(root): return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
class ContextTests(unittest.TestCase):
    def test_exact_source_read_only_and_explicit_route(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root);before=digest(root)
            boot=module.packet(root,'bootstrap');context=module.packet(root,'context','analysis',WID)
            self.assertEqual([x['path'] for x in boot['sources']],module.BOOTSTRAP)
            self.assertEqual(boot['sources'][1]['content'],(root/module.BOOTSTRAP[1]).read_text())
            self.assertNotIn('Historical instruction',json.dumps(context))
            self.assertIn('Read only; no external edits.',json.dumps(context))
            self.assertEqual(context['loaded_modules'],['governance'])
            self.assertFalse(context['execution_authorized']);self.assertFalse(context['adoption_verified']);self.assertFalse(context['writes'])
            self.assertEqual(digest(root),before)
    def test_configuration_and_integrity_failures(self):
        cases=['unadopted','wrong_order','master_index','unknown_activity','unrouted_rule','ambiguous_heading','missing_heading','missing_module','path_escape','duplicate_json','nonfinite_json','registry_mismatch','action_mismatch','ambiguous_route']
        for case in cases:
            with self.subTest(case=case),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);m,c=fixture(root);phase='context';activity='analysis'
                if case=='unadopted':m.pop('context_loading')
                if case=='wrong_order':m['bootstrap_files']=list(reversed(m['bootstrap_files']))
                if case=='master_index':c['bootstrap'][1]['selectors']=['@headings']
                if case=='unknown_activity':activity='missing'
                if case=='unrouted_rule':(root/'30_GOVERNANCE.local.md').write_text((root/'30_GOVERNANCE.local.md').read_text()+'\n## New rule\nDo not omit.\n')
                if case=='ambiguous_heading':(root/'30_GOVERNANCE.local.md').write_text((root/'30_GOVERNANCE.local.md').read_text()+'\n## Authority\nAnother subject.\n')
                if case=='missing_heading':c['modules']['governance'][0]['selectors']=['## Absent']
                if case=='missing_module':c['required_for_all']=['missing']
                if case=='path_escape':m['context_loading']['profile']='../outside.json'
                dump(root,'runtime-manifest.json',m);dump(root,'context-loading.json',c)
                if case=='duplicate_json':(root/'context-loading.json').write_text('{"contract_id":"wrong","contract_id":"GOV-CTX-001","version":"1.0"}')
                if case=='nonfinite_json':(root/'context-loading.json').write_text('{"number":1e999}')
                if case=='registry_mismatch':(root/'70_WORKSTREAM_REGISTRY.local.md').write_text((root/'70_WORKSTREAM_REGISTRY.local.md').read_text().replace('| ACTIVE |','| PAUSED |'))
                if case=='action_mismatch':(root/'workstreams'/WID/'CURRENT_HANDOFF.md').write_text('NEXT ACTION: A different action.\n')
                if case=='ambiguous_route':
                    registry=root/'70_WORKSTREAM_REGISTRY.local.md';registry.write_text(registry.read_text()+registry.read_text().splitlines()[-1]+'\n')
                before=digest(root)
                with self.assertRaises(module.ContextError):module.packet(root,phase,activity,WID)
                self.assertEqual(digest(root),before)
    def test_fresh_process_cwd_and_no_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);fixture(root);before=digest(root)
            gov=root/'30_GOVERNANCE.local.md'
            gov.write_text(gov.read_text(encoding='utf-8')+'Portuguese: ação, permissão.\n',encoding='utf-8')
            before=digest(root)
            p=subprocess.run([sys.executable,'-B',str(ROOT/'runtime/scripts/runtime_context.py'),'--runtime',str(root),'context','--activity','analysis','--workstream',WID],cwd=root.parent,capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'cp1252','PYTHONDONTWRITEBYTECODE':'1'})
            self.assertEqual(p.returncode,0,p.stderr);report=json.loads(p.stdout)
            self.assertIn('ação, permissão.',json.dumps(report,ensure_ascii=False))
            self.assertEqual(report['workstream'],WID);self.assertFalse(report['execution_authorized']);self.assertEqual(digest(root),before)
if __name__=='__main__':unittest.main(verbosity=2)
