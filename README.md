# Rectangular PLAS

An extension of PLAS with support for rectangular-based sorting.

## Overview

This project extends the original PLAS (Parallel Linear Assignment Sorting) algorithm to support rectangular grid structures. Unlike the original square-based approach, this implementation enables sorting into rectangular arrangements while maintaining the efficiency of parallel linear assignment.

## Background

Based on the original PLAS paper and implementation:
- Paper: [PLAS: Latent Action Space for Offline Reinforcement Learning](https://arxiv.org/abs/2312.13299)
- Original Implementation: [fraunhoferhhi/PLAS](https://github.com/fraunhoferhhi/PLAS)

## Features

- Parallel linear assignment sorting for high-dimensional data
- Efficient sorting into arbitrary rectangular dimensions
- Based on proven PLAS algorithm architecture

## Installation

```bash
pip install -e .
```

## Requirements
- Python 3.x
- PyTorch
- NumPy
- Kornia
- Additional dependencies listed in setup.py

## License

Please refer to the original [PLAS repository](https://github.com/fraunhoferhhi/PLAS) for licensing information.
