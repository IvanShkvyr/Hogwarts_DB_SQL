from connection import create_connection


def execute_query(sql):
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    sql_quety_1 = """
    SELECT s.fullname_stud, round(avg(g.grade),2) AS avg_grede
    FROM grades g
    LEFT JOIN students s ON s.id_stud = g.id_stud
    GROUP BY s.id_stud
    ORDER BY avg_grede DESC
    LIMIT 5;
    """
    sql_quety_2 = """
    SELECT s.fullname_stud, round(avg(g.grade),2) AS avg_grede, sub.name_sub
    FROM grades g
    LEFT JOIN students s ON s.id_stud = g.id_stud
    LEFT JOIN subjects sub ON sub.id_sub = g.id_sub
    WHERE sub.id_sub = 1
    GROUP BY s.id_stud, sub.name_sub
    ORDER BY avg_grede DESC
    LIMIT 1;
    """
    sql_quety_3 = """
    SELECT gru.name_group, round(avg(g.grade),2) AS avg_grede, sub.name_sub
    FROM grades g
    LEFT JOIN students s ON s.id_stud = g.id_stud
    LEFT JOIN subjects sub ON sub.id_sub = g.id_sub
    LEFT JOIN groups gru ON gru.id_group = s.id_group
    WHERE sub.id_sub = 1
    GROUP BY gru.id_group, sub.name_sub
    ORDER BY gru.id_group DESC;
    """
    sql_quety_4 = """
    SELECT round(avg(g.grade),2)
    FROM grades g
    """
    sql_quety_5 = """
    SELECT s.name_sub, p.name_prof
    FROM professors p
    LEFT JOIN subjects s ON p.id_prof = s.id_prof;
    """
    sql_quety_6 = """
    SELECT s.fullname_stud, g.name_group 
    FROM students s
    LEFT JOIN groups g  ON g.id_group = s.id_group;
    """
    sql_quety_7 = """
    SELECT g.name_group, s.fullname_stud, gr.grade, gr.date_of 
    FROM grades gr
    LEFT JOIN students s ON s.id_stud = gr.id_stud 
    LEFT JOIN groups g  ON g.id_group = s.id_group
    LEFT JOIN subjects sub ON sub.id_sub = gr.id_sub
    WHERE g.id_group = 1 AND sub.id_sub = 1
    """
    sql_quety_8 = """
    SELECT g.name_group, s.fullname_stud,sub.name_sub, gr.grade, gr.date_of 
    FROM grades gr
    LEFT JOIN students s ON s.id_stud = gr.id_stud 
    LEFT JOIN groups g  ON g.id_group = s.id_group
    LEFT JOIN subjects sub ON sub.id_sub = gr.id_sub
    WHERE g.id_group = 1 AND sub.id_sub = 3 AND gr.date_of = (
    SELECT max(gr.date_of)
    FROM grades gr
    WHERE g.id_group = 1 AND sub.id_sub = 3
    );
        """
    sql_quety_9 = """
    SELECT s.name_sub, st.fullname_stud 
    FROM grades g
    RIGHT JOIN subjects s  ON g.id_sub = s.id_sub 
    LEFT JOIN students st ON st.id_stud = g.id_stud
    WHERE g.id_stud = 2
    GROUP BY s.name_sub, st.fullname_stud;
        """
    sql_quety_10 = """
    SELECT s.name_sub, st.fullname_stud, p.name_prof 
    FROM grades g
    RIGHT JOIN subjects s  ON g.id_sub = s.id_sub 
    LEFT JOIN students st ON st.id_stud = g.id_stud
    LEFT JOIN professors p ON p.id_prof = s.id_prof 
    WHERE p.id_prof = 1 AND st.id_stud = 2
    GROUP BY s.name_sub, st.fullname_stud, p.name_prof;
        """
    sql_quety_11 = """
    SELECT st.fullname_stud, p.name_prof, avg(g.grade) AS avg_grade
    FROM grades g
    RIGHT JOIN subjects s  ON g.id_sub = s.id_sub 
    LEFT JOIN students st ON st.id_stud = g.id_stud
    LEFT JOIN professors p ON p.id_prof = s.id_prof 
    WHERE p.id_prof = 1 AND st.id_stud = 2
    GROUP BY st.fullname_stud, p.name_prof;
    """
    sql_quety_12 = """
    SELECT p.name_prof, avg(g.grade) AS avg_grade
    FROM grades g
    RIGHT JOIN subjects s  ON g.id_sub = s.id_sub 
    LEFT JOIN professors p ON p.id_prof = s.id_prof 
    WHERE p.id_prof = 4
    GROUP BY p.name_prof;
    """


    print('\nQUERY 1: 5 студентів із найбільшим середнім балом з усіх предметів.')
    ans = execute_query(sql_quety_1)
    for i in ans:
        print('{:<20} має середній бал - {:^5}'.format(i[0], i[1]))

    print('\nQUERY 2: 1 студент із найвищим середнім балом з одного предмета.')
    ans = execute_query(sql_quety_2)
    for i in ans:
        print('{:<20} має найвищий середній бал - {:^5} з дисципліни "{:<25}"'.format(i[0], i[1], i[2]))

    print('\nQUERY 3: Середній бал в групі по одному предмету.')
    ans = execute_query(sql_quety_3)
    for i in ans:
        print('Середній бал в "{:<12}"  - {:^5} з дисципліни "{:<25}"'.format(i[0], i[1], i[2]))

    print('\nQUERY 4: Середній бал у потоці.')
    ans = execute_query(sql_quety_4)
    for i in ans:
        print('Середній бал в потоці -{:^12}'.format(i[0],))

    print('\nQUERY 5: Які курси читає викладач.')
    ans = execute_query(sql_quety_5)
    for i in ans:
        print('Дисципліну {:<30} викладає {:<20}'.format(i[0], i[1]))

    print('\nQUERY 6: Список студентів у групі.')
    ans = execute_query(sql_quety_6)
    for i in ans:
        print('{:<20} навчається в групі {:<12}'.format(i[0], i[1]))

    print('\nQUERY 7: Оцінки студентів у групі з предмета.')
    ans = execute_query(sql_quety_7)
    for i in ans:
        print('В групі {:^12} студент {:^20} отримав {:^4} балів {:^10} числа'.format(i[0], i[1], i[2], i[3].strftime('%d %m %Y')))

    print('\nQUERY 8: Оцінки студентів у групі з предмета на останньому занятті.')
    ans = execute_query(sql_quety_8)
    for i in ans:
        print('В {:<20} студент {:<20} з дисципліни {:<20} отримав {:^4} {:>10}'.format(i[0], i[1], i[2], i[3], i[4].strftime('%d %m %Y')))

    ans = execute_query(sql_quety_9)
    print(f'\nQUERY 9: Список курсів, які відвідує студент {ans[0][1]}:')
    for i in ans:
        print('-- {:<25}'.format(i[0]))

    ans = execute_query(sql_quety_10)
    print(f'\nQUERY 10: Список курсів, які студенту {ans[0][1]} читає викладач {ans[0][2]}.')
    for i in ans:
        print('-- {:<25}'.format(i[0]))

    ans = execute_query(sql_quety_11)
    print(f'\nQUERY 11: Середній бал, який викладач {ans[0][1]} ставить студенту {ans[0][0]} становить {ans[0][2]}.')

    ans = execute_query(sql_quety_12)
    print(f'\nQUERY 12: Середній бал, який ставить {ans[0][0]} -- {ans[0][1]}.')
