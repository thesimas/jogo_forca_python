import random, os, time

def limpa_tela():
    os.system("cls" if os.name == 'nt' else "clear")


def gera_palavra():
    linguagens = ("python", "javascript", "typescript", "kotlin", "java", "cobol", "rust", "swift", "fortran", "haskell", "dart", "scala", "perl", "elixir", "clojure", "pascal", "racket", "erlang", "matlab", "groovy", "fsharp", "visualbasic", "delphi")
    return random.choice(linguagens)


def solicita_letra(letras_jogadas, opcao, tentativas_restantes): #opcao e tentativas_restantes são parametros para chamar a função com_ajuda
    while True:
        tentativa = input("\nDigite uma letra: ").lower()
        print("\nAnalisando...")
        time.sleep(2)
        if len(tentativa) != 1:
            print("\nError! Você digitou mais de um caractere!")
        elif tentativa == "!" and com_ajuda(opcao, tentativas_restantes): #com ajuda so vai retornar TRUE se o usuario escolheu esse modo e se ele tiver mais de 3 tentativas!
            return tentativa # vai retornar o caractere "!"
        elif not tentativa.isalpha():
            print("\nError! Digite apenas uma letra do alfabeto!")
        elif tentativa in letras_jogadas:
            print("\nError! Você já digitou essa letra!")
        elif tentativa == "ç":
            print("\nError! Você digitou o 'ç' e ele não pertence no alfabeto!")
        else:
            return tentativa
        

def verifica_vogal(tentativa):
    vogal = list("aeiou")
    for x in range(0, len(vogal)):
        if tentativa == vogal[x]:
            return True
    
    return False        


def verifica_letra(tentativa, palavra_secreta):
    if tentativa in palavra_secreta:
        return True
    else:
        return False        


def verifica_vitoria(palavra_secreta, letras_acertadas):

    for letra in palavra_secreta:
        if letra not in letras_acertadas:
            time.sleep(2)
            print(f"\nPara descobrir a palavra secreta, você precisa advinhar {len(palavra_secreta) - len(letras_acertadas)} letras!")
            return False

    time.sleep(2)
    print("\nParabéns você advinhou a palavra secreta e ganhou o jogo!")
    return True
    

def exibe_jogo(palavra_secreta, letras_advinhadas, tentativas_restantes, alfabeto, rodada, letras_acertadas, opcao):
    limpa_tela()
    modo_jogo = "Modo com Ajuda" if opcao == 2 else "Modo sem Ajuda"
    
    print("=========== Jogo da Forca! ==========")
    print(f"=== {modo_jogo:<16} Rodada: {rodada} ===")
    print("=====================================\n")
    print("Letras disponiveis:  " , " " .join(alfabeto))
    print(f"Letras advinhadas: {letras_advinhadas}")
    print(f"Tentativas Restantes: {tentativas_restantes}")
    print("Palavra Secreta", " " .join(mostrarPalavra(palavra_secreta,letras_acertadas)))
    print("=====================================")


def menu():
    limpa_tela()
    print(" "*6,"*=" * 45)
    print("\tBem vindo ao jogo da Forca com a temática de Linguagens de Programação!\n")
    print("\t1 - Modo Sem Ajuda!")
    print("\t2 - Modo Com Ajuda!")
    print("\t5 - Para sair\n")
    print("\t* Regras *\n")
    print("\n\t* Você começa com 10 tentativas!\n\t* Modo Com Ajuda - Consome 3 tentativas, caso escolha, informe o caractere '!'(ponto de exclamação).\n\t* Para tentativas erradas:\n\t  ° Vogal perde 2 tentativas!\n\t  ° Consoantes perde 1 tentativa!")
    
    while True:
        try:
            escolha = int(input("\n\tQual modo você escolhe? "))
            if escolha in [1, 2, 5]:
                return escolha
            else:
                print("\t\nOpção inválida!")
        except ValueError:
            print("\t\nErro de tipo de variavel, informe apenas números.")


def mostrarPalavra(palavra_secreta, letras_acertadas):
    palavra_mostrada = []
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_mostrada.append(letra)
        else:
            palavra_mostrada.append("*")

    return palavra_mostrada


def pontuacao(palavra_secreta, tentativas_restantes):

    letras_distintas = set(palavra_secreta)
    numero_letras_distintas = len(letras_distintas)

    pontuacao_jogador = tentativas_restantes + (4 * numero_letras_distintas) + (3 * len(palavra_secreta))

    return pontuacao_jogador


