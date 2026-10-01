# Evidence failure modes

## Historical code is read as current architecture
A visitor sees an old provider integration and assumes it is still live. Response: keep the timeline and evidence map explicit.

## Sanitization removes the useful part
An extract is scrubbed so aggressively that it proves nothing. Response: preserve control flow and implementation shape while removing secrets and private data.

## Sanitization misses operational data
A phone number, credential, clinic/customer identifier, or environment value survives the extraction. Response: fail publication review.

## Migration context disappears
The repository looks cleaner if later provider changes are omitted. Response: preserve migration notes so the evidence is not misleading.

## Setup notes become accidental instructions
Old setup material is copied as if it were current provider guidance. Response: label it historical and require fresh review for real deployment.

## Evidence overclaims outcome
Implementation evidence is turned into a claim about production success or customer results. Response: keep implementation proof and outcome proof separate.
