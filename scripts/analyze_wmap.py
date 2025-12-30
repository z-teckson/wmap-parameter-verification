#!/usr/bin/env python3
"""
Analysis script for WMAP 5-year data.
Loads CMB power spectrum and estimates the age of the universe using WMAP best-fit parameters.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Load data
    data = np.loadtxt('../data/wmap_5yr_tt_spectrum.txt', comments='#')
    l = data[:, 0]
    cl = data[:, 1]
    
    # Plot power spectrum
    plt.figure(figsize=(8,6))
    plt.plot(l, l*(l+1)*cl/(2*np.pi), 'o-')
    plt.xlabel('Multipole l')
    plt.ylabel(r'$l(l+1)C_l/(2\pi)$ [$\mu K^2$]')
    plt.title('WMAP 5-year CMB Temperature Power Spectrum')
    plt.grid(True)
    plt.savefig('../output/power_spectrum.png')
    plt.close()
    
    # WMAP 5-year best-fit parameters (flat ΛCDM)
    H0 = 70.4  # km/s/Mpc
    Om = 0.272
    OL = 0.728  # flat universe
    
    # Calculate age of universe (approximation for flat ΛCDM)
    # t0 = (1/H0) * (2/3) * (1/sqrt(OL)) * asinh(sqrt(OL/Om))
    # Convert H0 to s^-1: H0 = 70.4 km/s/Mpc = 70.4 * 1000 m/s / (3.086e22 m) = 2.28e-18 s^-1
    H0_s = H0 * 1000 / 3.086e22  # in s^-1
    age_seconds = (2/(3*H0_s*np.sqrt(OL))) * np.arcsinh(np.sqrt(OL/Om))
    age_Gyr = age_seconds / (365.25*24*3600*1e9)
    
    # Output result
    with open('../output/result.txt', 'w') as f:
        f.write(f'Estimated age of the universe: {age_Gyr:.2f} Gyr\n')
        f.write(f'WMAP 5-year best-fit age: 13.73 ± 0.12 Gyr\n')
        f.write(f'Difference: {age_Gyr - 13.73:.2f} Gyr\n')
    
    print(f'Age calculated: {age_Gyr:.2f} Gyr')

if __name__ == '__main__':
    main()
