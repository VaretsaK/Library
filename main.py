from book import Book
from library import Library
from user import Customer, Employee


def main() -> None:
    """
    Main function to demonstrate the usage of the Library system.
    """
    first_lib = Library()
    second_lib = Library()

    first_book = Book("Noel Papa", "Santa Claus", "ISBN 0-061-96436-1", 100)
    second_book = Book("Noel Papa2", "Santa Claus2", "ISBN 0-061-96436-2", 10)

    admin = Employee("Dave", "Administrator", 500)
    manager = Employee("Kevin", "Manager", 1500)

    first_customer = Customer("Adam")
    second_customer = Customer("Adam2")

    first_lib.hire_employee(admin)
    second_lib.hire_employee(manager)

    admin.add_book(first_book, 50)
    admin.add_book(second_book, 5)
    manager.add_book(second_book, 3)

    admin.library.register_user(first_customer)
    manager.library.register_user(second_customer)

    first_customer.take_book(second_book)


if __name__ == "__main__":
    main()
