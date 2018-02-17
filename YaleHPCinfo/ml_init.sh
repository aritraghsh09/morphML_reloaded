#!/bin/bash 
echo "Adding Conda to Path...."
export PATH=$HOME/anaconda2/bin:$PATH
echo "Activating Tensorflow......."
source activate tensorflow
echo "Loading Cuda8.0 and cuDNN8.0-v6 ....."
module load GPU/Cuda/8.0
module load GPU/cuDNN/8.0-v6
