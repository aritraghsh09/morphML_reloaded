# morphML_reloaded
Recreating a galaxy morphology classifier with SDSS using Yale HPRC resources

---

Spiral galaxies in `/data/0`

Elliptical galaxies in `/data/1`

Uncertain galaxies in `/data/2`

To upload your own data, remove the `data/` line from `.gitignore`

---

To get data run `wget -i list_of_urls.txt` for each of the galaxy lists in `/dataHandlers`

Then run `find . -type f -exec mv '{}' '{}'.jpg \;` in each data subfolder to change extensions to .jpg

Image preloader function of tflearn will automatically create learning sets using this file structure

To change dataset, change the SDSS CasJobs query `/dataHandlers/ZooMaster.txt` and run `python3 DataReader.py` pathing to the new CSV

---

Galaxy Zoo classifications: C. Lintott et al. 2008

SDSS DR12 images: S. Alam, F. D. Albareti, C. Allende Prieto et al. 2015

CasJobs Query specifications: E. Kuminski and L. Shamir 2016

Alexnet architecture: A. Krizhevsky, I. Sutskever, G. E. Hinton 2012
