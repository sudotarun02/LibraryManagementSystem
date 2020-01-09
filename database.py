import sqlite3

li = sqlite3.connect('Library.db')

l = li.cursor()


def create():
    l.execute('CREATE TABLE IF NOT EXISTS Books(Title TEXT, Author TEXT, Year INTEGER)')
    l.execute('CREATE TABLE IF NOT EXISTS Users(Name TEXT, Key BLOB, Uid BLOB)')
    l.execute('CREATE TABLE IF NOT EXISTS Issue(Uid BLOB, books TEXT)')


def check_user(id, key):
    l.execute('SELECT * FROM Users WHERE Uid=? AND Key=?', (id, key))
    if l.fetchone() is not None:
        return True
    return False


def issue(uid, book):
    l.execute('SELECT Title FROM Books WHERE Title=?', (book,))
    a = l.fetchone()
    l.execute('SELECT Uid FROM Users WHERE Uid=?', (uid,))
    b = l.fetchone()
    if a and b is not None:
        l.execute('SELECT * FROM Issue WHERE Uid=? AND books=?', (uid, book))
        if l.fetchone() is None:
            l.execute("INSERT INTO Issue(Uid, books) VALUES(?, ?)", (uid, book))
            li.commit()
        else:
            print("Book already Issued.")


def retrn(id, book):
    l.execute('SELECT * FROM Issue WHERE Uid=? AND books=?', (id, book))
    if l.fetchone() is not None:
        l.execute("DELETE FROM Issue WHERE Uid=? AND books=?", (id, book))
        li.commit()
        return
