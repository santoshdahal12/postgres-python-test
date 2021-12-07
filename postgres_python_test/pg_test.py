""" Module for testing postgres update"""
import os
import psycopg2


class DBConnector:
    """Establishes connection to local postgres"""

    def __init__(self):
        """ init method that establishes connection
            - *dbname*: the database name
            - *user*: user name used to authenticate
            - *password*: password used to authenticate
            - *host*: database host address (defaults to UNIX socket if not provided)
            - *port*: connection port number (defaults to 5432 if not provided)
        """
        self.host = 'localhost'
        self.user = os.environ['user']

    def connect(self):
        """ Connects to somedb in local postgres"""
        connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password='',
            database='somedb'
        )
        return connection

    def get_all_changed_rows(self):
        """ Get all"""
        sql = "Select user_id from users where email like '%test_changed%'"
        connection = self.connect()
        with connection:
            with connection.cursor() as curs:
                curs.execute(sql)
                return [r[0] for r in curs.fetchall()]

    def bulk_insert(self):
        """ bulk inserts million records in no time """
        connection = self.connect()
        with connection:
            with connection.cursor() as curs:
                with open('users.csv', 'r') as f:
                    next(f)
                    curs.copy_from(f, 'users', sep=',')

    def update(self, row):
        """ updates and test concurrency """
        sql = f"""Update users set email='test_changed_{row}' where username='test_{row}'"""
        print(sql)
        connection = self.connect()
        with connection:
            with connection.cursor() as curs:
                curs.execute(sql)
