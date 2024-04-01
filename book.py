import re


class Book:
    """
    Represents a book with attributes like title, author, and ISBN, and keeps track of copies across libraries.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        total_copies (int): The total number of copies of the book.
        copies (dict): A dictionary mapping Library instances to the number of copies in each.
        copies_available (dict): A dictionary mapping Library instances to the number of available copies in each.
        copies_added (bool): A flag indicating whether copies of the book have been added to any library.
        total_copies_available (int): The total number of available copies across all libraries.

    Methods:
        check_availability(library): Returns the number of available copies in the given library.
        increase_copies(library, value): Increases the number of copies in a specific library.
        decrease_copies(library, value): Decreases the number of copies in a specific library.
        increase_total_copies(value): Increases the total number of copies of the book.
        decrease_total_copies(value): Decreases the total number of copies of the book.
        validate_isbn(isbn): Validates the ISBN of the book.
    """
    def __init__(self, title: str, author: str, isbn: str, total_copies: int) -> None:
        """Initializes a new book instance with title, author, ISBN, and total copies."""

        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = {}
        self.copies_available = {}
        self.copies_added = False
        self.total_copies = total_copies
        self.total_copies_available = total_copies

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

    def check_availability(self, library):
        """Returns the number of available copies in the specified library."""

        for book in library.books:
            if self.isbn == book.isbn:
                return f"There are {book.copies_available[library]} copies available."
        return f"There is no such book in this library."

    def increase_copies(self, library, value: int):
        """Increases the number of copies for this book in a specified library by a given value."""

        if self.copies_added and value <= self.total_copies_available:
            self.total_copies_available -= value
            self.copies[library] += value
            self.copies_available[library] += value

    def decrease_copies(self, library, value: int):
        """Decreases the number of copies for this book in a specified library by a given value."""

        if self.copies_added and value <= sum(self.copies_available[library]):
            self.total_copies_available += value
            self.copies_available[library] -= value
            self.copies[library] -= value

    def increase_total_copies(self, value: int):
        """Increases the total number of copies of this book by a given value."""

        self.total_copies += value
        self.total_copies_available += value

    def decrease_total_copies(self, value: int):
        """Decreases the total number of copies of this book by a given value if it does not exceed available copies."""

        if value <= self.total_copies_available:
            self.total_copies -= value
            self.total_copies_available -= value

    @staticmethod
    def validate_isbn(isbn):
        """Validates the given ISBN against a regular expression pattern."""

        if len(isbn) == 18:
            result = re.search(r"ISBN \d-\d\d\d-\d\d\d\d\d-\d", isbn)
            return result
