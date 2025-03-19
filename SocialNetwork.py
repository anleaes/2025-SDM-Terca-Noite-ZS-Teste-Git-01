class Socialnetwork:

    def __init__(self, name, description):
        self._name = name
        self._description = description
    
    def __str__(self):
        return f"Socialnetwork(name={self._name}, description={self._description})"
    