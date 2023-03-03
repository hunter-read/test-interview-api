import sqlite3
import typing

# Database class for ease of using the database connection with sqlite.
# Best practice is to create DB using- `with Database() as db:`` to avoid risk of leaving connection open
# All queries/save must provide the params as a list to avoid sql injection.
class Database(object):
    def __init__(self):
        self.__db_connection = sqlite3.connect(database="database/gm.db")
        self.__db_cursor = None

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.close()

    def close(self):
        self.__db_connection.close()

    # Use for querying the database. Handles opening a cursor, closing a cursor, and converting it to a list.
    def query(self, query: str, params: typing.List[str]) -> tuple:
        self.__db_cursor = self.__db_connection.cursor()
        data = list(self.__db_cursor.execute(query, params))
        self.__db_cursor.close()
        return data

    # Use for any updates to the database. This handles opening a cursor, commiting the update, and closing a cursor.
    def save(self, query: str, params: typing.List[str]) -> None:
        self.__db_cursor = self.__db_connection.cursor()
        self.__db_cursor.execute(query, params)
        self.__db_connection.commit()
        self.__db_cursor.close()
