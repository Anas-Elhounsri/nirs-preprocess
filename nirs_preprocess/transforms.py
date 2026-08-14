import numpy as np
from scipy.signal import savgol_filter


def snv(spectrum):
    spectrum = np.asarray(spectrum, dtype=float)
    return (spectrum - spectrum.mean()) / spectrum.std()


def savgol_derivative(spectrum, window=11, order=2, deriv=1):
    return savgol_filter(spectrum, window, order, deriv=deriv)
