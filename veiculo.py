class Veiculo:
   def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano

   def ligar(self):
     print("Veículo ligado")

   def desligar(self):
    print("Veículo desligado")
   

class Carro(Veiculo):
   def __init__(self, marca, modelo, ano, numeroDePortas):
       super().__init__(marca, modelo, ano)
       self.numeroDePortas = numeroDePortas

   def NumeroDePortas(self):
     print("O Carro possui: ", self.numeroDePortas)

class Moto(Veiculo):
   def __init__(self, marca, modelo, ano, cilindradas):
      super().__init__(marca, modelo, ano)

      self.cilindradas = cilindradas

   def Cilindradas (self):
       print("A Moto possui: ", self.cilindradas)

Veiculo1   = Veiculo("Toyota", "Corolla", 2020)
Carro1     = Carro("Honda", "Civic", 2022, 4)
Moto1      = Moto("Honda", "Titan", 2018, 160)
Carro1.ligar()
Carro1.desligar()
Moto1.ligar()
Moto1.desligar(