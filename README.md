## MANUAL DE USUARIO

Este es un programa Python que compara un nombre dado con una lista de nombres recuperados de una base de datos PostgreSQL y determina el grado de similitud entre ellos. Utiliza un algoritmo SequenceMatcher de similitud de cadenas para realizar la comparación.

### REQUISITOS
- Python 3.12 ([Descargar Python](https://www.python.org/downloads/))
- PostgreSQL ([Descargar PostgreSQL](https://www.postgresql.org/download/))

### USO

1. Ejecutar los siguientes scripts en PostgreSQL para preparar la base de datos:

```sql
-- Creación de tabla
CREATE TABLE names (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Inserción de datos
INSERT INTO names (name) VALUES
    ('Herrera Guillermo'),
    ('Guillen Herrera'),
    ('Hernesto Herrera'),
    ('Guerrero Guillermo'),
    ('Her Gui Jr.'),
    ('Guil Herre Jr.'),
    ('Hernes Herre Jr.'),
    ('Gue Guiller Jr.'),
    ('Gui Herrera'),
    ('Her Guillermo Sr.'),
    ('Herrera Gui III'),
    ('Herr Guille IV'),
    ('Guillermo H. Herrera'),
    ('H. Gui Herrera'),
    ('H. Herrera Guille'),
    ('H. Guille Herrera'),
    ('Guiller H. Herre Jr.'),
    ('H. Guille Herrer'),
    ('H. Herre Gui'),
    ('H. Guille He'),
    ('Guillermo He Sr.'),
    ('H. Herrera'),
    ('Hernesto G. Herrera'),
    ('Guillermo Ernesto He'),
    ('Gu Herrera III'),
    ('Guille He IV'),
    ('Gu He III'),
    ('Guerrero Gu II'),
    ('Guille Guerrero'),
    ('H. Guerrero Guillermo');

2. Clona este repositorio ([Descargar](https://github.com/AlejandroSarmientoC/technical-test.git))

3. Navega al directorio del proyecto ( cd compareNames )

4. Instalacion de librerias ( pip install psycopg2 || pip install psycopg2-binary )

5. Ejecuta el programa ( python testNames.py )
