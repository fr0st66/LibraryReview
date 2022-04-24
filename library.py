from uuid import UUID
from customer import Customer
from book import Book
from loan import Loan

customers = {}
books = {}
loans = []


def add_book(book):
    books[book.get_name()] = book  

def add_customer(customer):
    customers[customer.get_id()] = customer   

def create_loan(customer, book):
    if not isinstance(customer, Customer):   # פונקציה שבודקת אם האובייקט הוא אובייקט של קלאס לקוח
        raise TypeError('Invalid customer object')

    if not isinstance(book, Book):     # פונקציה שבודקת אם האובייקט הוא אובייקט של קלאס ספר
        raise TypeError('Invalid book object')

    # בדיקה שיש מספיק עותקים בשביל להשאיל
    if book.get_copies() < 1:
        return f'There are no available copies of this book - {book.get_name}'

    # Find all customer loans
    customer_loans = []
    for loan in loans:
        if loan.get_customer() == customer:
            customer_loans.append(loan)

    # תנאי - שהלקוח לא לקח את הכמות שיש בתקרה
    if len(customer_loans) > 2:
        return f'Customer reached max amount of loans:{len(customer_loans)}'

    # בדיקה שאין ספרים שבאיחור
    for loan in customer_loans:
        if loan.is_overdue():
            # You have to make sure that 2 weeks passes between when a book is returned late
            # and when a customer is allowed to take another book. -3
            return f'No new loans until overdue book is returned: {loan.get_book().get_name()}'
 
    loan = Loan(customer, book) # ואם כל התנאים מתבצעים- יצירת מופע חדש של  קלאס השאלה
    loans.append(loan)

    return loan


def close_loan(customer, book):
    loans = get_all_loans()

    for loan in loans:
        if loan.get_customer() == customer and loan.get_book() == book:
            loans.remove(loan)
            book.add_copy()
            return


def get_all_books():
    return list(books.values())


def show_all_books():
    books = get_all_books()

    if not books:
        print('No books')
        return

    for book in books:
        print(book)


def get_all_customers():
    return list(customers.values())


def show_all_customers():
    customers = get_all_customers()

    if not customers:
        print('No customers')
        return

    for customer in customers:
        print(customer)


def get_all_loans():
    return loans


def show_all_loans():
    loans = get_all_loans()

    if len(loans) == 0:
        print('No loans')
        return

    for loan in loans:
        print(loan)


def get_late_loans():
    loans = []

    for loan in get_all_loans():
        if loan.is_overdue():
            loans.append(loan)
    return loans


def show_late_loans():
    for loan in get_late_loans():
        print(loan)


def get_loans_by_customer(customer):
    loans = []
    for loan in get_all_loans():
        if loan.get_customer() == customer:
            loans.append(loan)
    return loans


def show_loans_by_customer(customer):
    for loan in get_loans_by_customer(customer):
       print (loan)


def get_loans_by_book(book):
    loans = []

    for loan in get_all_loans():
        if loan.get_book() == book:
            loans.append(loan)
    return loans


def show_loans_by_book(book):
    for loan in get_loans_by_book(book):
        print(loan)


def find_customer_by_id(customer_id):
    # You have to check that this is a valid id_string and that the customer is actually in the library.
    return customers[UUID(str(customer_id))] # מספר לקוח יחודי 


def find_book_by_name(book_name):
    # You have to check that the book is in the library.
    return books[book_name]


def remove_book(book):
    for loan in get_all_loans():
        if loan.get_book() == book:
            # You should print something here letting them know they didn't remove successfully.
            return
    books.pop(book.get_name())


def remove_customer(customer):
    for loan in get_all_loans():
        if loan.get_customer() == customer:
            # You should print something here letting them know they didn't remove successfully.
            return
    customers.pop(customer.get_id())

