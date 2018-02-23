# Morphology Classification using Alexnet
Recreating a galaxy morphology classifier using Yale HPRC resources

---

### Log

2/22/18
- Optimized resource usage
- Deleted duplicate images

2/18/18
- Finished initial test train (~7 epochs, 80% accuracy in 12 hours)

2/17/18
- Set up TensorFlow on Grace
- Began training job (all data, 100 epochs)

2/17/18
- Succesful installation of TF and TFLearn using fresh Anaconda installation in home directory

2/13/18
- Uploaded data to group storage on Grace (Globus ID: 5c1d826e-1131-11e8-a7ed-0a448319c2f8)

2/12/18
- Received accounts for YHPC clusters

2/4/18
- Completed initial network code
- Downloaded data locally

---

Spiral galaxies in `/data/0`

Elliptical galaxies in `/data/1`

Uncertain galaxies in `/data/2`

To upload your own data remove the line `data/` from `.gitignore`

---

To get data run `wget -i listOfUrls.txt` for each of the galaxy lists in `/dataHandlers`

Then run `find . -type f -exec mv '{}' '{}'.jpg \;` in each data subfolder to change extensions to .jpg

Image preloader function of tflearn will automatically create learning sets using this file structure

To change dataset, change the SDSS CasJobs query `/dataHandlers/zooMaster.txt` and run `python3 dataReader.py` pathing to the new CSV (indices of where the classifications and image url must be changed for the data reader to work for new data)

---

Galaxy Zoo classifications: Lintott et al. 2008

SDSS DR12 images: Alam, Albareti, and Allende Prieto et al. 2015

CasJobs query specifications: Kuminski and Shamir 2016

Alexnet architecture: Krizhevsky, Sutskever, and Hinton 2012
