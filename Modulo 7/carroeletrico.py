class CarroEletrico(Carro):
    """
    Uma classe para representar um carro elétrico, que herda de Carro.
    """
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        # Chama o construtor da classe mãe (Carro)
        super().__init__(marca, modelo, ano)
        
        # Adiciona um novo atributo específico para carros elétricos
        self.autonomia_bateria = autonomia_bateria
        
    def exibir_info(self):
        """
        Sobrescreve o método da classe mãe para incluir a autonomia.
        """
        # Chama o método da classe mãe para exibir as informações básicas
        super().exibir_info()
        
        # Adiciona a informação específica da classe filha
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")

# --- Criando e usando objetos das duas classes ---

# Criando um carro tradicional (classe Carro)
carro_gasolina = Carro("Ford", "Focus", 2020)

# Criando um carro elétrico (classe CarroEletrico)
carro_eletrico = CarroEletrico("Tesla", "Model 3", 2023, 500)

print("--- Veículo a Gasolina ---")
carro_gasolina.exibir_info()
print("-" * 25)
