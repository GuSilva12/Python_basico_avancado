# EXERCÍCIO GUIADO COM WHILE
# Iterando strings com while

nome = "Luiz Otávio"

tamanho_str = len(nome)

i = 0               # setando um contador de valor inicial 0 que será usado como index para acessar cada caracter da str
novo_nome = ''      # setando uma string vazia para iteração e concatenação dos caractere da variável 'nome'

while i < tamanho_str:      # enquanto i menor que o tamanho da string, executar ação do bloco
    letra = nome[i]         # variavel do laço recebe um index para acessar o caracter correspondente
    novo_nome += letra      # variavel do laço recebe o caracter referenteao index acessado na str e concatena, na ocorrencia de outras iterações, nessa variavel
    i+=1                    # soma 1 ao contador, para ser usado como acessao ao próximo index

print(novo_nome)    # imprime o valor gerado e armazenado na variavel do laço while