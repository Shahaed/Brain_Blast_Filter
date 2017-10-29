import pymysql.cursors

def queryAccel():

    # connecting to thomas han database
    connection = pymysql.connect(host='phly.c7jx0v6pormd.us-east-1.rds.amazonaws.com',
                                 user='phly',
                                 password='phlyisthebest',
                                 db='phly',
                                 port=3306,
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM accel_data"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()

    print(len(result))
    for x in range(100):
        print(result[x])
    return result

if __name__ == '__main__':
    queryAccel()