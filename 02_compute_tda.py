#!/usr/bin/env python3
"""
Ripser Vietoris-Rips Filtration and Landscape Extraction Module
Computes H_0, H_1, and H_2 persistence landscapes from aligned pMHC point clouds.
"""
import numpy as np
from ripser import ripser
import yaml
import time
import argparse

def load_config(config_path="config/default_params.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def compute_point_cloud_tda(point_cloud, max_dim=2, thresh=15.0):
    results = ripser(point_cloud, maxdim=max_dim, thresh=thresh)
    return results['dgms']

def compute_persistence_landscape(diagrams, grid_points=50, max_scale=15.0, num_layers=4):
    landscape_features = []
    for dim_idx, dgm in enumerate(diagrams):
        clean_dgm = dgm[np.isfinite(dgm[:, 1])]
        if len(clean_dgm) == 0:
            landscape_features.append(np.zeros(grid_points * num_layers))
            continue
            
        t_values = np.linspace(0, max_scale, grid_points)
        layer_vectors = []
        for k in range(1, num_layers + 1):
            layer_vals = []
            for t in t_values:
                tent_heights = [max(0, min(t - b, d - t)) for b, d in clean_dgm]
                tent_heights.sort(reverse=True)
                val = tent_heights[k-1] if len(tent_heights) >= k else 0.0
                layer_vals.append(val)
            layer_vectors.extend(layer_vals)
        landscape_features.append(np.array(layer_vectors))
    return np.concatenate(landscape_features)

def main():
    parser = argparse.ArgumentParser(description="TDA Persistence Computation Benchmark")
    parser.add_argument("--benchmark-runtime", action="store_true", help="Run wall-clock runtime benchmark")
    args = parser.parse_args()

    config = load_config()
    print("Initializing Ripser TDA Computation Module...")
    
    np.random.seed(config['pipeline']['random_seed'])
    test_point_cloud = np.random.randn(85, 3) * 5.0
    
    if args.benchmark_runtime:
        start_time = time.time()
        n_runs = 100
        for _ in range(n_runs):
            dgms = compute_point_cloud_tda(
                test_point_cloud, 
                max_dim=config['tda']['max_homology_dim'],
                thresh=config['tda']['filtration_max_scale']
            )
            landscapes = compute_persistence_landscape(
                dgms, 
                grid_points=config['tda']['landscape_grid_points'],
                max_scale=config['tda']['filtration_max_scale'],
                num_layers=config['tda']['num_layers']
            )
        elapsed = (time.time() - start_time) / n_runs
        print(f"Benchmark Complete: Mean Ripser + Landscape Runtime = {elapsed:.4f} seconds/frame")
    else:
        dgms = compute_point_cloud_tda(test_point_cloud)
        landscapes = compute_persistence_landscape(dgms)
        print(f"Successfully computed TDA vector of shape: {landscapes.shape}")

if __name__ == "__main__":
    main()
