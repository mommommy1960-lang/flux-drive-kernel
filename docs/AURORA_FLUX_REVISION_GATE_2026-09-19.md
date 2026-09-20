# Aurora/Flux manuscript revision gate after Aerospace Systems decision

**Date:** 2026-09-19  
**Submission:** `0bf95d29-b59a-4d58-a56b-9bf645022c9a`  
**Decision:** rejected by *Aerospace Systems* without reviewer comments in the decision email  
**Status:** revision plan; not a rebuttal and not a new submission

## What the decision establishes

The journal declined the submitted manuscript. Because no technical comments accompanied the decision email, no specific scientific objection can be attributed to the editor or reviewers. The rejection is preserved as publication evidence, not converted into either experimental falsification or vindication.

## Reframing required before another submission

The next manuscript should lead with the contribution that is presently evidenced:

> an auditable software and metrology protocol that prevents simulated, instrument-generated, or incompletely bounded force signals from being promoted into propulsion claims.

Aurora should be reduced to a short downstream systems-engineering use case. The title and abstract should not make an unbuilt city-ship architecture appear to be co-equal experimental evidence.

## Mathematical core to make explicit

Let the synchronized measured primary and reaction forces be (F_p(t)) and (F_r(t)). Define impulses over a preregistered window ([t_0,t_1]):

[
J_p=int_{t_0}^{t_1}F_p(t),dt,qquad
J_r=int_{t_0}^{t_1}F_r(t),dt.
]

The momentum-closure residual is

[
R_J=J_p+J_r-J_{mathrm{known,external}},
]

where (J_{mathrm{known,external}}) contains independently measured or modeled external exchanges across the declared boundary. If a necessary external channel is missing, the result is **not assessed**, not anomalous.

For discrete synchronized samples with interval (Delta t),

[
hat J_p=Delta tsum_{k=1}^{n}F_{p,k},qquad
hat J_r=Delta tsum_{k=1}^{n}F_{r,k}.
]

The residual variance must retain covariance terms:

[
u^2(R_J)=u^2(J_p)+u^2(J_r)+u^2(J_{mathrm{known,external}})
+2,mathrm{Cov}(J_p,J_r)-2,mathrm{Cov}(J_p,J_{mathrm{known,external}})
-2,mathrm{Cov}(J_r,J_{mathrm{known,external}}).
]

A provisional residual gate may use

[
|R_J|>k,u_c(R_J),
]

with (k) and every exclusion/filter/window rule frozen before unblinding. Crossing this gate is only a trigger for artifact attacks and replication.

## Nuisance-variable model

The measured force channel is modeled as

[
F_{mathrm{meas}}(t)=F_{mathrm{candidate}}(t)+
oldsymbol{eta}^{T}mathbf{x}(t)+d(t)+epsilon(t),
]

where (mathbf{x}(t)) contains temperature, temperature gradients, vibration, acoustic pressure, magnetic field, current, cable displacement/tension, pressure, humidity, and orientation terms; (d(t)) represents drift; and (epsilon(t)) is remaining noise.

The model must be estimated on calibration/control data or by a preregistered procedure. A model fitted after observing the candidate residual cannot be used as if it were independent confirmation.

## Symmetry and control predictions

For an orientation variable (sin{-1,+1}), a directional candidate predicts a frozen sign transformation such as

[
E[J_pmid s=+1]=-E[J_pmid s=-1].
]

The exact transformation depends on the declared mechanism. Thermal, cable, magnetic, acoustic, buoyancy, and fixture effects may transform differently; the protocol must state those alternatives before testing.

The run families are:

- `NULL`: no energized candidate mechanism;
- `SHAM`: electrical/thermal loading without the proposed coupling geometry;
- `KNOWN+`: injected/calibration force of known sign and magnitude;
- `KNOWN-`: reversed injected/calibration force;
- `ACTIVE+` and `ACTIVE-`: blinded candidate orientations;
- `ARTIFACT`: deliberate cable, thermal, vibration, acoustic, or magnetic perturbation used to map false signatures.

CAL-00 must pass before any ACTIVE condition. An unexplained ACTIVE residual cannot advance if the apparatus fails to identify KNOWN conditions or rejects NULL/SHAM incorrectly.

## Energy accounting

Electrical input energy is

[
E_{mathrm{in}}=int_{t_0}^{t_1}V(t)I(t),dt.
]

Thermal storage and exported energy are included to the extent measurable. Energy bookkeeping cannot prove momentum closure, and momentum closure cannot replace energy bookkeeping. Both are necessary.

## Statistical decision structure

The next revision should report:

1. a preregistered primary endpoint;
2. a single primary analysis window;
3. an expanded uncertainty or interval rule;
4. repeated NULL and SHAM false-positive performance;
5. KNOWN-force recovery bias and coverage;
6. orientation-transform consistency;
7. sensitivity to time alignment and integration boundaries;
8. correction for any family of multiple tests;
9. raw and minimally processed data;
10. an independent replication requirement.

Internal repeated software runs validate implementation consistency. They are not independent experiments.

## Evidence needed for the next journal attempt

The strongest next manuscript would include at least one of:

- a real open calibration dataset demonstrating traceable force/impulse recovery and honest uncertainty coverage;
- hardware-in-the-loop replay using blinded NULL/SHAM/KNOWN labels;
- independent execution of the public software and protocol by a metrology or propulsion laboratory;
- a methods-focused comparison showing how the fail-closed architecture prevents false promotion under injected thermal, vibration, magnetic, acoustic, timing, and cable artifacts.

Without one of these, the work is better presented as a protocol/software methods preprint or technical report than as evidence of an advanced-propulsion effect.

## Stop conditions

Do not resubmit as a propulsion-result paper if there is no physical measurement dataset. Do not add more speculative mechanism detail merely to make the paper sound stronger. Do not treat lack of reviewer comments as evidence of suppression or correctness. Do not claim that mathematical self-consistency demonstrates physical thrust.

## Immediate revision deliverables

1. Retitle around auditability and false-positive control.
2. Move Aurora to a bounded application section.
3. Add the explicit residual, covariance, nuisance, symmetry, and energy equations above.
4. Add a calibration/control benchmark with frozen labels and decision rules.
5. Produce a venue-fit matrix only after the revised contribution is clear.
6. Send the revised public package for independent criticism before another journal submission.
