class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    def __str__(self):
        return f"Nome: {self._first_name} - Sobrenome:  {self._last_name}"