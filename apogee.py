import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def load_apogee_spec(path):
    hdulist = fits.open(path)
    tbdata = hdulist[1].data
    hdulist.close()
    return tbdata

def plot_spec(tbdata):
    flux = tbdata.field('flux')
    loglam = tbdata.field('loglam')
    plt.plot(np.power(10,loglam),flux)
    plt.xlabel('Wavelength '+'$[\AA]$')
    plt.ylabel('Flux $[10^{-17}$ erg/cm$^{2}$/s/$\AA]$')
    return 
