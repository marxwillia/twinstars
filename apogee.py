import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def load_boss_spec(path):
    hdulist = fits.open(path)
    tbdata = hdulist[1].data
    hdulist.close()
    return tbdata

def plot_boss_spec(tbdata,title=None):
    flux = tbdata.field('flux')
    loglam = tbdata.field('loglam')
    plt.plot(np.power(10,loglam),flux)
    plt.xlabel('Wavelength '+'$[\AA]$')
    plt.ylabel('Flux $[10^{-17}$ erg/cm$^{2}$/s/$\AA]$')
    plt.title(title)
#    plt.show()
    return plt.gcf()

def load_apogee(path):
    hdulist = fits.open(path)
    spec = hdulist[1].data
    spec_head = hdulist[1].header

    spec_model = hdulist[3].data
    spec_model_head = hdulist[3].header

    hdulist.close()
    return spec, spec_head, spec_model, spec_model_head

def plot_apogee_spec(spec_dat, spec_head, model_dat=None, title=None, bestfit=False):
    num = len(spec_dat)
    start_loglam = spec_head['CRVAL1']
    step_loglam = spec_head['CDELT1']
    wv_log = np.arange(start_loglam, start_loglam+num*step_loglam, step_loglam)
    plt.plot(np.power(10,wv_log), spec_dat, "k")

    if bestfit:
        plt.plot(np.power(10,wv_log), model_dat, "r")

    plt.xlabel('Wavelength '+'$[\AA]$')
    plt.ylabel('Flux $[10^{-17}$ erg/cm$^{2}$/s/$\AA]$')
    plt.title(title)
    return plt.gcf()
