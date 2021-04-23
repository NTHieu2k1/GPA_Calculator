import sqlite3

def db_access(): # Give rights to access the database
    subject_db = sqlite3.connect("FU All Subjects.db")
    return subject_db.cursor()

def is_exist_subject_id(subject_id):
    db = db_access()
    db.execute("SELECT * FROM Subjects WHERE Subject_Code = ?", (subject_id,))
    retrieve = db.fetchone()
    # None value means subject code is not exist
    if retrieve == None:
        return False
    else:
        return True

def filter_subject_ID(subject_id): # Filter subject code list for first 3 letters of the code input
    db = db_access()
    subject_ID_filter = list()
    db.execute("SELECT Subject_Code FROM Subjects")
    subject_ID_list = db.fetchall()
    # Filter subject code
    for id in subject_ID_list:
        if id[0][0:3] == subject_id:
            subject_ID_filter.append(id[0])
    return subject_ID_filter

def get_credit(subject_id):
    db = db_access()
    db.execute("SELECT No_of_Credits FROM Subjects WHERE Subject_Code = ?", (subject_id,))
    no_of_credit = db.fetchone()[0]
    return no_of_credit

class Student:

    def __init__(self, mark_data):
        self.mark_data = mark_data

    def get_total_mark(self):
        total_mark = 0
        for subject in self.mark_data:
            total_mark += (self.mark_data[subject] * get_credit(subject))
        return total_mark

    def get_sum_credits(self):
        total_credits = 0
        for subject in self.mark_data:
           total_credits += get_credit(subject)
        return total_credits

    def get_GPA_score(self, total_marks, total_credits):
        return (total_marks / total_credits)