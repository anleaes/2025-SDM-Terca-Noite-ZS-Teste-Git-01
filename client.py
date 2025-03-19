from person import Person

class Client(Person):
    def __init__(self, first_name, last_name, adress, cell_phone, email, gender):
        super().__init__(first_name, last_name)
        self._adress = adress
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender

        def __str__(self):
             return f"Client(name={self.first_name} {self.last_name},  address:{self.address}, cell_phone:{self.cell_phone},email{self.email} , gender:{self.gender})"