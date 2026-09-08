# Black Holes, Wormholes, and the Flux Drive

## Direct answer

No current evidence shows that a Flux Drive—or any controllable human-built
device—can create a stable black hole or use one for point-to-point transport.

A black hole is not a two-way doorway. Its event horizon is a causal boundary:
after crossing it, an ordinary traveler cannot return to the outside universe.
NASA explicitly distinguishes black holes from wormholes and states that black
holes are not portals or shortcuts between locations.

## Scale calculation

For an ideal, non-rotating black hole:

```text
r_s = 2GM/c²
E = Mc²
τ ≈ 5120πG²M³/(ℏc⁴)
```

The repository implements and tests these equations in
`flux_drive_kernel/relativity.py`. Illustrative scales are:

- 1 kg: radius about `1.49 × 10⁻²⁷ m`, rest energy about `8.99 × 10¹⁶ J`,
  idealized lifetime about `8.4 × 10⁻¹⁷ s`;
- 10⁹ kg: radius about `1.49 × 10⁻¹⁸ m`, rest energy about `8.99 × 10²⁵ J`,
  idealized lifetime about `8.4 × 10¹⁰ s`;
- 1 solar mass: radius about `2.95 km`.

These are scale comparisons, not an engineering pathway. They do not include
the additional problems of concentrating energy, preventing catastrophic
accretion, controlling tidal fields, or safely coupling matter to the object.

## Wormholes are a separate hypothesis

General relativity contains mathematical wormhole geometries, but a traversable
wormhole is not the same object as a black hole. In standard Einstein gravity,
traversable wormhole solutions generally require stress-energy that violates
the null energy condition. Stability and physical realization remain open
problems. Some papers study modified-gravity models, but those are theoretical
solutions—not demonstrated devices.

References:

- [NASA: Black Hole Basics](https://science.nasa.gov/universe/black-holes/)
- [Clement and Galtsov: Rotating traversable wormholes in Einstein-Maxwell theory](https://arxiv.org/abs/2210.08913)
- [Kain: Are Einstein-Dirac-Maxwell wormholes traversable?](https://arxiv.org/abs/2305.11217)
- [Lu et al.: Energy conditions in traversable wormholes](https://arxiv.org/abs/2402.17498)

## Project decision

The Flux Drive test program will not label a force trace as a black-hole or
wormhole effect. A future relativity branch may simulate candidate metrics and
test their equations for consistency, but it cannot claim transport capability
without a physically realized, stable, traversable geometry and independent
evidence of two-way information and matter transfer.
