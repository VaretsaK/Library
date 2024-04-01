import re


class Book:
    """
    Represents a book within a library system, tracking its copies across different library instances.

    Attributes:
        _title (str): The title of the book.
        _author (str): The author's name.
        _isbn (str): The International Standard Book Number identifying the book.
        _total_copies (int): Total number of copies of the book across all libraries.
        _copies (dict): Maps Library instances to the number of copies of this book in each.
        _copies_available (dict): Maps Library instances to the number of available copies in each.
        _copies_added (bool): Indicates whether copies of this book have been added to any library.
        _total_copies_available (int): The total number of copies available for borrowing across all libraries.

    Methods:
        check_availability(library): Checks the availability of this book in a specified library.
        increase_copies(library, value): Adds more copies to a specified library.
        decrease_copies(library, value): Removes copies from a specified library.
        increase_total_copies(value): Increases the total number of copies of this book.
        decrease_total_copies(value): Decreases the total number of copies of this book.
        validate_isbn(isbn): Validates the book's ISBN.
    """
    def __init__(self, title: str, author: str, isbn: str, total_copies: int) -> None:
        """
        Initializes a new instance of Book.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN of the book.
            total_copies (int): Initial total number of copies available across all libraries.
        """

        self._title = title
        self._author = author
        self._isbn = isbn
        self._copies = {}
        self._copies_available = {}
        self._copies_added = False
        self._total_copies = total_copies
        self._total_copies_available = total_copies

    def __repr__(self) -> str:
        """
        Provides a string representation of the Book instance.

        Returns:
            str: A string that represents the Book object.
        """
        return f"Book('{self._title}', '{self._author}', '{self._isbn}')"

    def get_isbn(self) -> str:
        """
        Returns the ISBN of the book.

        Returns:
            str: The ISBN of the book.
        """
        return self._isbn

    def get_copies(self) -> dict:
        """
        Retrieves the dictionary mapping libraries to their respective copies of this book.

        Returns:
            dict: A mapping of Library instances to the number of copies in each.
        """
        return self._copies

    def get_copies_available(self) -> dict:
        """
        Retrieves the dictionary mapping libraries to their available copies of this book.

        Returns:
            dict: A mapping of Library instances to the number of available copies in each.
        """
        return self._copies_available

    @property
    def total_copies_available(self) -> int:
        """
        Property to get the total number of available copies across all libraries.

        Returns:
            int: The total number of copies available.
        """
        return self._total_copies_available

    @total_copies_available.setter
    def total_copies_available(self, value: int) -> None:
        """
        Sets the total number of copies available across all libraries.

        Args:
            value (int): The total number of available copies to set.
        """
        self._total_copies_available = value

    def check_availability(self, library) -> str:
        """
        Checks and returns the availability of this book in a specified library.

        Args:
            library (Library): The library to check the book's availability in.

        Returns:
            str: A message indicating the number of available copies in the specified library.
        """

        for book in library.get_books():
            if self._isbn == book.get_isbn():
                return f"There are {book.get_copies_available()[library]} copies available."
        return f"There is no such book in this _library."

    def increase_copies(self, library, value: int) -> None:
        """
        Increases the number of copies of this book in a specified library.

        Args:
            library (Library): The library where copies will be added.
            value (int): The number of copies to add.
        """

        if self._copies_added and value <= self._total_copies_available:
            self._total_copies_available -= value
            self._copies[library] += value
            self._copies_available[library] += value

    def decrease_copies(self, library, value: int) -> None:
        """
        Decreases the number of copies of this book in a specified library.

        Args:
            library (Library): The library from which copies will be removed.
            value (int): The number of copies to remove.
        """

        if self._copies_added and value <= sum(self._copies_available[library]):
            self._total_copies_available += value
            self._copies_available[library] -= value
            self._copies[library] -= value

    def increase_total_copies(self, value: int) -> None:
        """
        Increases the total number of copies of this book across all libraries.

        Args:
            value (int): The number of total copies to increase by.
        """

        self._total_copies += value
        self._total_copies_available += value

    def decrease_total_copies(self, value: int) -> None:
        """
        Decreases the total number of copies of this book across all libraries.

        Args:
            value (int): The number of total copies to decrease by.
        """

        if value <= self._total_copies_available:
            self._total_copies -= value
            self._total_copies_available -= value

    @staticmethod
    def validate_isbn(isbn: str) -> re.Match[str] | None:
        """
        Validates the format of the book's ISBN.

        Args:
            isbn (str): The ISBN to validate.

        Returns:
            Match object or None: The search result if the ISBN is valid, None otherwise.
        """

        if len(isbn) == 18:
            result = re.search(r"ISBN \d-\d\d\d-\d\d\d\d\d-\d", isbn)
            return result
