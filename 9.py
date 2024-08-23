# Função para calcular o novo salário
def calcular_novo_salario(salario_atual, percentual_reajuste):
    aumento = salario_atual * (percentual_reajuste / 100)
    novo_salario = salario_atual + aumento
    return novo_salario

# Entrada de dados
salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

# Cálculo do novo salário
novo_salario = calcular_novo_salario(salario_atual, percentual_reajuste)

# Exibição do resultado
print(f"\nO novo salário do funcionário será: R${novo_salario:.2f}")
