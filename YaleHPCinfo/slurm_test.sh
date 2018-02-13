#!/bin/bash
#SBATCH --partition=general
#SBATCH --job-name=my_job
#SBATCH --ntasks=1 --nodes=1
#SBATCH --mem-per-cpu=6000 
#SBATCH --time=12:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=email

./myprog -p 20 arg1 arg2 arg3 ...


