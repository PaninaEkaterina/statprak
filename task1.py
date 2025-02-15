# task 1
print("task1")
t = tuple(
    n
    for n in range(1, int(12345 ** .5) + 1)
    if (n ** 2) % 3 == 0 and (n ** 2) % 4 == 0 and (n ** 2) % 8 != 0
)
print(t)


# task 2
print("task2")
def rotate(mat, dir):
    row = len(mat)
    col = len(mat[0])

    if dir == "left":
        return [[mat[i][j] for i in range(row)] for j in reversed(range(col))]
    else:
        return [[mat[i][j] for i in reversed(range(row))] for j in range(col)]

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "left"))
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "right"))

# task 3
print("task3")
def occurrences(s):
    return {c : s.count(c) for c in s}
print(occurrences("hello, world!"))

# task 4
print("task4")
import datetime

class Book:
    def __init__(self, title, author, year, isbn, amount):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.amount = amount

    def borrow_book(self):
        if self.amount > 0:
            self.amount -= 1
            return True
        else:
            return False

    def return_book(self):
        self.amount += 1
        return True
    
    def get_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "ISBN": self.isbn,
            "amount": amount,
        }

    def short_info(self):
        return f"{self.title!r} by {self.author!r}"

    def display_info(self):
        return f"Book {self.title!r} by {self.author!r}, {self.year}, {self.isbn} x{self.amount}"

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.books = []
    
    def short_info(self):
        return f"{self.name} (#{self.id})"

    def borrow_book(self, book):
        if book in self.books:
            return False
        elif book.borrow_book():
            self.books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.return_book()
            return True
        else:
            return False

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.history = []

    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        else:
            return False
    
    def add_user(self, name):
        new_user = User(name, len(self.users) + 1)
        self.users.append(new_user)
        return new_user
    
    def borrow_book(self, user, book):
        ok = user.borrow_book(book)
        self.history.append((user, datetime.date.today(), book, "borrowed" if ok else "tried to borrow"))
        return ok

    def return_book(self, user, book):
        ok = user.return_book(book)
        self.history.append((user, datetime.date.today(), book, "returned" if ok else "tried to return"))
        return ok

    def search_user(self, name):
        return [user for user in self.users if name in user.name]

    def search_book(self, name):
        return [book for book in self.books if name in book.name]

    def show_history(self):
        for user, date, book, action in self.history:
            print(user.short_info(), action, book.short_info(), "on", date)

lib = Library()
book1 = Book("Learning Python", "Mark Lutz", 2013, "978-1449355739", 10)
book2 = Book("Fluent Python", "Luciano Ramalho", 2022, "978-1492056355", 2)
lib.add_book(book1)
lib.add_book(book2)
user1 = lib.add_user("Vasya")
user2 = lib.add_user("Petya")
user3 = lib.add_user("Nikita")

assert lib.borrow_book(user1, book2) == True
assert lib.borrow_book(user2, book2) == True
assert lib.borrow_book(user3, book2) == False

assert lib.return_book(user2, book2) == True
assert lib.borrow_book(user3, book2) == True

lib.show_history()


# task 5
print("task5...")
# Все переменные в python являются ссылками. Поэтому код "b = a" означает,
# что теперь b является ссылкой на тот же объект, на который ссылается a. 
# И переменные a, b являются двумя способами получить доступ к одному и тому же объекту.
# Поэтому "a[0] = 4" и "print(b)" используют один и тот же объект, но разными способами.


# task 6
print("task6")
a = sum(1 / i ** 2 for i in range(1, 10001))
b = sum(1 / i ** 2 for i in reversed(range(1, 10001)))
print(a, b, a - b)
# Разница обусловлена ошибками округления при работе с числами с плавающей точкой. 
# При сложении двух чисел ошибка зависит от максимального из модулей двух чисел. 
# Поэтому нужно организоват сделать суммирование так, чтобы переменная, которая накапливает 
# сумму оставалась как можно дольше маленкой. А достичь этого можно, если складывать 
# числа в порядке возрастания их модулей. В данном конкретном случае это означает
# суммирование в обратном порядке.




