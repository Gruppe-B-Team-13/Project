import os
from contextlib import closing
import sqlite3
from datetime import date, datetime

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)
## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)

class BaseDataAccess:
    def __init__(self, db_connection_str: str = None):
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE")
            if self.__db_connection_str is None:
                raise Exception("DB_FILE environment variable and parameter path is not set.")
        else:
            self.__db_connection_str = db_connection_str

    def _connect(self):
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()):
        with closing(self._connect()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        with closing(self._connect()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> (int, int):
        with closing(self._connect()) as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
            finally:
                cur.close()
        return cur.lastrowid, cur.rowcount