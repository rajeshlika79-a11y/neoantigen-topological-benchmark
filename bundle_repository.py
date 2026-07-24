#!/usr/bin/env python3
"""
Local Standalone ZIP Packaging Script
Run this locally with python bundle_repository.py to assemble the zip archive.
"""
import os
import zipfile

REPO_NAME = "neoantigen-topological-benchmark"
ZIP_FILENAME = "neoantigen_topological_benchmark.zip"

if __name__ == "__main__":
    print(f"Creating local archive {ZIP_FILENAME}...")
