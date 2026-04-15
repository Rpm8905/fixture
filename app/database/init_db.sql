CREATE DATABASE IF NOT EXISTS mundial_db;
USE mundial_db;

CREATE TABLE IF NOT EXISTS partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(100) NOT NULL,
    equipo_visitante VARCHAR(100) NOT NULL,
    estadio VARCHAR(100),
    ciudad VARCHAR(100),
    fecha DATE NOT NULL,
    fase ENUM('grupos', 'dieciseisavos', 'octavos', 'cuartos', 'semis', 'final') NOT NULL
);

CREATE TABLE IF NOT EXISTS resultados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    partido_id INT NOT NULL UNIQUE,
    goles_local INT NOT NULL,
    goles_visitante INT NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partidos(id)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS predicciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    partido_id INT NOT NULL,
    goles_local INT NOT NULL,
    goles_visitante INT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (partido_id) REFERENCES partidos(id),
    UNIQUE(usuario_id, partido_id)
);

-- Datos de prueba: partidos
INSERT INTO partidos (equipo_local, equipo_visitante, estadio, ciudad, fecha, fase) VALUES
('Argentina', 'Canada', 'MetLife Stadium', 'Nueva York', '2026-06-11', 'grupos'),
('España', 'Brasil', 'Rose Bowl', 'Los Angeles', '2026-06-12', 'grupos'),
('Francia', 'Alemania', 'AT&T Stadium', 'Dallas', '2026-06-13', 'grupos'),
('Uruguay', 'Portugal', 'Levi Stadium', 'San Francisco', '2026-06-14', 'grupos'),
('Argentina', 'Chile', 'Estadio Azteca', 'Ciudad de Mexico', '2026-06-18', 'grupos'),
('Brasil', 'Mexico', 'SoFi Stadium', 'Los Angeles', '2026-06-19', 'grupos'),
('Argentina', 'España', 'MetLife Stadium', 'Nueva York', '2026-07-03', 'cuartos'),
('Francia', 'Brasil', 'Rose Bowl', 'Los Angeles', '2026-07-04', 'cuartos'),
('Argentina', 'Francia', 'MetLife Stadium', 'Nueva York', '2026-07-14', 'final');

-- Datos de prueba: resultados
INSERT INTO resultados (partido_id, goles_local, goles_visitante) VALUES
(1, 3, 0),
(2, 1, 1),
(3, 2, 1);

-- Datos de prueba: usuarios
INSERT INTO usuarios (nombre, email) VALUES
('Juan Perez', 'juan@gmail.com'),
('Maria Lopez', 'maria@gmail.com'),
('Carlos Garcia', 'carlos@gmail.com');

-- Datos de prueba: predicciones
INSERT INTO predicciones (usuario_id, partido_id, goles_local, goles_visitante) VALUES
(1, 1, 3, 0),
(1, 2, 2, 1),
(2, 1, 2, 0),
(2, 3, 1, 1),
(3, 1, 3, 1),
(3, 2, 0, 1);