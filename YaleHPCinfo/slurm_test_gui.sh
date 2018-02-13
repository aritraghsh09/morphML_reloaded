#!/bin/bash

#SBATCH --job-name=deep_learn
#SBATCH --output=gpu_job.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:k80:2
#SBATCH --partition=gpu
#SBATCH --gres-flags=enforce-binding
#SBATCH --time=10:00

module load CUDA
module load cuDNN
# using your anaconda environment
source activate deep-learn
python my_tensorflow.py
