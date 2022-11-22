from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = connect(host='mouse.db.elephantsql.com', user='iobvohbo', database='iobvohbo',
                       password='6xmUyMhZFPbdrNRfN3W2CnOOSIN7O0AI')  # отримання підклюсення
        yield conn
    except Error as err:
        print(err)
        conn.rollback()  # якщо виникла помилка відмотує дані назад
    finally:
        conn.close()  # закрити підключення
        