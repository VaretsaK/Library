from book import Book


class Library:
    """
    Represents a library system capable of managing books, users (customers and employees), and library details.

    Attributes:
        _name (str): The name of the library, uniquely assigned based on the library network name and an incrementing
        number.
        _books (list): A collection of Book objects available in the library.
        _customers (list): A list of Customer objects representing registered library users.
        _employees (list): A list of Employee objects representing library staff.
        _lib_id (int): A unique identifier for the library instance, based on an incrementing class-level counter.

    Class Attributes:
        LIBRARY_NET_NAME (str): The default name prefix for the library network.
        __lib_number (int): A counter tracking the total number of Library instances created.

    Methods:
        register_user(user): Registers a user with the library.
        hire_employee(employee): Adds an employee to the library's staff.
        find_book(isbn): Searches for a book by its ISBN.
        show_books(): Prints all books available in the library.
        show_customers(): Prints all registered customers of the library.
        show_employees(): Prints all employees of the library.
        change_lib_name(new_name): Updates the default library network name.
    """

    LIBRARY_NET_NAME = "Best Library"
    __lib_number = 0

    def __init__(self) -> None:
        """
        Initializes a new Library instance with a unique name and identifier.
        Automatically assigns a unique name based on the library network name and increments the library ID.
        """

        Library.__lib_number += 1

        self._name = f"{Library.LIBRARY_NET_NAME}. №{Library.__lib_number}"
        self._books = []
        self._customers = []
        self._employees = []
        self._lib_id = Library.__lib_number

    def __repr__(self) -> str:
        """Returns a string representation of the library instance."""
        return f"Library('{self._name}', '{self._lib_id}')"

    def get_books(self) -> list:
        """
        Returns a list of books available in the library.

        Returns:
            list: The list of Book objects in the library.
        """
        return self._books

    def register_user(self, user) -> None:
        """
        Registers a new user with the library, adding them to the list of customers.

        Args:
            user (User): The user to be registered with the library.
        """

        user.library = self
        self._customers.append(user)

    def hire_employee(self, employee) -> None:
        """
        Adds a new employee to the library's staff, setting the library as their place of work.

        Args:
            employee (Employee): The employee to be added to the library staff.
        """
        employee.library = self
        self._employees.append(employee)

    def find_book(self, isbn: str) -> None | Book:
        """
        Searches for and returns a book by its ISBN if it exists in the library's collection.

        Args:
            isbn (int): The ISBN of the book to find.

        Returns:
            Book or None: The Book object if found; otherwise, None.
        """
        if Book.validate_isbn(isbn):

            for book in self._books:
                if book.get_isbn() == isbn:
                    return book

    def show_books(self) -> None:
        """Prints details of all books available in the library."""

        for book in self._books:
            print(book)

    def show_customers(self) -> None:
        """Prints details of all registered customers of the library."""

        for customer in self._customers:
            print(customer)

    def show_employees(self) -> None:
        """Prints details of all employees of the library."""

        for employee in self._employees:
            print(employee)

    @classmethod
    def change_lib_name(cls, new_name: str) -> None:
        """
        Updates the default name of the library network to a new specified name.

        Args:
            new_name (str): The new default name for the library network.
        """

        cls.LIBRARY_NET_NAME = new_name
