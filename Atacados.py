# Identificador
ru = input('RU da aluna: ')
if ru == '3553052':
    print('Bem vindo(a) a empresa de atacados elaborada pela Karina Miatelli Calaça Vieira')
else:
    ru = input('RU da aluna: ')
    print('Bem vindo(a) a empresa de atacados elaborada pela Karina Miatelli Calaça Vieira')

# Início do código
produto = float(input('Entre com o valor do produto: '))
qtd = int(input('Qual a quantidade desse produto? '))

total = produto * qtd  # Variável para receber os dados digitados pelo usuário e já calcular o valor da compra

if 10 <= qtd <= 99:
    descont = 0.05  # Variável do desconto atribuído
    print('O valor da compra sem desconto é de {:.2f} reais.'.format(total))
    print('O valor da compra com desconto é de {:.2f} reais.'.format(total - (total * descont)))
elif qtd >= 1000:
    descont = 0.15  # Variável do desconto atribuído
    print('O valor da compra sem desconto é de {:.2f} reais.'.format(total))
    print('O valor da compra com desconto é de {:.2f} reais.'.format(total - (total * descont)))
else:
    if qtd <= 9:
        print('O valor da compra é de {:.2f} reais'.format(total))

