import library
from library import customers
from library import books
from library import loans
from customer import Customer
from book import Book
import pickle

if __name__ == '__main__':

    with open('data_loans.pickle', 'rb') as read_file1:
              library.loans= pickle.load(read_file1)
    with open('data_books.pickle', 'rb') as read_file2:
            library.books= pickle.load(read_file2)
    with open('data_costumer.pickle', 'rb') as read_file3:
            library.customers= pickle.load(read_file3)
   
    while True:

        print('''
        **** Hello Librarian, Please enter your choice ****
        1.  Add a new customer
        2.  Add a new book
        3.  Loan a book
        4.  Return a book
        5.  Display all books
        6.  Display all customers
        7.  Display all loans
        8.  Display late loans
        9.  Display loans by customer
        10. Display loans by book
        11. Display book details
        12. Display customer details
        13. Remove book
        14. Remove customer
        15. Exit the program
        ''')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Please enter a valid number')
            continue

        if choice < 1 or choice > 15:
            print('Please enter a valid number between 1 and 15')
            continue

        if choice == 1:
            name = input('Enter customer name - ')
            city = input('Enter a customer city of residence - ')
            age = int(input('Enter customers age - '))
            customer = Customer(name, city, age)
            library.add_customer(customer)
            print(customer)
            continue

        elif choice == 2:
            name = input('Enter book name - ')
            # You need to check that the book is not already in the library or you will erase the
            # previous data -1
            author = input('Enter author name - ')
            publish_year = input('Enter publish year - ')
            book_type = int(input('Enter type (1/2/3) - '))
            # You need to check that the type of book is valid 1/2/3 and not another number. -1
            copies = int(input('Enter a number of copies - '))
            book = Book(name, author, publish_year, book_type, copies)
            library.add_book(book)
            print(book)
            continue

        elif choice == 3:
            customer_id = input('Enter customer id - ')
            book_name = input('Enter book name - ')
            customer = library.find_customer_by_id(customer_id)
            # You have to check that this is a valid id_string and that the customer is actually in the library,
            # before you continue the code. -1
            book = library.find_book_by_name(book_name)
            # You have to check that the book is actually in the library before you continue the code. -1
            loan = library.create_loan(customer, book)
            print(loan)
            continue

        elif choice == 4:
            customer_id = input('Enter a customer id - ')
            book_name = input('Enter book name - ')
            customer = library.find_customer_by_id(customer_id)
            book = library.find_book_by_name(book_name)
            # You have to check that this is a valid id_string and that the customer is actually in the library,
            # before you continue the code. -1
            # You have to check that the book is actually in the library before you continue the code. -1
            # If you don't do these, the code will crash if you put in a wrong value.
            library.close_loan(customer, book)
            continue

        elif choice == 5:
            library.show_all_books()
            continue

        elif choice == 6:
            library.show_all_customers()
            continue

        elif choice == 7:
            library.show_all_loans()
            continue

        elif choice == 8:
            library.show_late_loans()
            continue

        elif choice == 9:
            customer_id = input('Enter customer id - ')
            # You have to check that this is a valid id_string and that the customer is actually in the library,
            # before you continue the code. -1
            customer = library.find_customer_by_id(customer_id)
            library.show_loans_by_customer(customer)
            continue

        elif choice == 10:
            book_name = input('Enter book name - ')
            # You have to check that the book is actually in the library before you continue the code. -1
            book = library.find_book_by_name(book_name)
            library.show_loans_by_book(book)
            continue

        elif choice == 11:
            book_name = input('Enter book name - ')
            # You have to check that the book is actually in the library before you continue the code. -1
            book = library.find_book_by_name(book_name)
            print(book)
            continue

        elif choice == 12:
            customer_id = input('Enter customer id - ')
            # You have to check that this is a valid id_string and that the customer is actually in the library,
            # before you continue the code. -1
            customer = library.find_customer_by_id(customer_id)
            print(customer)
            continue

        elif choice == 13:
            book_name = input('Enter book name - ')
            # You have to check that the book is actually in the library before you continue the code. -1
            book = library.find_book_by_name(book_name)
            library.remove_book(book)
            continue

        elif choice == 14:
            customer_id = input('Enter customer id - ')
            # You have to check that this is a valid id_string and that the customer is actually in the library,
            # before you continue the code. -1
            customer = library.find_customer_by_id(customer_id)
            library.remove_customer(customer)
            continue

        elif choice == 15:
            print ('Thank you for using our library system')

            with open('data_loans.pickle', 'wb') as write_file1:
                 pickle.dump(loans, write_file1)
            with open('data_books.pickle', 'wb') as write_file2:
                 pickle.dump(books, write_file2)
            with open('data_costumer.pickle', 'wb') as write_file3:
                pickle.dump(customers, write_file3)
            # The variables customers, books and loans are in the library module.
            # When you access them here, they're empty. That is the problem with using global variable
            # from another module. You get a copy when they're imported (and empty) and then that's what you
            # have access to. If you had written this code in the library module it would have worked. -3
            break  
              
        else:
            print("Please enter a choice between 1-15 only!")    


# book1=Book('Da Vinci Code','Brown Dan',1990,13)
# book2=Book('Harry Potter','Rowling J.K.',2010,8) 
# book3=Book('Fifty Shades of Grey','James E.L.',2001,3)   
# book4=Book('Angels and Demons','Brown Dan',1995,15) 
# book5=Book('Twilight','Meyer Stephenie',1999, 21) 
 
# person1=Customer ('Nancy', 'Bangkok',41)
# person2=Customer ('Emily', 'NYC', 9)
# person3=Customer ('Michelle', 'Tokyo', 6)
# person4=Customer ('Aline','Toronto', 3)
# person5=Customer ('Daniel', 'Paris', 41)

