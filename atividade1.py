#Crie um programa que tem uma funcao leiaInt (),
#que vai funcionar de forma semelhante a função
#input () do python. Então que fazendo a validação para aceitar apenas um valor númerico.
#Ex: inteiro, real. Obs: Se o usuario nao digitar o valor,
#quero que ele atribua o valor 0 a aquela variável.

# isnumeric()método retorna:
#Verdadeiro se todos os caracteres da string forem numéricos.
#False se pelo menos um caractere não for um caractere numérico
   
     
def  leiaInt ():
    numero = (input( "Digite um numero:" ))
    if numero.isnumeric() == True:
        pass
    else :
        numero = 0
    return numero
print(leiaInt())