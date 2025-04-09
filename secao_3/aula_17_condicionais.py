# INTRODUCAO AOS BLOCOS DE CODIGO + IF/EKIF/ELSE (CONDICIONAIS)

# caso o programa coninue apos o bloco de condicoes, apos realizada a condicao, o programa continua seu fluxo.

# if - se
# elif - senao, se
# else - senao

entrada = input("Você quer 'entrar' ou 'sair'? ")

if(entrada == 'entrar'):
    print("Você entrou no sistema.")
elif(entrada == 'sair'):
    print("Você saiu do sistema")
else:
    print("OPÇÃO NÃO VÁLIDA!!!")