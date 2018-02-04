# morphML_reloaded
Recreating a galaxy morphology classifier with SDSS using Yale HPRC resources

data is stored in
```
/data
```

spiral galaxies in
```
/data/0
```

elliptical galaxies in
```
/data/1
```

uncertain galaxies in
```
/data/2
```

to get data run `wget -i list_of_urls.txt`
then run `find . -type f -exec mv '{}' '{}'.jpg \;` to change extensions to .jpg