"""
Programa hello
Descrição: imprima na tela a frase ”Hello, World!”.
Autor: Nelson S. dos Santos
Data: 25/02/2025
Versão: 0.0.3
Novidades da versão:

25/02/2025
Nesta versão:
Nesta versão, o usuário poderá entrar com seu nome para ser cumprimentado pelo programa.
"""

# Alocação de memória

nome_usuario = ""
frase = "Hello, "

# Entrada de dados

nome_usuario = input("\nQual o seu nome: ")

# Processamento de dados

frase = frase + nome_usuario

# Saída de dados

print(frase)