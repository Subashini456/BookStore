import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,Title text,Author text,Year INTEGER,isbn INTEGER)")
        self.conn.commit()

    def insert_data(self,Title,Author,Year,isbn):
        self.curr.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(Title,Author,Year,isbn))
        self.conn.commit()

    def delete_item(self,id):
        self.curr.execute("DELETE FROM books WHERE id = ?",(id,))
        self.conn.commit()

    def update_data(self,id,Title,Author,Year,isbn):
        self.curr.execute("UPDATE books SET Title = ? ,Author = ? ,Year = ? , isbn = ? WHERE id = ?",(Title,Author,Year,isbn,id))
        self.conn.commit()

    def view(self):
        self.curr.execute("SELECT * FROM books")
        rows = self.curr.fetchall()
        return rows

    def search(self,Title="",Author="",Year="",isbn=""):
        self.curr.execute("SELECT * FROM books WHERE Title=? OR Author=? OR Year=? OR isbn=?",(Title,Author,Year,isbn))
        rows = self.curr.fetchall() 
        return rows

    def __del__(self):
        self.conn.close()    

#delete_item(4)
#delete_item(5)
#delete_item(6)
#insert_data('Harry Poter','J K Rowling',1990,12345)
#insert_data('Fault in our Stars','Jonny Green',2000,98765)
#insert_data('2 States','Chetan Bhagat',2010,56478) 
#update_data(3,"Half GirlFriend","Chetan Bhagat",2010,456123)
#print(search(Author="Chetan Bhagat"))
#print(view())