# Aurora / Flux Drive outreach and submission log

This log records external scientific-review actions and preserves their exact evidence status. It excludes sensitive unrelated case details.

## 2026-09-09 — University of Surrey response

- Surrey stated that academic staff do not review unsolicited theories and recommended established scientific channels.
- The response pointed to formal peer-reviewed journal submission, Sabine Hossenfelder's physicist-review service, and Stanford/Theoretical Minimum resources.
- Interpretation: referral guidance, not scientific endorsement of Aurora or Flux Drive.

## 2026-09-10 — Referral follow-through

- A bounded request was sent to Sabine Hossenfelder's review channel.
- A bounded inquiry was sent to Stanford/Theoretical Minimum.
- Both described the project as an unverified architecture and propulsion-research program seeking feasibility review.
- No reply or scientific validation is recorded here.

## 2026-09-11 — AIRDEC / Zenodo reply

- Replied to Zenodo support ticket `#3326754` in its existing thread.
- Asked whether independent depositors can participate in the wider AIRDEC alpha.
- Offered suitable public, non-confidential Reality Audit records as test cases.
- Explicitly separated AIRDEC metadata/curation from broader assistant-integration permissions.
- Gmail message id: `1a091c77f2f2cee3`.

## 2026-09-11 — Minewing reply

- Replied to Jenny at Minewing in the existing thread.
- Stated that Sage is in architecture, safety, and software-validation work and is not ready for a manufacturing order.
- Requested due-diligence information: low-volume/no-MOQ capability, minimum charges, examples, current ISO certifications and legal entity, NDA/IP terms, tooling ownership/storage, quality documentation, and two customer references.
- Explicitly authorized no quotation, design work, billable work, or component purchase.
- Gmail message id: `1a091c782ed22c37`.

## 2026-09-11 — Formal peer-review path

- Created a pre-submission manuscript focused on the auditable software architecture, measurement protocol, and falsification gates.
- The manuscript does **not** claim demonstrated thrust, reactionless propulsion, flight readiness, a human-rated city ship, or spacetime engineering.
- JOSS was screened out as an immediate submission route because its current review criteria expect feature-complete research software with a substantial public development history; the present repository is too recent for a defensible immediate submission there.
- Venue selection remains constrained to a legitimate journal with relevant scope and no mandatory author charge.
- No journal submission, acceptance, endorsement, or peer-review outcome exists yet.

## 2026-09-11 — Reproducibility gate

- Ran `python tools/run_submission_demo.py` from the repository package.
- Result: exit code `0`; 25 software tests passed; three Aurora schemas checked.
- The command reported `hardware_io=disabled` and `physical_propulsion_proven=false`.
- Interpretation: the software-only submission gate passed. This is not physical propulsion evidence.
- GitHub Actions run `34635679559` (workflow run 125, job `103382845687`) concluded `failure`, but the job exposed zero executed steps and its log download returned `BlobNotFound`.
- A second run, `34635746702` / job `103383066089`, exposed GitHub's exact annotation: `The job was not started because your account is locked due to a billing issue.`
- Classification: account/billing infrastructure failure before meaningful computation. It does not overturn the local software result and provides no physical evidence.
- Created `tools/build_submission_evidence.py` and preserved `artifacts/submission_evidence_2026-09-11.json`.
- Evidence-bundle SHA-256: `643b2067fee83702e6fdb25662860f279fee6ce957cbf3e16a00fa28161bbb5a`.
- Source-manifest SHA-256: `dad9ec401b476097f6e165a80697deaa226a6c12704471fcd0cf3813395097ae`.
- The evidence bundle reports all three checks passed, hardware disabled, no random seeds, and `physical_propulsion_proven=false`.

## Codespace preservation status

- The named Sage Codespace URL resolves, but the controlled browser remained at GitHub's sign-in gate even after the user signed in elsewhere; those sessions did not share authentication.
- Repository work continued through the authenticated GitHub connection.
- The Codespace deletion clock has **not** been claimed as reset until the Codespace itself is successfully opened.
