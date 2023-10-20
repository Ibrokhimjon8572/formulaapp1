class Driver:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self) -> str:
        return self.name