from datetime import date
import faker
from random import randint, choice
import sqlite3

N_STUDENTS = 50
N_GROUPS = 3
N_SUBJECTS = 8
N_LECTURERS = 5
N_MARKS = 20

DB_NAME = 'univ.db'

FKR = faker.Faker()

def generate_fake_data():

    students = [FKR.name() for _ in range(N_STUDENTS)]
    groups = [f'MO{i}' for i in range(1, N_GROUPS+1)]
    subjects = ['Algebra', 'Biology', 'Geography', 'History', 'Literature', 'Geometry']
    lecturers = [FKR.name() for _ in range(N_LECTURERS)]
    return students, groups, subjects, lecturers

def prepeare_data(students, groups, subjects, lecturers):
    students_tpl = [(student, randint(1, N_GROUPS)) for student in students]
    groups_tpl = [(group, ) for group in groups]
    subjects_tpl = [(subject, randint(1, N_LECTURERS)) for subject in subjects]
    lecturers_tpl = [(lecturer, ) for lecturer in lecturers]
    marks_tpl = [(randint(50, 100), date(2022, randint(1, 12), randint(1, 28)), st_id, randint(1, N_SUBJECTS)) for _ in range(randint(10, N_MARKS)) for _ in range(N_SUBJECTS) for st_id in range(1, N_STUDENTS+1)]
    return students_tpl, groups_tpl, subjects_tpl, lecturers_tpl, marks_tpl

def insert_data(students_tpl, groups_tpl, subjects_tpl, lecturers_tpl, marks_tpl):

    insert_student = 'INSERT INTO students (fullname, group_id) VALUES (?, ?)'
    insert_groups = 'INSERT INTO groups (title) VALUES (?)'
    insert_lecturers = 'INSERT INTO lecturers (fullname) VALUES (?)'
    insert_subjects = 'INSERT INTO subjects (title, lecturer_id) VALUES(?, ?)'
    insert_marks = 'INSERT INTO marks (mark, m_date, student_id, subject_id) VALUES (?, ?, ?, ?)'

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.executemany(insert_groups, groups_tpl)
        cur.executemany(insert_student, students_tpl)
        cur.executemany(insert_lecturers, lecturers_tpl)
        cur.executemany(insert_subjects, subjects_tpl)
        cur.executemany(insert_marks, marks_tpl)

if __name__ == '__main__':
    insert_data(*prepeare_data(*generate_fake_data()))
