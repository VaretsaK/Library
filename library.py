from book import Book


class Library:
    """
    Represents a library which can contain books and manage users and employees.

    Class Attributes:
        LIBRARY_NET_NAME (str): The default name for the library network.
        __lib_number (int): A class-level attribute tracking the number of libraries.

    Attributes:
        name (str): The name of the library, automatically assigned.
        books (list): A list of books available in the library.
        customers (list): A list of registered customers of the library.
        employees (list): A list of employees working at the library.
        lib_id (int): A unique identifier for the library, automatically assigned.

    Methods:
        register_user(user): Registers a new user in the library.
        hire_employee(employee): Adds an employee to the library staff.
        find_book(isbn): Finds and returns a book by its ISBN if it exists in the library.
        show_books(): Displays all books available in the library.
        show_customers(): Displays all registered customers of the library.
        show_employees(): Displays all employees of the library.
        change_lib_name(new_name): Changes the default name of the library network (class method).
    """

    LIBRARY_NET_NAME = "Best Library"
    __lib_number = 0

    def __init__(self) -> None:
        """Initializes a new library instance with a unique name and ID."""

        Library.__lib_number += 1

        self.name = f"{Library.LIBRARY_NET_NAME}. №{Library.__lib_number}"
        self.books = []
        self.customers = []
        self.employees = []
        self.lib_id = Library.__lib_number

    def register_user(self, user):
        """Registers a new user in the library."""

        user.set_lib(self)
        self.customers.append(user)

    def hire_employee(self, employee):
        """Adds an employee to the library's staff and sets the library as their place of work."""

        employee.set_lib(self)
        self.employees.append(employee)

    def find_book(self, isbn: int):
        """Finds a book by its ISBN in the library's collection, if it exists and the ISBN format is valid."""

        if Book.validate_isbn(isbn):

            for book in self.books:
                if book.isbn == isbn:
                    return book

    def show_books(self):
        """Displays all the books available in the library."""

        for book in self.books:
            print(book)

    def show_customers(self):
        """Displays all registered customers of the library."""

        for customer in self.customers:
            print(customer)

    def show_employees(self):
        """Displays all employees of the library."""

        for employee in self.employees:
            print(employee)

    @classmethod
    def change_lib_name(cls, new_name: str):
        """Changes the default name of the library network to a specified new name."""

        cls.LIBRARY_NET_NAME = new_name
