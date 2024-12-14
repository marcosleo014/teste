def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        fat = 1
        while n>1:
            fat *= n
            n-=1
        return fat
        return n*fatorial(n)
    
def impressão(self):
    print(f'palavra: {self.palavra}')
    print(f'quantidade de letras: {self.letras}')
    print(f'quantidade de anagramas: {self.anagramas}')