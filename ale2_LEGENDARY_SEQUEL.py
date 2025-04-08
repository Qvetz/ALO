import sqlite3
def main():
    conn = sqlite3.connect('medical.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Durka (PatientID, Name, SecondName, Phone)
                                        VALUES(4224576, 'Максимильяно', 'Тухачевский', 79187776354),
                                              (9943833, 'Джон', 'Доу', 79998266655),
                                              (2281337, 'Иосиф', 'Джугашвили', 71488228666)''')

    cur.execute('''INSERT INTO Doctor (DoctorID, Name, SecondName, Phone, Salary)
                                      VALUES(4342335, 'Марк','Роббер',79994337897, 49999),
                                            (1232133,'Джимми', 'Нейтрон',78828747665, 45000),
                                            (3213124, 'Алекс', 'Хирш',79917778723, 100000)''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()