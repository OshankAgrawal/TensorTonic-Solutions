import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    
    if len(x) != len(y):
        raise ValueError("Vector must have same length")
        
    dis = 0
    for i in range(len(x)):
        dis += (x[i] - y[i])**2
    return np.sqrt(dis)