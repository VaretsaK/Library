class User:
    """
    Represents a generic user in the library system, serving as a base class for both Customers and Employees.

    This class provides a foundation with basic attributes like name and a unique user ID.
    Subclasses should implement specific behaviors like borrowing books (Customer) or managing library inventory
    (Employee).

    Attributes:
        _name (str): The name of the user.
        _user_id (int): A unique identifier for the user, automatically assigned.

    Class Attributes:
        __user_count (int): Tracks the total number of User instances created across the system.

    Methods:
        library: Property method to get or set the library instance associated with the user.
    """

    __user_count = 0  # using this value to set _user_id variable

    def __init__(self, name: str) -> None:
        """
        Initialize a new User instance.

        Args:
            name (str): The name of the user.
        """
        User.__user_count += 1

        self._name = name
        self._user_id = User.__user_count
        self._library = None

    @property
    def library(self):
        """Get the library instance associated with this user."""
        return self._library

    @library.setter
    def library(self, lib) -> None:
        """
        Set the library instance for this user. This is intended for internal use by the Library class.

        Args:
            lib: The library instance to associate with this user.
        """

        self._library = lib


class Customer(User):
    """
    Represents a customer of the library, capable of borrowing books.

    Inherits from User and adds functionality specific to library customers, such as borrowing and returning books.

    Attributes:
        _borrowed_books (list): A list of books currently borrowed by the customer.
    """
    def __init__(self, name) -> None:
        """
        Initialize a new Customer instance.

        Args:
            name (str): The name of the customer.
        """

        super().__init__(name)
        self._borrowed_books = []

    def __repr__(self) -> str:
        """
        Return a string representation of the Customer instance, including their name and borrowed books.
        """
        return f"Customer('{self._name}', '{self._borrowed_books}')"

    def take_book(self, book) -> None:
        """
        Borrow a book from the library, adding it to the list of borrowed books.

        Args:
            book: The book instance to be borrowed.
        """
        self._borrowed_books.append(book)
        book_inx = self._library.get_books().index(book)
        self._library.get_books()[book_inx].get_copies_available()[self._library] -= 1

    def return_book(self, book) -> None:
        """
        Return a borrowed book to the library, removing it from the list of borrowed books.

        Args:
            book: The book instance to be returned.
        """
        self._borrowed_books.remove(book)
        book_inx = self._library.get_books().index(book)
        self._library.get_books()[book_inx].get_copies_available()[self._library] += 1

    def get_borrowed_books(self) -> list:
        """
        Get a list of books currently borrowed by the customer.

        Returns:
            A list of borrowed book instances.
        """
        return self._borrowed_books


class Employee(User):
    """
    Represents an employee of the library, with responsibilities like managing the book inventory.

    Inherits from User and adds specific attributes and methods related to library operations.

    Attributes:
        _salary (int): The employee's salary.
        _position (str): The employee's job position within the library.
    """
    def __init__(self, name, position: str, salary: int) -> None:
        """
        Initialize a new Employee instance.

        Args:
            name (str): The name of the employee.
            position (str): The job position of the employee within the library.
            salary (int): The salary of the employee.
        """
        super().__init__(name)
        self._salary = salary
        self._position = position

    def __repr__(self) -> str:
        """
        Return a string representation of the Employee instance, including their name, position, and salary.
        """
        return f"Employee('{self._name}', '{self._position}', '{self._salary}')"

    def add_book(self, book, book_copies: int) -> None:
        """
        Add copies of a book to the library's inventory.

        Args:
            book: The book instance to be added to the library.
            book_copies (int): The number of copies of the book to add.

        Raises:
            ValueError: If the specified number of copies exceeds the book's total available copies.
        """
        if book_copies <= book.total_copies_available:
            book.total_copies_available -= book_copies
            book.get_copies()[self._library] = book_copies
            book.get_copies_available()[self._library] = book_copies
            book._copies_added = True
            self._library.get_books().append(book)
        else:
            raise ValueError("There are not enough _copies.")

    def remove_book(self, book) -> None:
        """
        Remove a book from the library's inventory.

        Args:
            book: The book instance to be removed from the library.
        """
        self._library.get_books().remove(book)
        book.total_copies_available += book.get_copies()[self._library]
        book.get_copies_available().pop(self._library)
        book.get_copies().pop(self._library)
