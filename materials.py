def get_materials(absorption=0):
    """
    Returns refractive indices at 266 nm.
    absorption: imaginary index component (k)
    """

    n_air = 1.0
    n_sio2 = 1.56 + 1j * absorption
    n_hfo2 = 2.05 + 1j * absorption
    n_sub = 1.5

    return n_air, n_sio2, n_hfo2, n_sub

