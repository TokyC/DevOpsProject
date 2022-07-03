from flask import Flask
import pymysql.cursors
import json

app = Flask(__name__)


@app.route('/')
def hello_world() :  # put application's code here
    return 'Hello World!'

@app.get('/pushDataToMySQL')
def pushDataToMySQL():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='admin',
                                 database='COURS', port=6603)

    with connection:
        with connection.cursor() as cursor :
            sql_create_table = "CREATE TABLE `matieres` ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(30) NOT NULL, description VARCHAR(30) NOT NULL, nb_heure INT);"
            sql_insert_data = "INSERT INTO matieres (nom,description, nb_heure) VALUES ('Anglais', 'cours en anglais', 5), ('BI et big data', 'cours de big data cool', 7);"

            # cursor.execute(sql_create_table)
            cursor.execute(sql_insert_data)
            connection.commit()

            print("Finish")
    return "OK"

class Matiere :
    def __init__(self, nom, description, nb_heure):
        self.nom = nom
        self.description = description,
        self.nb_heure = nb_heure

    def to_dict(self):
        return {"nom": self.nom, "description": self.description, "nb_heure":self.nb_heure}

@app.get('/load')
def loadMySQL() :
    # Connect to the database


    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='admin',
                                 database='COURS',port=6603)
    with connection :
        with connection.cursor() as cursor :
            # Read a single record
            sql = "SELECT * FROM `matieres` "
            cursor.execute(sql)
            result = cursor.fetchone()
            connection.commit()

    result = Matiere(result[1],result[2], result[3])

    return result.to_dict()


if __name__ == '__main__' :
    app.run()
