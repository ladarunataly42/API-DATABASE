from mysql.connector import connect, Error
import mysql.connector


class Actions:

    def __init__(self):
        self.db = mysql.connector.connect(user='root', password='',
                                          host='localhost',
                                          database='api')

    def upload_database(self, text, filename):
        insert_query = f"INSERT INTO api_file(FILENAME, FILE_TEXT) VALUES ('{text}','{filename}');"
        with self.db.cursor() as cursor:
            cursor.execute(insert_query)
            self.db.commit()
            return True

    def delete_by_id(self, id):
        delete_query = f"Delete FROM api_file WHERE id={id}"
        with self.db.cursor() as cursor:
            cursor.execute(delete_query)
            self.db.commit()
            return True

    def update_from_id(self, id, text):
        update_query=f"UPDATE api_file set FILE_TEXT = '{text}' where id = {id}"

        with self.db.cursor() as cursor:
            cursor.execute(update_query)
            self.db.commit()
            return True
