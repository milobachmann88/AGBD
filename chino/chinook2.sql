INSERT INTO artists (name) VALUES ("Mitski")

INSERT INTO albums (AlbumId, Title, ArtistId)
VALUES (348,"Lush",276)

INSERT INTO tracks (TrackId, name, AlbumId, MediaTypeId, GenreId,
 Composer, Milliseconds, Bytes, UnitPrice)
VALUES (3504,"Real men", 348, 5, 4, "Mitski", 144600,
  5574958, 0.99),
  (3505,"Pearl diver", 348, 5, 4, "Mitski", 144600,
  5574958, 0.99)

UPDATE employees SET Address = "Av. Siempreviva 742", 
City = "Springfield"
WHERE EmployeeId = 3

UPDATE tracks SET UnitPrice = UnitPrice+UnitPrice*0.10
WHERE GenreId = 2

Execution finished with errors.
Result: FOREIGN KEY constraint failed
At line 1:
DELETE FROM artists WHERE name == "Queen"

--Los registros que se deberian borrar son todos los que tengan relacion con
-- el artistid

 
