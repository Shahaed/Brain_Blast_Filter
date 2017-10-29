from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
import shortQuery

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'phly'
app.config['MYSQL_DATABASE_PASSWORD'] = 'phlyisthebest'
app.config['MYSQL_DATABASE_DB'] = 'phly'
app.config['MYSQL_DATABASE_HOST'] = 'phly.c7jx0v6pormd.us-east-1.rds.amazonaws.com'
mysql.init_app(app)


def timeZ():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT `time_stamp` FROM accel_data")
    return float(cursor.fetchone()[0])


@app.route('/OneSecAvr', methods=['POST'])
def oneSecData():
    return str(shortQuery.meanData(1736302585,1000))


@app.route('/')
def returnData():
    zero = timeZ()
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM accel_data")
    data = cursor.fetchall()
    out = [x for x in data ]
    return jsonify(out)



if __name__ == '__main__':
    app.run()
