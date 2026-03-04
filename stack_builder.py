import numpy as np
from materials import get_materials

def build_duv_stack(design_wavelength, num_pairs=6, absorption=0):
    n_air, n_sio2, n_hfo2, n_sub = get_materials(absorption)

    # Thickness defined ONLY at design wavelength
    d_sio2 = design_wavelength / (4 * np.real(n_sio2))
    d_hfo2 = design_wavelength / (4 * np.real(n_hfo2))

    n_list = [n_air]
    d_list = [np.inf]

    for _ in range(num_pairs):
        n_list.append(n_hfo2)
        d_list.append(d_hfo2)
        n_list.append(n_sio2)
        d_list.append(d_sio2)

    n_list.append(n_sub)
    d_list.append(np.inf)

    return n_list, d_list