**DUV Multilayer Thin-Film Simulation**
Transfer Matrix Modeling of High-Reflectivity Coatings at 266 nm

**Overview**

This project implements a physics-based simulation of dielectric multilayer coatings in the deep ultraviolet (DUV) regime using the transfer matrix method (TMM).
The goal is to analyze reflectance performance, internal electric field distribution, and coating sensitivity to material absorption and thickness variation — key parameters in high-precision optical systems such as semiconductor inspection and laser-based metrology.

Design wavelength: 266 nm
Structure: Quarter-wave HfO₂ / SiO₂ multilayer stack
Method: Coherent transfer matrix formalism

**Physical Background**
Multilayer dielectric mirrors operate through constructive interference between alternating high- and low-index layers. For a quarter-wave stack centered at λ₀:

𝑑 =λ₀/4n

The transfer matrix method enables:
- Accurate reflectance spectrum calculation
- Polarization-dependent modeling
- Electric field distribution inside layers
- Sensitivity and reliability analysis

This approach is widely used in thin-film optical design and laser coating engineering.

**Simulation Outputs**
**- Reflectance Spectrum**

File: reflectance_266nm.png
- X-axis: Wavelength (250–300 nm)
- Y-axis: Reflectance (0–1)

Result:
- High-reflectivity band centered at 266 nm
- Peak reflectance >95% (lossless design)
- Expected spectral roll-off away from center wavelength
- This demonstrates proper quarter-wave interference behavior.

**- Electric Field Distribution**
File: field_distribution.png
- X-axis: Depth into coating (µm)
- Y-axis: Normalized |E|²

Result:
- Standing-wave pattern inside multilayer
- Field localization primarily within low-index layers
- Field decay toward substrate for HR configuration

This is critical for analyzing:
- Laser damage thresholds
- Absorption-induced heating
- Degradation mechanisms in DUV environments

**- Thickness Sensitivity Analysis**
File: thickness_sensitivity.png
- X-axis: Thickness variation (±5 nm)
- Y-axis: Reflectance at 266 nm

Result:
- Maximum reflectance at nominal thickness
- Symmetric degradation for positive/negative deviations
- Tolerance window indicating manufacturing robustness
This models deposition sensitivity and production yield stability.

**- Absorption Sensitivity Analysis**

File: absorption_sensitivity.png
- X-axis: Imaginary refractive index (k)
- Y-axis: Reflectance

Result:
- Monotonic reflectance reduction with increasing absorption
- Demonstrates importance of low-loss DUV materials
- Links coating optical performance to degradation risk

Relevant for:
- DUV laser systems
- Long-term coating reliability
- Semiconductor inspection optics
