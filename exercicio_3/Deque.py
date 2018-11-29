from No import No


class Deque:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicial = None
        self.final  = None
        self.quantidade = 0

    @property
    def full(self):
        if self.quantidade <= self.tamanho:
            return False
        else:
            return True

    @property
    def empty(self):
        if self.quantidade == 0:
            return True
        else:
            return False

    def peek_front(self):
        return self.inicial

    def peek_back(self):
        return self.final

    def push_front(self, valor):
        if self.full is False:
            if self.inicial is None and self.final is None:
                self.inicial = self.final = No(valor)
            else:
                no = No(valor)
                no.proximo = self.inicial
                self.inicial = no

                proximo = self.inicial.proximo
                proximo.anterior = no
            self.quantidade += 1

    def push_back(self, valor):
        if self.full is False:
            if self.inicial is None and self.final is None:
                self.inicial = self.final = No(valor)
            else:
                self.final.proximo = no = No(valor)
                no.anterior = self.final
                self.final = self.final.proximo
            self.quantidade += 1

    def __str__(self):
        iterador = self.inicial
        texto = "#"*50+"\n"
        while iterador is not None:
            texto += str(iterador)+"\n"
            iterador = iterador.proximo
        texto += "#"*50+"\n"
        return texto









