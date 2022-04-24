import uuid
from datetime import datetime
from datetime import timedelta


class Loan:
    def __init__(self, customer, book):
        self.id = uuid.uuid4()
        self.customer = customer
        self.book = book.get_copy()
        self.loan_date = datetime.now()
        self.return_date = \
            self.loan_date + timedelta(days=book.get_loan_days())

    def __str__(self):
        return f'Loan:{self.customer}{self.book} Loan date:{self.loan_date} Due date:{self.return_date}'

    def get_customer(self):
        return self.customer

    def get_book(self):
        return self.book

    def is_overdue(self): 
        return datetime.now().timestamp() - self.return_date.timestamp() > 0
         #  יום השאלה (פלוס +) ימי טייפ בוק (מינוס -)יום חזרה

    def __eq__(self, other):
        return self.id == other.id
     