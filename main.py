"""
Indentacao e usada para delimitar blocos de codigos, enquanto outras linguagens utilizam chaves/palavras chaves, o python utiliza espacos
para determinar o escopo das declaracoes, exemplo:"""

if 10 > 5:
    print('e sim')
    if 'hello' == 'hello':
        print('obvio')

# se nao houvesse esse espaco entre as linhas o codigo nao iria funcionar.

"""As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas.
Para declarar e atribuir um valor a uma variável em Python, utilizamos o operador de atribuição =. O nome da variável vai à esquerda do operador,
e o valor que você deseja atribuir vai à direita. Por exemplo:"""

nome = 'Juan'
idade = 18
altura = 1.75
e_estudante = True

"""Aqui temos 4 tipos de dados, String, Int, Float e Booleano
String= Sequencias de caracteres encerradas entre aspas
Int= Numeros inteiros
Float = Numeros com casas decimais
Booleano = Sim ou Nao, True or false, basicamente isso"""

#Você também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:
a=b=c=('zaza')
if a == b:
    print(c)

    """Pontos importantes ao declarar variaveis:
    -Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados (_). Não podem começar com um número.
    -O Python diferencia maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.
    -Não se pode usar palavras-chave reservadas do Python como nomes de variáveis (por exemplo, if, else, for, while, etc.).
    -Recomenda-se usar nomes descritivos para as variáveis, que indiquem claramente seu propósito: nome, idade, total_vendas, etc.

    alguns exemplos de nomes de variáveis inválidos são:
    
    1idade , Comeca com numero
    nome-completo , Usa um hífen em vez de um sublinhado
    if , Palavra-chave reservada do Python
"""


