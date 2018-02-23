SELECT TOP 1000000
  Z.objID,
  'http://skyserver.sdss.org/dr12/SkyserverWS/ImgCutout/getjpeg?ra='  + cast(Z.ra AS varchar(15)) + '&dec=' + cast(Z.dec AS varchar(15)) + '&scale=0.2&width=120&height=120' AS img,
  Z.spiral,
  Z.elliptical,
  Z.uncertain,
  PZ.z
from Galaxy AS G
  JOIN ZooSpec AS Z ON Z.objID = G.objID
  JOIN Photoz AS PZ ON PZ.objID = Z.objID

WHERE
  G.type = 3
  and G.petroRad_r > 5.5
  and G.petroRadErr_r < 5
  and (G.flags & (dbo.fPhotoFlags('TOO_LARGE') + dbo.fPhotoFlags('BAD_RADIAL')
    + dbo.fPhotoFlags('NOPETRO_BIG') + dbo.fPhotoFlags('BADSKY')
    + dbo.fPhotoFlags('EDGE') + dbo.fPhotoFlags('PEAKS_TOO_CLOSE')
    + dbo.fPhotoFlags('MANYPETRO') + dbo.fPhotoFlags('TOO_FEW_GOOD_DETECTIONS'))) = 0
