import sqlite3
def main():
    conn = sqlite3.connect('medical.db')
    cur = conn.cursor()
    
    cur.execute('SELECT PatientID, Name, SecondName, Phone FROM Durka')
    print('Пациенты:')
    results = cur.fetchall()
    for row in results:

    print(f'{row[0]:10}{row[1]:15}{row[2]:15}{row[3]:15}')
    print()

    cur.execute('SELECT DoctorID, Name, SecondName, Phone, Salary FROM Doctor')
    print('Врачи:')
    results2 = cur.fetchall()
    for row in results2:

    print(f'{row[0]:10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:10}')

    conn.close()

if __name__ == '__main__':
    main()