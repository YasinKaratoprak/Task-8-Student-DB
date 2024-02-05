import sqlite3
Connection = sqlite3.connect("TESTDB.db")
class Database:
    def __init__(self):
        self.cursor = Connection.cursor()

    def getColumnNames(self):
        self.cursor.execute("PRAGMA table_info(STUDENTS)")
        Columns = self.cursor.fetchall()
        return Columns

    def updateStudent(self):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS;")
            students = self.cursor.fetchall()

            print("öğrenciler:")
            for student in students:
                print(student)

            student_id = int(input("Güncellemek istediğiniz öğrencinin ID'sini girin: "))
            column_name = input("Hangi sütunu güncellemek istersiniz (studentName, studentSurname): ")
            new_value = input("Yeni değeri girin: ")

            self.cursor.execute("UPDATE STUDENTS SET {} = ? WHERE studentId = ?;".format(column_name),
                                (new_value, student_id,))
            Connection.commit()
            print("Veri güncellendi.")
            self.getAllStudents()
        except Exception as e:
            print("error:", e)

    def searchStudent(self, value):
        try:
            value = '%{}%'.format(value)
            self.cursor.execute("SELECT * FROM STUDENTS WHERE studentName LIKE ? OR studentSurname LIKE ?;",
                                (value, value,))
            students = self.cursor.fetchall()
            return students
        except Exception as e:
            print("error:", e)

    def getAllStudents(self):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS ORDER BY studentName ASC;")
            students = self.cursor.fetchall()
            print("Öğrenciler:")
            for student in students:
                print(student)
        except Exception as e:
            print("error:", e)

    def deleteStudent(self):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS;")
            students = self.cursor.fetchall()

            print("Öğrenciler:")
            for student in students:
                print(student)

            student_id = int(input("Silmek istediğiniz öğrencinin ID'sini girin: "))
            self.cursor.execute("DELETE FROM STUDENTS WHERE studentId = ?;", (student_id,))
            Connection.commit()
            print("Öğrenci silindi.")
            self.getAllStudents()
        except Exception as e:
            print("error:", e)

    def insertStudent(self, studentName, studentSurname):
        try:
            self.cursor.execute("INSERT INTO STUDENTS (studentName, studentSurname) VALUES (?, ?);",
                                (studentName, studentSurname,))
            Connection.commit()
            print("Yeni öğrenci eklendi.")
            self.getAllStudents()
        except Exception as e:
            print("error:", e)

    def delete_all(self):
        try:
            self.cursor.execute("DELETE FROM STUDENTS;")
            Connection.commit()
            print("Tüm öğrenciler silindi.")
            self.getAllStudents()
        except Exception as e:
            print("error:", e)
while True:
    print("Merhaba, öğrenci veritabanında ne işlem yapmak istersiniz?")
    print("[1] Öğrenci Ara")
    print("[2] Öğrenci Güncelleştir")
    print("[3] Öğrenci Ekle")
    print("[4] Öğrenci Sil")
    print("[5] Tüm veritabını sil")

    choice = input("Seçiminizi yapın (1-5): ")

    if choice == '1':
        search_value = input("Aramak istediğiniz öğrencinin adını veya soyadını girin: ")
        results = Database().searchStudent(search_value)
        print("Arama sonuçları:")
        for student in results:
            print(student)

    elif choice == '2':
        Database().updateStudent()

    elif choice == '3':
        student_name = input("Eklemek istediğiniz öğrencinin adını girin: ")
        student_surname = input("Eklemek istediğiniz öğrencinin soyadını girin: ")
        Database().insertStudent(student_name, student_surname)

    elif choice == '4':
        Database().deleteStudent()

    elif choice == "5":
        print("Emin misin?")
        answer = input("evet veya hayır yaz: ")
        if answer == "evet":
            Database().delete_all()
            print("Veritabanı temizlendi")
        elif answer == "hayır":
            pass
    else:
        print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı seçin.")
