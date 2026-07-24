# Conformational Topological Descriptors Enhance Neoantigen Immunogenicity Prediction Across HLA Supertypes

Official repository for the multi-dataset computational benchmark and validation study evaluating dynamic structural-topological descriptors ($H_0, H_1, H_2$ persistent homology landscapes) for pMHC immunogenicity prediction.

## 📌 Quick Start

```bash
# 1. Clone Repository
git clone https://github.com/rajesh-lab/neoantigen-topological-benchmark.git
cd neoantigen-topological-benchmark

# 2. Build Conda Environment
conda env create -f environment.yml
conda activate pmhc-tda

# 3. Verify System Dependencies & Run Core Benchmark
python scripts/04_train_eval_benchmark.py
```

## 📂 Repository Structure
- `config/`: Default filtration and XGBoost hyperparameters
- `data/`: Raw records and pre-processed 40% MMseqs2 cluster splits
- `models/`: Trained model weights (.json)
- `scripts/`: Fully runnable modular pipeline (01 through 08)
- `reproducibility_verification_guide.md`: Peer-review verification checklist
