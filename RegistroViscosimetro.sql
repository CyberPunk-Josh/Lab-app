CREATE DATABASE LabFluidos

CREATE TABLE RegistroViscosimetro(
	ID INT NOT NULL IDENTITY(1,1),
	RPM3 INT,
	RPM6 INT,
	RPM100 INT,
	RPM200 INT,
	RPM300 INT,
	RPM600 INT,
	DESCRIPCION VARCHAR(250),
	FECHA VARCHAR(20)
)

TRUNCATE TABLE RegistroViscosimetro