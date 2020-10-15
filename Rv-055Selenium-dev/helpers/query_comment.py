"""simple db connector"""
import pymysql
import pymysql.cursors
import helpers.settings as settings

def query_db():
    """query db, look for last comment"""
    connection = pymysql.connect(host=settings.HOST,
                                 port=int(settings.PORT),
                                 user=settings.USER,
                                 password=settings.PASSWORD,
                                 db=settings.DB,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select * from appsrc_eventscomments order by id desc limit 1;"
            cursor.execute(sql)
            query_result = cursor.fetchall()
            return query_result
    except Exception as error:
        print(error)
    finally:
        connection.close()
