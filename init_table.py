from connection import create_connection
from psycopg2 import DatabaseError


def create_table(conn, sql):
    try:
        curs = conn.cursor()
        curs.execute(sql)
        curs.close()
        conn.commit()
    except DatabaseError as err:
        print(err)


if __name__ == '__main__':
    sql_create_table_groups = """
    CREATE TABLE IF NOT EXISTS groups (
    id_group SERIAL PRIMARY KEY,
    name_group VARCHAR(25)
    );
    """
    sql_create_table_students = """
    CREATE TABLE IF NOT EXISTS students (
    id_stud SERIAL PRIMARY KEY,
    fullname_stud VARCHAR(50),
    id_group INT,
    FOREIGN KEY (id_group) REFERENCES groups (id_group)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """
    sql_create_table_professors = """
    CREATE TABLE IF NOT EXISTS professors (
    id_prof SERIAL PRIMARY KEY,
    name_prof VARCHAR(50)
    );
    """
    sql_create_table_subjects = """
    CREATE TABLE IF NOT EXISTS subjects (
    id_sub SERIAL PRIMARY KEY,
    name_sub VARCHAR(50),
    id_prof INT,
    FOREIGN KEY (id_prof) REFERENCES professors (id_prof)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """
    sql_create_table_grades = """
    CREATE TABLE IF NOT EXISTS grades (
    id_grad SERIAL PRIMARY KEY,
    id_stud INT,
    id_sub INT,
    grade INT,
    date_of DATE,
    FOREIGN KEY (id_stud) REFERENCES students (id_stud)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_sub) REFERENCES subjects (id_sub)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_table_groups)
            print('The creation of the table "groups" is complete')
            create_table(conn, sql_create_table_students)
            print('The creation of the table "students" is complete')
            create_table(conn, sql_create_table_professors)
            print('The creation of the table "professors" is complete')
            create_table(conn, sql_create_table_subjects)
            print('The creation of the table "subjects" is complete')
            create_table(conn, sql_create_table_grades)
            print('The creation of the table "grades" is complete')
