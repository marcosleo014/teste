from funcoes import *
class Anagrama:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras = len(self.palavra)
        self.anagramas = fatorial(self.letras)