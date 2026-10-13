# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("Hardcover", "PaperBack", "E-Book")

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if( not booktype in Book.BOOK_TYPES):
          raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype



# TODO: access the class attribute
print("Book types :", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("Title1", "Hardcover")
# b2 = Book("Title1", "Comic Book")

# TODO: Use the static method to access a singleton object
