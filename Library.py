import sqlite3

li = sqlite3.connect('Library.db')
l = li.cursor()


def create():
    l.execute('CREATE TABLE IF NOT EXISTS Books(Title TEXT, Author TEXT, Year INTEGER, Uid BLOB)')
    l.execute('CREATE TABLE IF NOT EXISTS Users(Name TEXT, Key BLOB, Uid BLOB)')


def display():
    l.execute('SELECT * FROM Books')
    print(l.fetchall())


def check_user(id, key):
    l.execute('SELECT * FROM Users WHERE Uid=? AND Key=?', (id, key))
    if l.fetchone() is not None:
        return True
    return False


def check_book(title, uid):
    l.execute('SELECT Title FROM Books WHERE Title=?', (title,))
    a = l.fetchone()
    l.execute('SELECT Uid FROM Users WHERE Uid=?', (uid,))
    b = l.fetchone()
    if a is not None:
        if b is not None:
            print(a)
            l.execute('INSERT INTO Books(Uid) VALUES(?)', uid)
            li.commit()
        else:
            print("No user")
    else:
        print("no books")


create()


class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.next = None
        l.execute("INSERT INTO Books(Title, Author, Year) VALUES(?, ?, ?)", (title, author, year))
        li.commit()


class User:

    def __init__(self, name, uid, key):
        self.name = name
        self.key = key
        self.uid = uid
        self.books = []
        self.next = None
        l.execute("INSERT INTO Users(Name, Key, Uid) VALUES(?, ?, ?)", (name, key, uid))
        li.commit()


# class Admin:
#     def __init__(self):
#         pass
#
#     def userDetails(self):
#         pass
#


class Library:
    def __init__(self):
        self.head = None
        self.user = None

    def register(self, users):
        if self.user is None:
            self.user = users
        else:
            prev = self.user
            while True:
                if prev.next is None:
                    break
                prev = prev.next
                prev.next = users

    def login(self, uid, key):
        if check_user(uid, key):
            return
        print("wrong entry")
        return False

    def insert(self, book):
        if self.head is None:
            self.head = book
        else:
            prev = self.head
            while True:
                if prev.next is None:
                    break
                prev = prev.next
            prev.next = book

    def issue(self, name, uid):
        check_book(name, uid)

    def rturn(self):
        pass

    def displayUser(self, uid):
        if self.user is None:
            print("Empty!")
            return
        c = self.user
        while True:
            if c is None:
                break
            if uid == c.uid:
                b = c.books
                print("Name:" + c.name, "UID:" + c.uid)
                print("Books:", end=" ")
                for a in b:
                    print(a, "|", end=" ")
            c = c.next

    # def displayBook(self):
    #     # b.execute("SELECT Title, Author, Year FROM Books")
    #     if self.head is None:
    #         print("Empty!")
    #         return
    #     c = self.head
    #     while True:
    #         if c is None:
    #             break
    #         print("|  {} | {} | {}".format(c.title, c.author, c.year))
    #         print("|-------------------------------------|")
    #         c = c.next


if __name__ == '__main__':

    lib = Library()
    # t = ["ALCHEMIST", "5 AM", "RICH DAD POOR DAD", "THINK", "UNKNOWN"]
    # a = ["ROBIN", "ROBIN SHARMA", "ROBERT", "NAPOLIAN", "ANNONYMOUS"]
    # y = ["2001", "2012", "2015", "1995", "1999"]
    # for n in range(len(t)):
    #     lib.insert(Book(t[n], a[n], y[n]))


    def log_menu():
        print("|========LIBRARY========|")
        print("|  n - new user")
        print("|  l - login")
        print("|-----------------------|")
        ch = input("|  Enter:")
        if ch == "n":
            new()
        if ch == "l":
            login()

    def login():
        print("|---------Login---------|")
        uid = input("|  uid:")
        key = input("|  key:")
        if lib.login(uid, key) is False:
            login()
        return

    def new():
        print("|-------REGISTER--------|")
        a = input("|  name:")
        uid = input("|  uid:")
        c = input("|  key:")
        lib.register(User(a, uid, c))
        login()

    def book_menu():
        print("|========LIBRARY========|")
        print("|  1 - display books")
        print("|  2 - add books")
        print("|  3 - issue")
        print("|  0 - exit")
        a = int(input("|  Enter:"))
        if a == 1:
            print("|----------------BOOKS----------------|")
            display()
        if a == 2:
            d = input("title:")
            b = input("author:")
            c = int(input("year:"))
            lib.insert(Book(d, b, c))
            print("|============BOOKS============|")
            display()
            print("|=========================|")
        if a == 3:
            n = input("Enter title:")
            u = input("UID:")
            lib.issue(n, u)
            # lib.displayUser(u)
            print("")
        if a == 0:
            exit()

    log_menu()
    while True:
        book_menu()
