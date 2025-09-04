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