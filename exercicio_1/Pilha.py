from No import No


class ErroNaPilha(Exception):
    pass


class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.quantidade = 0
        self.inicial = None
        self.final = None

    @property
    def top(self):
        return self.inicial

    def is_full(self):
        if self.quantidade <= self.tamanho:
            return False
        else:
            return True

    def is_empty(self):
        if self.quantidade == 0:
            return True
        else:
            return False

    def push(self, valor):
        if self.is_full() is False:
            no = No(valor)
            no.proximo = self.inicial
            self.inicial = no
            self.quantidade += 1
        else:
            raise ErroNaPilha()

    def pop(self):
        if self.is_empty() is False:
            self.inicial = self.inicial.proximo
            self.quantidade -= 1
        else:
            raise ErroNaPilha()

    def __str__(self):
        iterador = self.inicial
        texto = "#"*40+"\n"
        while iterador is not None:
            texto += str(iterador)+"\n"
            iterador = iterador.proximo
        texto += "#"*40
        return texto

    def __reversed__(self, fila):
        pass

