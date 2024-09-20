# Classe base Empregado
class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


# Subclasse Gerente
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo


# Subclasse Vendedor
class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao_percentual, vendas_total):
        super().__init__(nome, salario_base)
        self.comissao_percentual = comissao_percentual
        self.vendas_total = vendas_total

    def calcular_salario(self):
        comissao = self.vendas_total * (self.comissao_percentual / 100)
        return self.salario_base + comissao


# Exemplo de uso
gerente = Gerente("João", 5000, 1000)
vendedor = Vendedor("Maria", 3000, 10, 20000)

print(f"O salário do gerente {gerente.nome} é: R${gerente.calcular_salario():.2f}")
print(f"O salário da vendedora {vendedor.nome} é: R${vendedor.calcular_salario():.2f}")
