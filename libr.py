class Library:

    def __init__(self, li, name):
        self.lib_name = name
        self.books = li
        self.dic_books = {li[i]: "None" for i in range(0, len(li))}

    def show(self):
        """This function gives the list of books in the library"""
        return f"The books in the library are: {self.books}"

    def give(self, book):
        """This function is used to return a book"""
        print(f"The {book} has been returned by {self.dic_books[book]}")
        self.dic_books[book] = "None"

    def borrow(self, book):
        """This function is used to get a book issued"""
        if self.dic_books.keys() == book:
            if self.dic_books[book] == "None":
                num = int(input("Enter the customer number"))
                self.dic_books[book] = num
            else:
                print(f"{book} is already issued by {self.dic_books[book]}")
        else:
            print("The book is not in library.")
            print("Try viewing the books available.")

    def more(self, li):
        """This function is used to add a book into the library"""
        self.books.extend(li)
        self.dic_books.update({li[i]: "None" for i in range(0, len(li))})
        print("Book added")

    def rem(self, li):
        """This function is used to remove a book from the library"""
        for i in li:
            self.books.remove(i)
            self.dic_books.pop(i)
        print("Book removed")


if __name__ == '__main__':
    print("Welcome to the Library Management System")
    name = input("Enter the name of the library you want to create")
    books = list(input("Enter the books available in the library seperated by commas.").split(", "))
    dlib = Library(books, name)
    ch = 1
    print("\n"*10)
    print(f"Welcome to the {name} Library")
    while ch == 1:
        print("\n"*2)
        print("What do you want to do?")
        opt = int(input("1. See the list of books in the library. \n2. Issue a book. \n3. Return a book. \n4. Add a book to the library. \n5. Remove a book from the library. \n\n"))
        if opt == 1:
            print(dlib.show())
            print("\n")
        elif opt == 2:
            b = input("Enter the name of the book to be issued")
            dlib.borrow(b)
            print(dlib.dic_books)
            print("\n")
        elif opt == 3:
            b = input("Enter the name of the book to be returned")
            dlib.give(b)
            print("\n")
        elif opt == 4:
            b = list(input("Enter the books to be added. (* with names separated by comma)").split(", "))
            dlib.more(b)
            print("\n")
        elif opt == 5:
            b = list(input("Enter the books to be removed. (* with names separated by comma)").split(", "))
            dlib.rem(b)
            print("\n")
        else:
            print("Wrong input. Try again. \n")

        ch = int(input("Do you want to perform any other operation? \n1. Yes"))
        if ch == 1:
            continue
        else:
            print("Thank you for using Library Management System")