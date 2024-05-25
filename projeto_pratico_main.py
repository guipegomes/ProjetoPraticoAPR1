
#### Repetições de escolha dos menus =========================================================
'''
Loop em função para não ter muita repetição de código
Variável max é o número máximo de opções que o menu tem
É utilizada em uma das verificações e nas mensagens de erro
'''
def loopEscolhas(max):
    # inicializa variável loop como condição na repetição while
    loop = True
    while loop: 
        entrada = input("Digite a opção escolhida: ")

        # verifica se a entrada é um digito e então faz a conversão para int se verdadeiro
        # dessa maneira garante que não ocorrerá erro ao converter logo no input
        if entrada.isdigit(): 
            opt = int(entrada)

            # condição para sair do loop
            if opt>=1 and opt<=max: 
                loop = False 
            
        # chama função com mensagem de opção inválida caso não cumpra condições
            else:
                msg_Invalida(max) 
        else: 
            msg_Invalida(max)
    return opt

#### Mensagens ===============================================================================
'''
Utilizada quando há erro de escolha do usuário
Recebe max, que é o número máximo de escolhas do menu
'''
def msg_Invalida(max):
    print()
    print("-----------------------------------------------------------")
    print(f"Atenção! Opção inválida. Digite apenas números entre 1 e {max}.")
    print("-----------------------------------------------------------")
    print()
#---------------------------------------------------------------------------------------------
def msg_Encerrado():
    print()
    print("========================================")
    print("Programa encerrado.")
    print()

##### Menus ==================================================================================
def menu_Principal():
    print()
    print("========================================")
    print("Menu principal:")
    print("1. Profissionais de Medicina;")
    print("2. Pacientes;")
    print("3. Consultas;")
    print("4. Relatórios;")
    print("5. Encerrar;")

    # chama função que contém loop de repetição com 5 opções
    return loopEscolhas(5)

#=================================================================================
def submenu_Medicina():
    print()
    print("========================================")
    print("Menu de Profissionais de Medicina:")
    print("1. Mostrar todos;")
    print("2. Pesquisar profissional;")
    print("3. Adicionar profissional;")
    print("4. Alterar cadastro de profissional;")
    print("5. Excluir cadastro de profissional;")
    print("6. Retornar ao Menu Principal;")
    print("7. Encerrar.")

    # chama função que contém loop de repetição com 7 opções    
    return loopEscolhas(7)

#=========================================================================================
def submenu_Pacientes():
    print()
    print("=========================================")
    print("Menu de Pacientes:")
    print("1.Mostrar todos;")
    print("2.Pesquisar paciente;")
    print("3.Adicionar paciente;")
    print("4.Alterar cadastro de profissional;")
    print("5.Excluir cadastro de paciente;")
    print("6.Retornar ao Menu Principal;")
    print("7.Encerrar.")
    
    return loopEscolhas(7)

def submenu_Consultas():
    return "========================================\nCONSULTAS"

def submenu_Relatorios():
    return "========================================\nRELATÓRIOS"

#### Main ====================================================================================
def main():
    # Inicializa opt em 1 para entrar no loop
    # receberá novo valor de menuPrincipal()
    opt = 1
    while opt!=5:
        opt = menu_Principal()
        subopt = 1 #inicializa opção para submenus subopt
        if opt == 1:

            # enquanto subopt não indicar retorno ao menu principal(6) ou encerrar(7), repete o submenu de medicina
            while subopt!=6 and subopt!=7:
                subopt = submenu_Medicina()
                # condições para acessar funções específicas
                if subopt == 1:
                    print("1. Mostrar todos;") # TESTE
                elif subopt == 2:
                    print("2. Pesquisar profissional;") # TESTE
                elif subopt == 3:
                    print("3. Adicionar profissional;") # TESTE
                elif subopt == 4:
                    print("4. Alterar cadastro de profissional;") # TESTE
                elif subopt == 5:
                    print("5. Excluir cadastro de profissional;") # TESTE
                elif subopt == 6:
                    print("6. Retornar ao Menu Principal;") # TESTE
                elif subopt == 7:
                    msg_Encerrado()
                    opt = 5
         #Após selecionar a opção 2 inicializa o bloco de comandos.           
        elif opt == 2:
            #Enquanto subopt for diferente de 6(menu principal) e 7(encerrar), o submenu de pacientes se repete 
            while subopt!=6 and subopt!=7:
                subopt=submenu_Pacientes()
                #condições para acessar determinadas funções
                if subopt==1:
                     print("1. Mostrar todos;") # TESTE
                elif subopt == 2:
                    print("2. Pesquisar paciente;") # TESTE
                elif subopt == 3:
                    print("3. Adicionar paciente;") # TESTE
                elif subopt == 4:
                    print("4. Alterar cadastro do paciente;") # TESTE
                elif subopt == 5:
                    print("5. Excluir cadastro do paciente;") # TESTE
                elif subopt == 6:
                    print("6. Retornar ao Menu Principal;") # TESTE
                elif subopt == 7:
                    msg_Encerrado()
                    opt = 5
                    
        elif opt == 3:
            print(submenu_Consultas()) # TESTE
        elif opt == 4:
            print(submenu_Relatorios()) # TESTE
        elif opt == 5:
            msg_Encerrado()
        else:
            print("========================================")
            print("aparentemente esse else é inútil")


#### Programa principal ======================================================================
main()