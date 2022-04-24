import uuid

class Customer:
    def __init__(self, name, city, age):
        self.id = uuid.uuid4()
        self.name = name
        self.city = city
        self.age = age

    def __str__(self):
        return f'Customer id:{self.id}, name:{self.name}, city: {self.city}, age: {self.age}'
          
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id    