def com_ajuda(opcao, tentativas_restantes):
    if opcao == 2 and tentativas_restantes > 2:
        return True
    elif opcao == 2 and tentativas_restantes < 3:
        print("\nVocê não tem tentativas suficiente para solicitar uma ajuda!")
        return False
    else:
        print("\nVocê não habilitou o Modo com Ajuda!")
        return False


def obtem_palavra_com_ajuda(palavra_secreta, letras_acertadas):
    for letra in palavra_secreta:
        if letra not in letras_acertadas:
            return letra 
    return "" 


def jogo():
    while True:

        opcao = menu()
        palavra_secreta = gera_palavra()
        alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        if opcao == 1 or opcao == 2:
                
            rodada = 1
            letras_advinhadas = 0
            letras_jogadas = []
            letras_acertadas = "" 
            tentativa = ""

            tentativas_restantes = 10
            custo_ajuda = 3
            custo_vogal = 2
            custo_consoante = 1

            exibe_jogo(palavra_secreta, letras_advinhadas, tentativas_restantes, alfabeto, rodada, letras_acertadas, opcao)

            while tentativas_restantes > 0:
                
                tentativa =  solicita_letra(letras_jogadas, opcao, tentativas_restantes)

                if tentativa == "!" and opcao == 2:
                        letra_ajuda = obtem_palavra_com_ajuda(palavra_secreta, letras_acertadas)

                        letras_jogadas.append(letra_ajuda)

                        alfabeto.remove(letra_ajuda)

                        letras_acertadas += letra_ajuda

                        tentativas_restantes -= custo_ajuda
                        print("\nVocê solicitou ajuda e perdeu 3 tentativas!")        
                else:
                    flag_acertou_letra = verifica_letra(tentativa, palavra_secreta)

                    if(flag_acertou_letra):
                        print(f'\nParabéns a letra "{tentativa}" está na palavra secreta!')
                        letras_advinhadas += 1
                        letras_acertadas += tentativa
                        letras_jogadas.append(tentativa)
                        alfabeto.remove(tentativa)

                    else:
                        flag_vogal_ou_consoante = verifica_vogal(tentativa) 
                        if(flag_vogal_ou_consoante):

                            letras_jogadas.append(tentativa)
                            alfabeto.remove(tentativa)
                            
                            print(f'\nQue pena a letra "{tentativa}" não está na palavra secreta!')
                            time.sleep(2)
                            print("\nVocê jogou uma vogal e errou sua tentativa, perdeu 2 tentativas!")
                            tentativas_restantes -= custo_vogal

                        else:
                            letras_jogadas.append(tentativa)
                            alfabeto.remove(tentativa)

                            print(f'\nQue pena a letra "{tentativa}" não está na palavra secreta!')
                            time.sleep(2)
                            print("\nVocê jogou uma consoante, portanto perdeu 1 tentativa!")
                            tentativas_restantes -= custo_consoante

                flag_vitoria = verifica_vitoria(palavra_secreta, letras_acertadas) 
            
                if(flag_vitoria):   #checando se o usuario venceu
                    pontuacao_jogador = pontuacao(palavra_secreta, tentativas_restantes)
                    print("\nAvaliando sua pontuação...")
                    time.sleep(4)
                    print(f"\nSua pontuação por ter ganhado o jogo foi {pontuacao_jogador} pontos!")
                    time.sleep(4)
                    break
                else:
                    rodada += 1
                    time.sleep(3.5)
                    limpa_tela()
                    exibe_jogo(palavra_secreta, letras_advinhadas, tentativas_restantes, alfabeto, rodada, letras_acertadas, opcao)

            if tentativas_restantes <= 0:    
                limpa_tela()
                print("\nSuas Tentativas acabaram e você não adivinhou a palavra secreta...")
                time.sleep(4)
                print(f"\nA palavra secreta era: {palavra_secreta}")
                print(f"\nSua pontuação é ZERO!!")
                time.sleep(4)
        else:
            print("\n\n\tVocê escolheu sair...")
            time.sleep(1.5)
            print("\n\n\tDesenvolvido por: Luciano Simas Junior\n\n")
            time.sleep(1)
            break  
    
if __name__ == "__main__":
    jogo()