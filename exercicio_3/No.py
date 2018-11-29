class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        if self.proximo is None and self.anterior is None:
            return f"|\t Anterior: {self.anterior} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo} \t| "
        elif self.proximo is None:
            return f"|\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo} \t| "
        elif self.anterior is None:
            return f"|\t Anterior: {self.anterior} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado} \t| "
        else:
            return f"|\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|\t Proximo: {self.proximo.dado} \t| "
