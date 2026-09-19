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

## Historical outreach deduplication registry — verified from Sent mail

The following routes were already contacted during the September 8–13 campaign. Do not send a new cold message to them. Any new communication must use the existing thread, identify the material change, and be logged as a follow-up:

### September 8

- University of Washington Aeronautics & Astronautics — `aa-chair@uw.edu`; the same message included blind-copy routes `nasa@uw.edu`, `communications@pnwaiaa.org`, `cfmlab@uw.edu`, and `uwal-kwt@uw.edu`.
- University of Surrey — `a.luccafabris@surrey.ac.uk` and `smp-office@surrey.ac.uk`.
- Pacific Northwest Aerospace Alliance — `nmalcom@pnaa.net` and `contact@pnaa.net`.
- Michelli Weighing & Measurement — `info@michelli.com`.
- University of Washington — `littlej7@uw.edu`.
- Morehouse Instrument Company — `info@mhforce.com`.
- MIT — `plozano@mit.edu`.
- NASA — `Alicia.Graham@nasa.gov`.
- University of Florida — `roy@ufl.edu`.

Several of these received a technical-update reply later the same day. That update is part of the existing thread, not a separate recipient.

### September 10

- UC Davis / JPAS route — `nsarigulklijn@ucdavis.edu`.
- Professor Martin Tajmar — `martin.tajmar@tu-dresden.de`.
- Sabine Hossenfelder routing channel — `sabine@mediamobilize.com`.
- Stanford Leinweber Institute for Theoretical Physics — `litpadmin@stanford.edu`.
- Waterloo Rocketry — `contact@waterloorocketry.com`, copied to `ajbmilne@uwaterloo.ca`.

### September 13

- Orbital Metrology — `sid@orbitalmetrology.com`.
- Seattle University Mechanical Engineering — `me@seattleu.edu`.
- University of Washington Mechanical Test Lab — `mechtest@uw.edu`.
- University of Washington — `littlej7@uw.edu` (already contacted September 8; this later message is recorded as a follow-up/second bounded request, not a new recipient).

This registry was reconstructed from Gmail's Sent records on September 19, 2026. It supersedes any shorter recipient list for deduplication purposes. It records transmission, not delivery, reading, technical review, agreement, or endorsement.

## 2026-09-18 — Aerospace Systems decision

- Submission ID: `0bf95d29-b59a-4d58-a56b-9bf645022c9a`.
- Manuscript: *Aurora/Flux: an auditable systems architecture and falsification protocol for an unverified advanced-propulsion concept*.
- The journal rejected the manuscript for publication.
- The decision email included no reviewer comments or technical critique.
- Interpretation: publication outcome only. It neither validates nor experimentally disproves the Flux hypothesis.
- Status: revise the paper package and select a suitable next venue only after the evidence and venue-fit review.

## 2026-09-19 — Direct critical-review outreach

Six bounded messages were transmitted. They requested skeptical review, measurement guidance, or routing and did not request endorsement:

1. Professor Benjamin Jorns — `bjorns@umich.edu`.
2. University of Michigan PEPL — `pepl_webmaster@umich.edu`.
3. Paihau–Robinson Research Institute routing contact — `Jackson.miller@vuw.ac.nz`.
4. NASA/JPL electric-propulsion contact — `Robert.B.Lobbia@jpl.nasa.gov`.
5. University of Canterbury — `info@canterbury.ac.nz`.
6. Wellington UniVentures — attempted at `info@wellingtonunventures.nz`.

Delivery evidence:

- University of Canterbury issued an automated acknowledgment and stated that a response should arrive within two working days. This is receipt confirmation, not scientific review or endorsement.
- Wellington UniVentures did **not** receive the message. Gmail returned an address failure because the domain `wellingtonunventures.nz` could not be found. Do not resend until the official current route is independently verified.
- No substantive reply from the other four recipients is recorded at this update.

## 2026-09-19 — Official routing wave

- AIAA's current public contact page identifies `custserv@aiaa.org` as its customer-service route rather than providing a research contact form.
- A bounded request was sent to that verified address asking to be routed to the appropriate technical committee, publication contact, standards activity, or professional member for precision-thrust measurement and experimental controls.
- Gmail message id: `1a0ba1e2186fd0ee`.
- Interpretation: routing request only; not technical review or endorsement.

The remaining previously saved routes are not represented as submitted. Live verification found that several URLs are stale, redirect to unrelated pages, return 404, or expose no message form. The Aerospace Corporation page blocked this automated browser. Current official routes must be verified individually before transmission.

Remaining queue:

- NASA Glenn Research Center
- NASA Marshall Space Flight Center
- European Space Agency
- The Aerospace Corporation
- University of Washington College of Engineering
- University of Surrey Engineering
- Purdue College of Engineering
- University of Colorado Boulder Aerospace Engineering

Each submission must preserve its exact route, date, subject, and confirmation evidence. A browser attempt or page visit is not a submission.

## Standing disclosure and interpretation boundary

First-contact disclosure is limited to the public repository, public concept sheet, equation sheet, control matrix, uncertainty plan, and low-energy measurement-bench plan. Do not transmit unpublished implementation details, private Aurora material, patent-sensitive drawings, protected schematics, credentials, or security-sensitive files.

Interest, acknowledgment, referral, correspondence, software tests, and paper analysis are not physical propulsion validation. Null results, refusals, delivery failures, and nonresponses remain part of the evidence record.

## Codespace preservation status

- The named Sage Codespace URL resolves, but the controlled browser remained at GitHub's sign-in gate even after the user signed in elsewhere; those sessions did not share authentication.
- Repository work continued through the authenticated GitHub connection.
- The Codespace deletion clock has **not** been claimed as reset until the Codespace itself is successfully opened.
