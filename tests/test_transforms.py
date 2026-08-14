import numpy as np

from nirs_preprocess import snv


def test_snv_mean_zero():
    out = snv(np.array([1.0, 2.0, 3.0, 4.0]))
    assert abs(out.mean()) < 1e-9
