
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

#---------------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------------
def submenu_Pacientes():
    print()
    print("=========================================")
    print("Menu de Pacientes:")
    print("1.Mostrar todos;")
    print("2.Pesquisar paciente;")
    print("3.Adicionar paciente;")
    print("4.Alterar cadastro de paciente;")
    print("5.Excluir cadastro de paciente;")
    print("6.Retornar ao Menu Principal;")
    print("7.Encerrar.")
    
    return loopEscolhas(7)

def submenu_Consultas():
    return "========================================\nCONSULTAS"

def submenu_Relatorios():
    return "========================================\nRELATÓRIOS"

#### Funções =================================================================================

# Recebe o dicionário Banco e 'escolha' vem como "Medicina", "Pacientes" ou "Consulta" dependendo de qual menu foi selecionado
def mostrar_todos(banco, escolha):
    if escolha == "Medicina":
        print()
        print("************ Profissionais de Medicina *************")

        # Para cada elemento em banco[escolha] chama a função de pesquisar 1
        for crm in banco[escolha]:
            pesquisar_profissional(banco, crm) 
            print("----------------------------------------------------")

    elif escolha == "Pacientes":
        print()
        print("******************** Pacientes *********************")

        #Para cada elemento em banco[escolha] (Neste caso é o dict Pacientes dentro de Banco)
        for elem in banco[escolha]:
            print(f"CPF:{elem}")
            print(f"Nome:{banco[escolha][elem][0]}")
            print(f"Data de nascimento:{banco[escolha][elem][1]}")
            print(f"Sexo:{banco[escolha][elem][2]}")
            print(f"Plano de Saúde:{banco[escolha][elem][3]}")
            print(f"Emails:")
            for email in banco [escolha][elem][4]:
                print(f"\t- {email}")
            print("Telefones:")
            for telefone in banco[escolha][elem][5]:
                print(f"\t- {telefone}")
            print("----------------------------------------------------")
        
    elif escolha == "Consultas":
        print()
        print("Mostrando todas as consultas: ")

#---------------------------------------------------------------------------------------------

def pesquisar_profissional(banco, crm):
    medicina = banco["Medicina"] #coloquei em uma variável pra ficar mais fácil para escrever o código
    if crm in medicina:
        print(f"CRM: {crm}")
        print(f"Nome: {medicina[crm][0]}")
        print(f"Data de nascimento: {medicina[crm][1]}")
        print(f"Sexo: {medicina[crm][2]}")
        print(f"Especialidade: {medicina[crm][3]}")
        print(f"Formação: {medicina[crm][4]}")
        print("E-mails:")
        for email in medicina[crm][5]:
            print(f"\t- {email}")
        print("Telefones: ")
        for telefone in medicina[crm][6]:
            print(f"\t- {telefone}")
    else:
        print("Profissional não encontrado. Verifique o CRM e tente novamente")

def pesquisar_paciente(banco, cpf):
    # Aqui vc pode fazer igual o código de cima
    print("Print só pra ter alguma coisa aqui dentro") # pode apagar

#### Main ====================================================================================
def main():
    Banco = {"Medicina":{"CRM001":["Pedro de Paula", "12/12/1995", "Masculino", "Cardiologista", "UFSCar", ["pedro@gmail.com", "drpedro@unimed.com"], ["(16)99999-9999", "(16)3333-3333"]], "CRM002":["Ana Clara Souza", "06/06/2000", "Feminino", "Pneumologista", "USP", ["clara@santacasa.com"], ["(11)9999-9999", "(11)9999-8888", "(11)4444-4444"]]}, "Pacientes":{"CPF1":["Alex Nunes","27/05/1998","Masculino","Unimed",["alex@gmail.com"],["(16) 5555-5555"]],"CPF2":["Elen Maria Da Silva","06/06/1955","Feminino","SUS",["elen@gmail.com"],["(14)1234-9876"]]}, "Consultas":{}}
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
                    mostrar_todos(Banco, "Medicina") # FUNCIONANDO
                elif subopt == 2:
                    crm = input("Digite o CRM do profissional: ")
                    print()
                    print("********** Mostrando profissionais de medicina ********** ")
                    pesquisar_profissional(Banco, crm)
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
                    mostrar_todos(Banco, "Pacientes") # FUNCIONANDO
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