import sqlite3

books = sqlite3.connect('books.db')
user = sqlite3.connect('users.db')

b = books.cursor()
u = user.cursor()


def create():
    b.execute('CREATE TABLE IF NOT EXISTS Books(Title TEXT, Author TEXT, Year INTEGER)')
    u.execute('CREATE TABLE IF NOT EXISTS Users(Name TEXT, Key BLOB, Uid BLOB)')


create()


class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.next = None
        b.execute("INSERT INTO Books(Title, Author, Year) VALUES(?, ?, ?)", (title, author, year))
        books.commit()


class User:

    def __init__(self, name, uid, key):
        self.name = name
        self.key = key
        self.uid = uid
        self.books = []
        self.next = None
        u.execute("INSERT INTO Users(Name, Key, Uid) VALUES(?, ?, ?)", (name, key, uid))
        user.commit()


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

    def register(self, user):
        if self.user is None:
            self.user = user
        else:
            prev = self.user
            while True:
                if prev.next is None:
                    break
                prev = prev.next
                prev.next = user

    def login(self, uid, key):
        if uid == self.user.uid:
            if key == self.user.key:
                return
            else:
                print("Wrong Password")
                return False
        else:
            prev = self.user
            while True:
                if prev.next is None:
                    print("NO USER")
                    return False
                else:
                    if uid == prev.next.log.uid:
                        if key == prev.next.key:
                            return
                        else:
                            print("Wrong Password")
                            return False
                    prev = prev.next

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

    def issue(self, name, id):
        if self.head is None:
            print("NO BOOKS")
            return
        t = self.head
        u = self.user
        while True:
            if name == t.title:
                while True:
                    if id == u.uid:
                        u.books.append(name)
                        print("ISSUED")
                        return
                    elif u.next is None:
                        print("ID INVALID")
                        return
                    u = u.next
            elif t.next is None:
                print("NO BOOKS")
                return
            t = t.next

    def rturn(self):
        pass

    def displayUser(self, id):
        if self.user is None:
            print("Empty!")
            return
        c = self.user
        while True:
            if c is None:
                break
            if id == c.uid:
                b = c.books
                print("Name:"+c.name, "UID:"+c.uid)
                print("Books:", end=" ")
                for a in(b):
                    print(a,"|", end=" ")
            c = c.next

    def displayBook(self):
        if self.head is None:
            print("Empty!")
            return
        c = self.head
        while True:
            if c is None:
                break
            print("|  {} | {} | {}".format(c.title, c.author, c.year))
            print("|-------------------------------------|")
            c = c.next


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
        u = input("|  Enter:")
        if u == "n":
            new()
        if u == "l":
            login()

    def login():
        print("|----------Login---------|")
        uid = input("|  uid:")
        key = input("|  key:")
        if lib.login(uid, key) is False:
            login()
        return

    def new():
        print("|-------REGISTER--------|")
        a = input("|  name:")
        b = input("|  uid:")
        c = input("|  key:")
        lib.register(User(a, b, c))
        login()

    def book_menu():
        print("|========LIBRARY========|")
        print("|  1 - display books")
        print("|  2 - add books")
        print("|  3 - issue")
        print("|  0 - exit")
        a = int(input("|  Enter:"))
        #print("|=======================|")
        if a == 1:
            print("|----------------BOOKS----------------|")
            #print("|----------------------------------|n")
            lib.displayBook()
        if a == 2:
            d = input("title:")
            b = input("author:")
            c = int(input("year:"))
            lib.insert(Book(d, b, c))
            print("|============BOOKS============|")
            lib.displayBook()
            print("|=========================|")
        if a == 3:
            n = input("Enter title:")
            u = input("UID:")
            lib.issue(n, u)
            lib.displayUser(u)
            print("")
        if a == 0:
            exit()

    log_menu()
    while True:
        book_menu()
