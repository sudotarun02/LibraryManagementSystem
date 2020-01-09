from database import*


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
        issue(uid, name)
        l.execute('SELECT books FROM Issue WHERE Uid=?', uid)
        print(l.fetchall())


if __name__ == '__main__':
    create()
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
        elif ch == "l":
            login()
        else:
            print("ENTER VALID INPUT")
            log_menu()

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
        print("|  4 - return")
        print("|  0 - exit")
        a = input("|  Enter:")
        if a == "1":
            print("|----------------BOOKS----------------|")
            l.execute('SELECT * FROM Books order by Title asc')
            print(l.fetchall())
        elif a == "2":
            d = input("title:")
            b = input("author:")
            c = int(input("year:"))
            lib.insert(Book(d, b, c))
            print("|============BOOKS============|")
            print("|=========================|")
        elif a == "3":
            n = input("Enter title:")
            u = input("UID:")
            lib.issue(n, u)
            print("")
        elif a == "4":
            n = input("Enter title:")
            u = input("UID:")
            retrn(u, n)
            l.execute('SELECT books FROM Issue WHERE Uid=?', u)
            print(l.fetchall())
        elif a == "0":
            exit()
        else:
            print("ENTER VALID INPUT")
            book_menu()

    log_menu()
    while True:
        book_menu()
