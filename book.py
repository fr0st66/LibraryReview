from datetime import datetime

book_type_to_loan_days = (2, 5, 10)

class Book:
    def __init__(self, name, author, publish_year, book_type, copies):
        self.name = name
        self.author = author
        self.publish_year = publish_year
        self.loan_days = book_type_to_loan_days[book_type - 1] # This is nice! I'd put it in a class variable though.
        self.existing_copies = copies
        self.remaining_copies = copies

    def __str__(self):
        return f'Book name:{self.name}, author:{self.author}, publish_year:{self.publish_year}, loan_days:{self.loan_days}, copies:{self.remaining_copies}'
           
    def get_name(self):
        return self.name

    def get_loan_days(self):
        return self.loan_days

    def get_copies(self): 
        return self.remaining_copies

    def get_copy(self): #כמות העותקים - השאלת ספר
        if self.remaining_copies > 0:
            self.remaining_copies -= 1
            return self

    def add_copy(self): # כמות העותקים - החזרת ספר
        if self.remaining_copies < self.existing_copies:
            self.remaining_copies += 1

    def __eq__(self, other):
        return self.name == other.name  