class User:
    """
    Represents a generic user of the library system, serving as a base class for Customer and Employee.

    Attributes:
        name (str): The name of the user.
        user_id (int): A unique identifier for the user, automatically assigned.

    Class Attributes:
        __user_count (int): A class-level attribute tracking the total number of users.

    Methods:
        No public methods defined in this base class.
    """

    __user_count = 0  # using this value to set user_id variable

    def __init__(self, name: str) -> None:
        """Initializes a new user instance and assigns a unique user ID."""

        User.__user_count += 1

        self.name = name
        self.user_id = User.__user_count
        self.library = None

    def set_lib(self, lib):
        """Sets the library instance for the user, used internally when registering the user with a library."""

        self.library = lib


class Customer(User):
    """
    Represents a customer who can borrow books from the library, inheriting from User.

    Attributes:
        borrowed_books (list): A list of books the customer has borrowed.
        __library (Library): The library from which the customer borrows books, kept private.

    Methods:
        take_book(book): Borrows a book from the library, adding it to borrowed_books.
        return_book(book): Returns a borrowed book to the library, removing it from borrowed_books.
        _set_lib(lib): Sets the library instance for the customer, intended for internal use.
    """
    def __init__(self, name) -> None:
        """Initializes a new customer instance with an empty list of borrowed books."""

        super().__init__(name)
        self._borrowed_books = []

    def __repr__(self):
        return f"Customer('{self.name}')"

    def take_book(self, book):
        """Adds a book to the customer's borrowed books and decreases its availability in the library."""

        self._borrowed_books.append(book)
        book_inx = self.library.books.index(book)
        self.library.books[book_inx].copies_available[self.library] -= 1

    def return_book(self, book):
        """Removes a book from the customer's borrowed books and increases its availability in the library."""

        self._borrowed_books.remove(book)
        book_inx = self.library.books.index(book)
        self.library.books[book_inx].copies_available[self.library] += 1


class Employee(User):
    """
    Represents an employee of the library, inheriting from User.

    Attributes:
        library (Library): The library where the employee works.
        salary (int): The salary of the employee.
        position (str): The position of the employee within the library.

    Methods:
        add_book(book, book_copies): Adds a specified number of copies of a book to the library.
        remove_book(book): Removes a book from the library's collection.
    """
    def __init__(self, name, position: str, salary: int) -> None:
        """Initializes a new employee with a name, position, and salary."""

        super().__init__(name)
        self._salary = salary
        self._position = position

    def __repr__(self):
        return f"Employee('{self.name}', '{self._position}', '{self._salary}')"

    def add_book(self, book, book_copies: int):
        """Adds copies of a book to the library if the specified number does not exceed available copies."""

        if book_copies <= book.total_copies_available:
            book.total_copies_available -= book_copies
            book.copies[self.library] = book_copies
            book.copies_available[self.library] = book_copies
            book.copies_added = True
            self.library.books.append(book)
        else:
            raise ValueError("There are not enough copies.")

    def remove_book(self, book):
        """Removes a specified book from the library's collection and library's details
        from the books track of copies."""

        self.library.books.remove(book)
        book.total_copies_available += book.copies[self.library]
        book.copies_available.pop(self.library)
        book.copies.pop(self.library)
