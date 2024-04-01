from book import Book
from library import Library
from user import Customer, Employee


def main() -> None:
    """
    Main function to demonstrate the usage of the Library system.
    """
    first_lib = Library()
    first_book = Book("Noel Papa", "Santa Claus", "ISBN 0-061-96436-1", 100)
    second_book = Book("Noel Papa2", "Santa Claus2", "ISBN 0-061-96436-2", 10)
    admin = Employee("Dave", "Administrator", 500)
    first_lib.hire_employee(admin)
    admin.add_book(first_book, 50)
    admin.add_book(second_book, 5)
    first_lib.show_books()
    first_customer = Customer("Adam")
    second_customer = Customer("Adam2")
    admin.library.register_user(first_customer)
    first_customer.take_book(second_book)
    print(second_book.copies_available)
    second_book.increase_total_copies(6)
    print(second_book.total_copies_available)
    first_lib.show_customers()
    first_lib.show_employees()
    second_lib = Library()
    manager = Employee("Kevin", "Manager", 1500)
    second_lib.hire_employee(manager)
    second_lib.register_user(second_customer)
    manager.add_book(second_book, 3)
    print(second_book.total_copies_available)

    first_lib.show_books()
    print(second_book.copies)
    print()
    second_book.decrease_total_copies(5)
    second_lib.show_books()
    print(second_book.copies_available)
    print(second_book.check_availability(second_lib))
    print(second_book.check_availability(first_lib))
    print(second_book.total_copies_available)
    manager.remove_book(second_book)
    print(second_book.check_availability(first_lib))
    print(second_book.total_copies_available)


if __name__ == "__main__":
    main()
