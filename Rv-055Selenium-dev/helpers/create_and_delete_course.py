import pymysql

class testCourse():

    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='root_password',
                                 db='YouYoda',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    def create_test_course(self):

        """Method for creating course for tests"""
        self.cursor = self.connection.cursor()
        self.sql = "INSERT INTO appsrc_courses (coursename, owner_id, status, description, is_public, start_date, duration, rate, members_limit, categories_id, location, cover_url, cost) VALUES ('Test_subscribe_course', 5, 'Open', 'description1', True, 1569936600, 2, 8, 20, 2, 'Rivne, Ukraine', '/media/library-863148_1920.jpg',0)"
        self.cursor.execute(self.sql)
        self.connection.commit()



    def delete_test_course(self):

        """Method for deleting test course"""
        self.cursor = self.connection.cursor()
        self.sql = "DELETE FROM appsrc_courses WHERE coursename = 'Test_subscribe_course'"
        self.cursor.execute(self.sql)
        self.connection.commit()


    def close_connection(self):

        """Method for closing connection"""
        self.connection.close()

