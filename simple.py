import psycopg2

try:
    connection = psycopg2.connect(
        database="botdb",
        user="botuser",
        password="botpassword",
        host="127.0.0.1",
        port="5432"
    )
    print("Connected to PostgreSQL")
except Exception as e:
    print("Error:", e)
