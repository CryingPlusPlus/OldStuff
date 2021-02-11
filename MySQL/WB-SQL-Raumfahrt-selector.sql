SELECT * FROM SALZ_Raumfahrt.mitarbeiter
LEFT JOIN SALZ_Raumfahrt.arbeitet_an
	ON SALZ_Raumfahrt.arbeitet_an.id=SALZ_Raumfahrt.mitarbeiter.id
LEFT JOIN SALZ_Raumfahrt.projekt
	ON SALZ_Raumfahrt.projekt.id = SALZ_Raumfahrt.arbeitet_an.projekt
WHERE bezeichner LIKE"%c%"