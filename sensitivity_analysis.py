import numpy as np
import matplotlib.pyplot as plt
from tmm import coh_tmm
from stack_builder import build_duv_stack

theta = 0
wavelength = 266e-9

# ------------------------------
# Absorption sensitivity
# ------------------------------
absorption_values = np.linspace(0, 0.01, 50)
R_absorption = []

for k in absorption_values:
    n_list, d_list = build_duv_stack(wavelength, absorption=k)
    result = coh_tmm('s', n_list, d_list, theta, wavelength)
    R_absorption.append(result['R'])

plt.figure()
plt.plot(absorption_values, R_absorption)
plt.title("Reflectance vs Absorption (k)")
plt.xlabel("Imaginary Index k")
plt.ylabel("Reflectance")
plt.grid()
plt.savefig("absorption_sensitivity.png")
plt.show()

# ------------------------------
# Thickness tolerance
# ------------------------------
thickness_error = np.linspace(-5e-9, 5e-9, 50)
R_thickness = []

for delta in thickness_error:
    n_list, d_list = build_duv_stack(wavelength)

    # Modify layer thickness
    d_modified = d_list.copy()
    for i in range(1, len(d_modified)-1):
        if d_modified[i] != np.inf:
            d_modified[i] += delta

    result = coh_tmm('s', n_list, d_modified, theta, wavelength)
    R_thickness.append(result['R'])

plt.figure()
plt.plot(thickness_error * 1e9, R_thickness)
plt.title("Reflectance vs Thickness Error")
plt.xlabel("Thickness Variation (nm)")
plt.ylabel("Reflectance")
plt.grid()
plt.savefig("thickness_sensitivity.png")
plt.show()