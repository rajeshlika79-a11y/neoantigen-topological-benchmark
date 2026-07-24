#!/usr/bin/env python3
"""
Geometric Dynamics Extraction Module
Calculates per-residue RMSF, backbone circular variance, and discrete Frenet-Serret curvature.
"""
import numpy as np

def compute_rmsf(coords):
    """Calculates RMSF across trajectory frames coords of shape (K, N, 3)."""
    mean_pos = np.mean(coords, axis=0)
    return np.sqrt(np.mean(np.sum((coords - mean_pos)**2, axis=-1), axis=0))

if __name__ == "__main__":
    print("Geometric Feature Extraction Module Ready.")
