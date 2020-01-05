class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.next = None


class User:

    def __init__(self, name, uid, key):
        self.name = name
        self.key = key
        self.uid = uid
        self.books = []
        self.next = None


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
                pass
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
                            pass
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
                print("|    {}  |   {}  |   {}  |".format(c.name, c.uid, b))
            c = c.next

    def displayBook(self):
        print("|==TITLE==|==AUTHOR==|==YEAR==|")
        if self.head is None:
            print("Empty!")
            return
        c = self.head
        while True:
            if c is None:
                break
            print("{}|{}|{}|".format(c.title, c.author, c.year))
            c = c.next


lib = Library()
t = ["ALCHEMIST", "5 AM", "RICH DAD POOR DAD", "THINK", "UNKNOWN"]
a = ["ROBIN", "ROBIN SHARMA", "ROBERT", "NAPOLIAN", "ANNONYMOUS"]
y = ["2001", "2012", "2015", "1995", "1999"]
for n in range(len(t)):
    lib.insert(Book(t[n],a[n],y[n]))

while True:
    print("|========LIBRARY========|")
    print("Menu:n for new user, l for login")
    u = input("")
    if u == "n":
        a = input("name:")
        b = input("uid:")
        c = input("key:")
        lib.register(User(a, b, c))
        print("Login")
        b = input("uid:")
        c = input("key:")
        if lib.login(b, c) is True:
            break
    if u == "l":
        b = input("uid:")
        c = input("key:")
        if lib.login(b, c) is True:
            break
    break

while True:
    print("|========LIBRARY========|")
    print("|  1-display books")
    print("|  2-add books")
    print("|  3-issue")
    print("|  0-exit")
    a = int(input("|  Enter:"))
    print("|=======================|")
    if a == 1:
        print("====BOOKS====")
        lib.displayBook()
    if a == 2:
        a = input("title:")
        b = input("author:")
        c = int(input("year:"))
        lib.insert(Book(a, b, c))
        print("|============BOOKS============|")
        lib.displayBook()
        print("|=========================|")
    if a == 3:
        n = input("Enter title:")
        u = input("UID")
        lib.issue(n, u)
        lib.displayUser(u)
    if a == 0:
        break
