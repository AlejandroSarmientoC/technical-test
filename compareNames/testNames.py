import psycopg2
from difflib import SequenceMatcher

def connect_to_database():
    # Conexion con la base de datos
    try:
        conn = psycopg2.connect(
            dbname="postgres", #cambiar dbname
            user="basc",       #cambiar user
            password="1234",   #camniar password
            host="localhost",
            port="5432"
        )
        return conn

    except psycopg2.Error as e:
        print("Error al conectar a la base de datos", e)
        return None


def get_names_from_database():
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM names")
            names = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return names
        except psycopg2.Error as e:
            print("Error al recuperar nombres de la base de datos:", e)
            return []
    else:
        return []


def calculate_similarity(name1, name2):
    # Calcular similitud utilizando el coeficiente de similitud de secuencia de difflib
    return round(SequenceMatcher(None, name1, name2).ratio(), 4)


def compare_names(given_name, names_list):
    print(f"Comparando el nombre '{given_name}' con la lista de nombres recuperados de la base de datos:")
    for name in names_list:
        similarity = calculate_similarity(given_name, name)
        similarity_percent = round(similarity * 100, 2)
        print(f"{name}: {similarity_percent}%")


# Nombre dado
given_name = "Guillermo Herrera"
#Lista de nombres recuperados de la BD
names_list = get_names_from_database()

# Comparar nombres y mostrar resultados
compare_names(given_name, names_list)
