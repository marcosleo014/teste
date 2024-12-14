class Linha:
    def __init__(self,quantidades = 1):
        self.quantidades = quantidades
    def impressão(self):
        print("*"*self.quantidades)