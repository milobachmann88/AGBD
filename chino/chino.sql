--1
SELECT FirstName,LastName FROM employees
--2
SELECT name, Milliseconds FROM albums a JOIN tracks t 
ON a.AlbumId=t.AlbumId WHERE a.Title LIKE "big ones" 
ORDER BY Milliseconds DESC
--3
SELECT Title, UnitPrice FROM albums a JOIN tracks t
ON a.AlbumId=t.AlbumId GROUP BY t.AlbumId 
ORDER BY t.UnitPrice DESC LIMIT 10
--4
SELECT t.name AS cancion,g.name AS genero,a.Title AS album
FROM tracks t JOIN genres g ON g.GenreId=t.GenreId
JOIN albums a ON t.AlbumId=a.AlbumId 
WHERE t.UnitPrice=0.99
--5
SELECT t.name AS cancion, t.Milliseconds AS duracion,
a.Title AS album, ar.name AS artista
FROM tracks t JOIN albums a ON a.AlbumId=t.AlbumId
JOIN artists ar ON ar.ArtistId=a.ArtistId
ORDER BY t.Milliseconds ASC LIMIT 20
--6
SELECT emp.LastName AS apellido_emp, emp.Title AS puesto, 
jef.LastName AS apellido_jef, COUNT (*) AS cant_clientes 
FROM employees emp JOIN employees jef ON emp.ReportsTo=jef.EmployeeId
JOIN customers c ON c.SupportRepId=emp.EmployeeId
GROUP BY emp.EmployeeId ORDER BY cant_clientes DESC
--7
SELECT emp.FirstName AS nom_empleado, emp.LastName AS ape_empleado,
c.FirstName AS nom_cliente, c.LastName AS ape_cliente 
FROM employees emp JOIN customers c
--8
SELECT c.FirstName AS nombre, c.LastName AS apellido,
c.Address AS direccion, i.InvoiceDate AS factura
FROM customers c JOIN invoices i
--9
SELECT g.name AS genero, SUM(t.GenreId) AS canciones
FROM genres g JOIN tracks t WHERE g.GenreId=t.GenreId
GROUP BY g.name ORDER BY canciones DESC
--10
SELECT c.FirstName AS nombre, ar.name AS artista 
FROM customers c JOIN invoices i
ON c.CustomerId=i.CustomerId
JOIN invoice_items ii ON i.InvoiceId=ii.InvoiceId
JOIN tracks t ON ii.TrackId=t.TrackId
JOIN albums a ON t.AlbumId=a.AlbumId
JOIN artists ar ON a.ArtistId=ar.ArtistId
GROUP BY artista ORDER BY nombre ASC
--11
SELECT c.FirstName AS nombre, c.City AS ciudad,
t.name AS cancion, g.name AS genero 
FROM customers c JOIN invoices i
ON c.CustomerId=i.CustomerId
JOIN invoice_items ii ON i.InvoiceId=ii.InvoiceId
JOIN tracks t ON ii.TrackId=t.TrackId
JOIN genres g ON t.GenreId=g.GenreId
--12
SELECT * FROM employees e JOIN customers c 
ON e.EmployeeId=c.SupportRepId
JOIN invoices i ON c.CustomerId=i.CustomerId
JOIN invoice_items ii ON i.InvoiceId=ii.InvoiceId
JOIN tracks t ON ii.TrackId=t.TrackId
JOIN albums a ON t.AlbumId=a.AlbumId
JOIN artists ar ON a.ArtistId=ar.ArtistId
JOIN playlist_track pt ON t.TrackId=pt.TrackId
JOIN playlists p ON pt.PlaylistId=p.PlaylistId
JOIN media_types mt ON t.MediaTypeId=mt.MediaTypeId
JOIN genres g ON t.GenreId=g.GenreId
