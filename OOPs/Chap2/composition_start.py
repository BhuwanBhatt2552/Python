# Demonstrating Object-Oriented Composition in Python.
# Composition models a "has-a" relationship, where complex objects are built
# using instances of other classes (e.g., a Book HAS an Author and HAS Chapters).


class Book:
    """Represents a book composed of an Author object and multiple Chapter objects."""

    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author  # Composition: Book holds an Author instance
        self.chapters = []    # Composition: Book holds a collection of Chapter instances

    def addchapter(self, chapter):
        """Appends a Chapter instance to the internal chapters list."""
        self.chapters.append(chapter)

    def getbookpagecount(self):
        """Calculates total pages by iterating through each composed Chapter object."""
        result = 0
        for ch in self.chapters:
            result += ch.pagecount  # Accesses pagecount attribute of Chapter
        return result     

class Author:
    """Represents an author with a first and last name."""

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        # Defines the user-friendly string representation when printed
        return f"{self.fname} {self.lname}"

class Chapter:
    """Represents an individual book chapter with a title and page count."""

    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


# --- Usage Example ---

# 1. Instantiate an Author object
auth = Author("Leo", "Tolstoy")

# 2. Instantiate a Book object, embedding the Author instance (Composition)
b1 = Book("War and Peace", 39.95, auth)

# 3. Instantiate and attach Chapter objects to the Book (Composition)
b1.addchapter(Chapter("Chapter 1", 104))
b1.addchapter(Chapter("Chapter 2", 89))
b1.addchapter(Chapter("Chapter 3", 124))

# 4. Display results
print(b1.title)              # Output: War and Peace
print(b1.author)             # Output: Leo Tolstoy (triggers Author.__str__)
print(b1.getbookpagecount())  # Output: 317 (sum of chapter pages)