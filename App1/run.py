from flask import Flask, request
import pymysql.cursors
import json

app = Flask(__name__)


@app.route('/')
def hello_world() :  # put application's code here
    return 'Hello World!'

@app.route('/createTable', methods=['GET'])
def createTable():
    connection = pymysql.connect(host='host.docker.internal',
                                 user='root',
                                 password='admin',
                                 database='mysql', port=6603)

    with connection:
        with connection.cursor() as cursor :
            sql_create_table = "CREATE TABLE `matieres` ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(30) NOT NULL, description VARCHAR(30) NOT NULL, nb_heure INT);"
            cursor.execute(sql_create_table)
            connection.commit()
            print("Table created")
    return app.response_class(response="Table Created", status=200)

@app.route('/pushDataToMySQL', methods=['GET'])
def pushDataToMySQL():
    connection = pymysql.connect(host='host.docker.internal',
                                 user='root',
                                 password='admin',
                                 database='mysql', port=6603)

    with connection:
        with connection.cursor() as cursor :
            sql_insert_data = "INSERT INTO matieres (nom,description, nb_heure) VALUES ('Espa', 'cours en anglasis', 4), ('BI et big data', 'cours de big data cool', 7);"

            cursor.execute(sql_insert_data)
            connection.commit()

            print("Finish")
    return app.response_class(response="Data Pushed", status=200)

class Matiere :
    def __init__(self, nom, description, nb_heure):
        self.nom = nom
        self.description = description,
        self.nb_heure = nb_heure

    def to_dict(self):
        return {"nom": self.nom, "description": self.description, "nb_heure":self.nb_heure}

@app.route('/load', methods=['GET'])
def loadMySQL() :
    # Connect to the database


    connection = pymysql.connect(host='host.docker.internal',
                                 user='root',
                                 password='admin',
                                 database='mysql',port=6603)
    with connection :
        with connection.cursor() as cursor :
            # Read a single record
            sql = "SELECT * FROM `matieres` "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            connection.commit()

    response = {
        "matieres":[]
    }
    for res in result:
        matiere = Matiere(res[1], res[2], res[3]).to_dict()
        response["matieres"].append(matiere)

    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__' :
    app.run()
