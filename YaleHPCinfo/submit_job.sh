#!/bin/bash

#SBATCH --job-name=galreg_00
#SBATCH --output=galreg_test.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:p100:1
#SBATCH --partition=gpu
#SBATCH --gres-flags=enforce-binding
#SBATCH --time=24:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=aritra.ghosh@yale.edu

source /home/fas/urry/ag2422/.bashrc
export PATH=$HOME/anaconda3/bin:$PATH
conda init bash
conda activate tf113
module load cuDNN/7.6.0-CUDA-9.2.148.1
module load CUDA/10.0.130

python aritra_test.py
