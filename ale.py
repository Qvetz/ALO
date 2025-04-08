import sqlite3
def main():
    conn = sqlite3.connect('medical.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Durka(PatientID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        SecondName TEXT,
                                        Phone INTEGER)''')
    cur.execute('''CREATE TABLE Doctor(DoctorID INTEGER PRIMARY KEY NOT NULL,
                                       Name TEXT,
                                       SecondName TEXT
                                       Phone INTEGER,
                                       Salary float)''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()