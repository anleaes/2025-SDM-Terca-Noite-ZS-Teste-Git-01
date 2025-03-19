class Category:
    def __init__(self, name, description):
        self._name = name
        self._description = description

        def __str__(self):
            return f"Nome: {self._name} - Descrição:  {self._description}"