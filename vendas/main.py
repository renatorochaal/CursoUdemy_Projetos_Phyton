
from vendas.calc_precos import aumeto, reducao
from vendas.formata import preco
preco = 49.90

preco_aumento = aumeto(valor=preco, porcentagem=15)
print(preco_aumento)

preco_reducao = reducao(valor=preco, porcentagem=15)
print(preco_reducao)