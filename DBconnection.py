from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


DB_NAME = "45"
DB_USER = "postgres"
DB_PASSWORD = "5916"
DB_HOST = "localhost"
DB_PORT = "5432"


#HTML kısmını bir html class'a taşıyarak kodunda string olarak getir.
#  config class'a taşı home olsun



@app.route('/', methods=['GET'])
def welcome():
    return """
    <html>
    <head>
    <style>
    .center {
        text-align: center;
    }
    </style>
    </head>
    <body>
    <div class="center">
    <h1>Merhaba, caph.org'a hoş geldiniz.</h1>
    <p> Sınıflar --> /classes </p>
    <p> Okullar --> /school </p> 
    <p> Öğrenciler --> /students </p>
    </div>
    </body>
    </html>
    """
def get_classes():
    connection = None

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
    #
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM classes;")
        records = cursor.fetchall()

        return jsonify(records)

    except (Exception, psycopg2.Error) as error:
        return jsonify({"error": str(error)})

    finally:
        if connection:
            cursor.close()
            connection.close()

            #connection kısmı ayrı bir class olacak, connection da isme göre çağır
            #tek bir connection, altında

def get_school():
    connection = None

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM school;")
        records = cursor.fetchall()

        return jsonify(records)

    except (Exception, psycopg2.Error) as error:
        return jsonify({"error": str(error)})

    finally:
        if connection:
            cursor.close()
            connection.close()

def get_students():
    connection = None

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students;")
        records = cursor.fetchall()

        return jsonify(records)

    except (Exception, psycopg2.Error) as error:
        return jsonify({"error": str(error)})

    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/classes', methods=['GET'])
def classes():
    return get_classes()

@app.route('/school', methods=['GET'])
def school():
    return get_school()

@app.route('/students', methods=['GET'])
def students():
    return get_students()


if __name__ == '__main__':
    app.run(debug=True)
