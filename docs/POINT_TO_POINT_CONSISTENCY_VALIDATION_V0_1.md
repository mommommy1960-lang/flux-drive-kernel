# Point-to-Point Consistency Module — Validation Record v0.1

## Scope

This module evaluates necessary mathematical conditions for two speculative
relativity branches. It is not a transport simulator or physical drive model.

Implemented:

- Morris-Thorne throat-radius check;
- finite-redshift check;
- flaring-out check;
- radial null-energy combination at the throat;
- Alcubierre smooth top-hat profile;
- requested average-speed reporting check;
- finite/value input validation.

## Local validation

Command:

    python -m unittest -v test_spacetime_consistency.py

Result on September 19, 2026:

- 7 tests run;
- 7 passed;
- 0 failures;
- 0 errors.

## Scientific result preserved

For the standard Morris-Thorne throat expression,

    rho_energy + p_r = c^4 (b'(r0)-1) / (8 pi G r0^2),

the flaring-out condition b'(r0) < 1 produces a negative radial null-energy
combination at the throat. The software records that conflict; it does not
reinterpret it as a propulsion result.

## Non-claims

The module does not derive a complete stress-energy tensor, demonstrate a
physical source, prove stability, create a black hole/wormhole/warp bubble,
or establish point-to-point transport.

## Next gate

Independent review of equations and units, followed by a symbolic full-tensor
implementation for one frozen metric and coordinate convention.
