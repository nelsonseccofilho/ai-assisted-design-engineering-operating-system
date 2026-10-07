# Local transcription setup

This guide documents an optional local transcription workflow for meeting evidence.

The operating framework does **not** require WhisperX, OBS Studio or any specific transcription tool. This guide exists so a local recording → transcript workflow can be reproduced when a project chooses to use it.

## Reference workflow

```text
meeting
→ local recording
→ audio/video file
→ WhisperX
→ JSON transcript
→ review
→ Evidence ID
→ requirement / decision mapping
```

## Tools

Typical stack:

- recording: OBS Studio or another approved local recorder;
- transcription/alignment/diarization: WhisperX;
- shell: PowerShell, Bash or equivalent;
- optional GPU acceleration: NVIDIA CUDA-compatible environment;
- optional diarization: Hugging Face read token and accepted pyannote model terms.

Upstream references:
- WhisperX: https://github.com/m-bain/whisperX
- OBS Studio: https://obsproject.com/
- Hugging Face tokens: https://huggingface.co/settings/tokens

## Security first

Never commit:
- Hugging Face tokens;
- passwords;
- API keys;
- OAuth secrets;
- raw client recordings to a public repository.

Prefer environment variables or local secret storage for tokens.

## Install WhisperX

The current WhisperX upstream recommends PyPI for the simplest installation:

```bash
pip install whisperx
```

Verify:

```bash
whisperx --help
```

WhisperX may also require FFmpeg depending on the environment/input media. Install FFmpeg through a trusted platform/package source and verify:

```bash
ffmpeg -version
```

Because WhisperX evolves, always compare this guide with the current upstream README before rebuilding a machine from zero.

## CPU profile

CPU is slower but avoids GPU/CUDA setup.

Generic example:

```powershell
whisperx ".\stakeholder-session.mkv" --model medium --device cpu --compute_type int8 --diarize --output_dir ".\transcriptions" --output_format json --language pt
```

Projects may add a conservative thread count when they want to preserve machine responsiveness, for example:

```powershell
whisperx ".\stakeholder-session.mkv" --model medium --device cpu --compute_type int8 --diarize --output_dir ".\transcriptions" --output_format json --language pt --threads 6
```

## GPU profile

GPU acceleration is optional.

At the time this guide was written, WhisperX upstream documents CUDA 12.8 for its GPU installation path.

A common profile is:

```powershell
whisperx ".\stakeholder-session.mkv" --model medium --device cuda --compute_type float16 --diarize --output_dir ".\transcriptions" --output_format json --language pt
```

Exact CUDA/PyTorch compatibility changes over time. Treat the upstream WhisperX instructions as canonical for a fresh GPU installation.

## Speaker diarization

WhisperX uses pyannote-based diarization.

Current upstream instructions require:
1. a Hugging Face account;
2. a read token;
3. accepting the terms for the diarization model named by the current WhisperX release;
4. supplying the token through a secure mechanism.

Do not hardcode the token in versioned scripts.

Upstream CLI usage may support `--hf_token`; a project may instead persist the token in a local environment/profile if its security policy allows it.

## Output

For evidence workflows, JSON is useful because it is machine-readable and can preserve segments/timestamps/speaker labels.

Recommended output pattern:

```text
meeting-files/
├── stakeholder-session.mkv
└── transcriptions/
    └── stakeholder-session.json
```

The raw recording should stay in approved private/local storage.

A reviewed transcript may be copied into a private Project Runtime only when project policy allows it.

## Validate a new machine

Before relying on a new setup:

1. run `whisperx --help`;
2. transcribe a short non-sensitive sample;
3. confirm JSON output exists;
4. confirm Portuguese language handling when relevant;
5. confirm diarization labels appear when enabled;
6. verify CPU/GPU execution matches the intended profile;
7. confirm the output path is correct;
8. check that no token is written into repository files or shell history scripts.

## Known limitations

WhisperX upstream documents that:
- diarization is not perfect;
- overlapping speech can be difficult;
- alignment depends on language/model support;
- compute settings can trade performance, memory and accuracy.

Therefore:

`machine transcript → review → durable evidence`

not:

`machine transcript → automatic truth`

## Project-specific configuration

Do not add real client names, operator machines, private paths or tokens to this public guide.

Each private Project Runtime should document:
- approved recording tool;
- operator transcription profile;
- CPU/GPU parameters;
- output/storage policy;
- evidence indexing rules;
- any project-specific review requirements.

See [Evidence ingestion](EVIDENCE_INGESTION.md).
