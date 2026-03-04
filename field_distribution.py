
import numpy as np
import matplotlib.pyplot as plt
from tmm import coh_tmm, position_resolved
from stack_builder import build_duv_stack

# ===============================
# Parameters
# ===============================
wavelength = 266e-9
theta = 0
pol = 's'

# ===============================
# Build stack
# ===============================
n_list, d_list = build_duv_stack(wavelength)

# Solve TMM
result = coh_tmm(pol, n_list, d_list, theta, wavelength)

# ===============================
# Compute field distribution
# ===============================

z_global = []
E_intensity = []

current_position = 0

# Skip first and last layers (semi-infinite)
for layer_index in range(1, len(d_list)-1):

    thickness = d_list[layer_index]

    # create depth points inside this layer
    z_local = np.linspace(0, thickness, 200)

    for z in z_local:
        data = position_resolved(layer_index, z, result)

        # Electric field magnitude squared
        E2 = abs(data['Ey'])**2

        z_global.append(current_position + z)
        E_intensity.append(E2)

    current_position += thickness

# ===============================
# Plot
# ===============================
plt.figure(figsize=(8,5))
plt.plot(np.array(z_global)*1e9, E_intensity)
plt.title("Electric Field Intensity |E|² at 266 nm")
plt.xlabel("Depth (nm)")
plt.ylabel("|E|²")
plt.grid(True)
plt.tight_layout()
plt.savefig("field_distribution.png", dpi=300)
plt.show()