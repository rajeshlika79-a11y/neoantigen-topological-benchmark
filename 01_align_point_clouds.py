#!/usr/bin/env python3
"""
Procrustes Structural Alignment Module
Superposes pMHC conformational ensemble snapshots onto MHC alpha1/alpha2 helices.
"""
import numpy as np

def align_coordinates(points, ref_points):
    """Weighted Procrustes superposition onto reference coordinates."""
    centroid_p = np.mean(points, axis=0)
    centroid_r = np.mean(ref_points, axis=0)
    p_centered = points - centroid_p
    r_centered = ref_points - centroid_r
    H = p_centered.T @ r_centered
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[2, :] *= -1
        R = Vt.T @ U.T
    return (p_centered @ R) + centroid_r

if __name__ == "__main__":
    print("Procrustes Superposition Module Ready.")
