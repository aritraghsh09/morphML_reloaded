# Morphology Classification using Deep Learning
Recreating a galaxy morphology classifier using Yale HPRC resources

---

### Log

3/5/18
- Grace maintenance complete

2/25/18
- Completed test runs changing learning rate and batch size

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

## Getting Data

1. Run `wget -i listOfUrls.txt` for each of the galaxy lists in `/dataHandlers`
2. On Mac, run `find . -name '.DS_Store' -type f -delete` from the project directory to recursively delete Finder preferences (avoid opening the data directories in Finder)
3. Then run `find . -type f -exec mv '{}' '{}'.jpg \;` in each data subfolder to change extensions to .jpg (image preloader function of tflearn will automatically create learning sets using this file structure)
4. Get the number of images by running `\ls -afq | wc -l` in each subdirectory

---

## Changing Data

### SDSS

1. Change the SDSS CasJobs query `/dataHandlers/zooMaster.sql`
2. Run `python3 dataReader.py` pathing to the new CSV (indices of where the classifications and image url must be changed for the data reader to work for new data)
3. Delete any duplicates by running `find . -type f -name '*.1.jpg' -delete` in each subdirectory

### To another set

1. Compile images in `/data` folder structure with each subdirectory as a different category to classify
2. Reset the `dataPath` variable in the network

### Dataset size

1. Create a backup running `cp -r ./data ./dataBackup` in the `/project` directory
2. Create a folder `/dataTest` with the same subdirectory structure as `/data`
3. Run `for file in $(ls -p | grep -v / | tail -NUMBER_OF_IMAGES_TO_MOVE); do mv $file ../../dataTest/SUBDIRECTORY_NAME; done` from each subdirectory in `/data` to move a number of images to a test folder
4. Ensure the training and test data are loaded correctly with image preloader in the network

---

Galaxy Zoo classifications: Lintott et al. 2008

SDSS DR12 images: Alam, Albareti, and Allende Prieto et al. 2015

CasJobs query specifications: Kuminski and Shamir 2016

Alexnet architecture: Krizhevsky, Sutskever, and Hinton 2012
