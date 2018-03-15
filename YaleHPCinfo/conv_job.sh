#!/bin/bash

#SBATCH --job-name=conv1
#SBATCH --output=conv1.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --gres-flags=enforce-binding
#SBATCH --time=5:00:00

export PATH=$HOME/anaconda2/bin:$PATH
source activate tensorflow
module load GPU/Cuda/8.0
module load GPU/cuDNN/8.0-v6

python conv.py
