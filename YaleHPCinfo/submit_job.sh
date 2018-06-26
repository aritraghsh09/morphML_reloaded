#!/bin/bash

#SBATCH --job-name=gal_8e
#SBATCH --output=gal_net_run_8e_n1.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --gres-flags=enforce-binding
#SBATCH --time=18:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=aritra.ghosh@yale.edu

export PATH=$HOME/anaconda2/bin:$PATH
source activate tensorflow
module load GPU/Cuda/8.0
module load GPU/cuDNN/8.0-v6

python gal_net_mt.py
