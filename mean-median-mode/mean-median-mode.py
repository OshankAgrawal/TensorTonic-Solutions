import numpy as np
from collections import Counter
from statistics import mode

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    npArray = np.array(x)
    # Write code here
    mean_x = np.mean(npArray)
    median_x = np.median(npArray)
    mode_x = mode(npArray)

    ans = (mean_x, median_x, mode_x)

    return ans