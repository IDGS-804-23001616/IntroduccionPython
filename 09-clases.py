class Operacionesbas:
    num1=0
    num2=0
    resultado=0
    
    def __init__(self):
        self.num1=0
        self.num2=0
    
    def suma(self, a):
        self.num1=a
        self.resultado = self.num1 + self.num2
        print('La suma es: {0}' .format(self.resultado))
    
    def resta(self):
        self.resultado = self.num1 - self.num2
        print('La resta es: {0}' .format(self.resultado))
        
def main():
    obj=Operacionesbas()
    obj.suma(10)
    obj.resta()
    
if __name__ == "__main__":
    main()