from connection import create_connection
from datetime import datetime, timedelta
from random import randint


groups_data = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
students_data = {
    "Hermione Granger": 1,
    "Harry Potter": 1,
    "Minerva McGonagall": 1,
    "Angelina Johnson": 1,
    "Sirius Black": 1,
    "Bridget Wenlock": 2,
    "Fat Friar": 2,
    "Hengist of Woodcroft": 2,
    "Susan Bones": 2,
    "Zacharias Smith": 2,
    "Luna Lovegood": 3,
    "Michael Corner": 3,
    "Sue Li": 3,
    "Badeea Ali": 3,
    "Padma Patil": 3,
    "Barnaby Lee": 4,
    "Zubeida Khan": 4,
    "Yatin Bhagat": 4,
    "Draco Malfoy": 4,
    "Salazar Slytherin": 4
}
professors_data = ['Remus Lupin', 'Pomona Sprout', ' Silvanus Kettleburn', 'Minerva McGonagall', 'Bathsheda Babbling' ]
subjects_data = {
    'Defence Against the Dark Arts': 1,
    'Transfiguration': 2,
    'Charms': 3,
    'Potions': 4,
    'History of Magic': 5,
    'Astronomy': 1,
    'Study of Ancient Runes': 2,
    'Care of Magical Creatures': 3
}


def give_date():
    current_date_edu = datetime.now().date()
    start_edu = datetime(2022, 9, 1).date()
    time_delta = int((current_date_edu - start_edu) / timedelta(days=1))

    while True:
        date_of_grade = start_edu + timedelta(days=(randint(1, time_delta)))
        if date_of_grade.isoweekday() < 6:
            return date_of_grade
        else:
            continue


if __name__ == '__main__':
    sql_insert_groups = """
    INSERT INTO groups (name_group) VALUES (%s)
    """
    sql_insert_students = """
    INSERT INTO students (fullname_stud, id_group) VALUES (%s, %s)
    """
    sql_insert_professors = """
    INSERT INTO professors (name_prof) VALUES (%s)
    """
    sql_insert_subjects = """
    INSERT INTO subjects (name_sub, id_prof) VALUES (%s, %s)
    """
    sql_insert_grades = """
    INSERT INTO grades (id_stud, id_sub, grade, date_of) VALUES (%s, %s, %s, %s)
    """

    with create_connection() as conn:
        if conn is not None:
            curs = conn.cursor()

            for i in groups_data:
                curs.execute(sql_insert_groups, (i,))
            print('The table "groups" is filled')

            for i, j in students_data.items():
                curs.execute(sql_insert_students, (i, j))
            print('The table "students" is filled')

            for i in professors_data:
                curs.execute(sql_insert_professors, (i, ))
            print('The table "professors" is filled')

            for i, j in subjects_data.items():
                curs.execute(sql_insert_subjects, (i, j))
            print('The table "subjects" is filled')

            for i in range(len(students_data)):
                for j in range(20):
                    curs.execute(sql_insert_grades, (i + 1, randint(1, len(subjects_data)), randint(4, 12), give_date()))
            print('The table "grades" is filled')

            curs.close()
            conn.commit()
