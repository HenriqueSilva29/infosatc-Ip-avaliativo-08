#reecreva a função leiaInt (), agora incluindo uma possibilidade
#da digitação de um tipo invalido (fazendo como condições de erro).
#E depois Crie também uma função leiaFloat () com essa mesma funcionalidade.



def leiaInt():

      try:
            numeroInt = int(input( "Insira um numero inteiro: " ))
      except:
            print ( "Ops, inválido!! Apenas número inteiro " )
      else:
            print("número",numeroInt,"válido")

def  leiafloat ():
      try:
            numeroFloat = float(input( "Insira um numero decimal: " ))
      except:
            print ( "Ops, número inválido. Apenas número com vírgula é aceito" )
      else:
            print("número",numeroFloat,"válido")
leiaInt()
leiafloat ()

