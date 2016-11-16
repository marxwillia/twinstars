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

    err_dat = hdulist[2].data
    err_head = hdulist[2].header

    spec_model = hdulist[3].data
    spec_model_head = hdulist[3].header



    hdulist.close()
    return spec, spec_head, spec_model, spec_model_head, err_dat, err_head

def plot_apogee_spec(spec_dat, spec_head, err_dat=None, model_dat=None, title=None, bestfit=False, showerr=False, split=[]):
    num = len(spec_dat)
    start_loglam = spec_head['CRVAL1']
    step_loglam = spec_head['CDELT1']
    wv_log = np.arange(start_loglam, start_loglam+num*step_loglam, step_loglam)
    wave_lambda = np.power(10,wv_log)

    split.append(wave_lambda[-1]+1)

    num_split = len(split)
    for i in range(num_split):
        plt.subplot(num_split,1,i+1)
        wave_split = split[i]
        mask = wave_lambda < wave_split
        if i==0:
            mask = wave_lambda < wave_split
        else:
            mask = (wave_lambda < wave_split)&(wave_lambda > split[i-1])

        plt.plot(wave_lambda[mask], spec_dat[mask], "k")
        if bestfit:
            plt.plot(wave_lambda[mask], model_dat[mask], "r")
        if showerr:
            plt.plot(wave_lambda[mask], spec_dat[mask]+err_dat[mask], "k", alpha=.5)
            plt.plot(wave_lambda[mask], spec_dat[mask]-err_dat[mask], "k", alpha=.5)
        plt.ylabel('Flux $[10^{-17}$ erg/cm$^{2}$/s/$\AA]$')

    plt.subplot(num_split,1,num_split)
    plt.xlabel('Wavelength '+'$[\AA]$')
    plt.subplot(num_split,1,1)
    plt.title(title)
    return plt.gcf()
