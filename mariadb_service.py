#!/usr/bin/python
from config import mariadb_ini
import mysql.connector as mariadb

class Mariadb:
    def __init__(self):
        self._conn = mariadb.connect(**mariadb_ini)
        self._curs = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._curs

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def rollback(self):
        self.connection.rollback()

    def execute(self, sql, params=None):
        try:
            self.cursor.execute(sql, params or ())
            self.commit()
        except mariadb.Error as e:
            self.rollback()
            print("Error:\n{}\n{}".format(e.args[0], e.args[1]))
        self.close()

    def get_rows(self, sql):
        self._conn = mariadb.connect(**mariadb_ini)
        self._curs = self._conn.cursor()
        self._curs.execute(sql)
        titles = [i[0] for i in self._curs.description]
        rows = [list(i) for i in self._curs.fetchall()]
        rows.insert(0, titles)
        self.close()
        return rows

    def fetchall(self):
        return self.cursor.fetchall()
 
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
