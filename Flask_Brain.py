from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'phly'
app.config['MYSQL_DATABASE_PASSWORD'] = 'phlyisthebest'
app.config['MYSQL_DATABASE_DB'] = 'phly'
app.config['MYSQL_DATABASE_HOST'] = 'phly.c7jx0v6pormd.us-east-1.rds.amazonaws.com'
mysql.init_app(app)


@app.route('/')
def hello_world():

    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM accel_data")
    data = cursor.fetchall()
    out = [x for x in data ]
    return str(out)



if __name__ == '__main__':
    app.run()
