import numpy as np
import matplotlib.pyplot as plt
from tmm import coh_tmm
from stack_builder import build_duv_stack

theta = 0
wavelengths = np.linspace(250, 300, 300) * 1e-9

design_wavelength = 266e-9
n_list, d_list = build_duv_stack(design_wavelength, num_pairs=8)
print("n_list:", n_list)
print("d_list:", d_list)

print("Layer thicknesses (nm):")
for d in d_list:
    if d != np.inf:
        print(d * 1e9)

R_spectrum = []


for wl in wavelengths:
    result = coh_tmm('s', n_list, d_list, theta, wl)
    R_spectrum.append(result['R'])

plt.figure()
plt.plot(wavelengths * 1e9, R_spectrum)
plt.title("DUV HR Reflectance Spectrum")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")
plt.grid()
plt.savefig("reflectance_spectrum.png")
plt.show()