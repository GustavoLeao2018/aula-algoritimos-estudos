class No:
    def __init__(self, valor):
        self._dado = valor
        self.proximo = None

    @property
    def dado(self):
        return self._dado

    def __str__(self):
        if self.proximo is None:
            return f"|\t Nó: {self.dado} \t|\t Próximo: {self.proximo} \t|"
        else:
            return f"|\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado} \t|"