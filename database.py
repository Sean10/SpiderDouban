import pymysql.cursors

def db_open():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='SpiderDouban',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

def db_insert(connection, title, content):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `data` (`title`, `content`) VALUES (%s, %s)"
            cursor.execute(sql, (title, content))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        #     cursor.execute(sql, ('webmaster@python.org',))
        #     result = cursor.fetchone()
        #     print(result)
    finally:
        connection.close()


if __name__ == '__main__':
    db_open()
