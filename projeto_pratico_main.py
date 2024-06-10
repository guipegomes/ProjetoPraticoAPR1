
#### Repetições ==============================================================================
'''
Loops em funções para não ter muita repetição de código
'''
def loopEscolhas(max): # max é o número de escolhas dos menus
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

#---------------------------------------------------------------------------------------------
def adicionar_email_telefone(lista, escolha): # para que não fique repetindo as estruturas para profissionais e pacientes
    if escolha == "email":
        email = ""
        print("Iniciada repetição para adicionar e-mails. Para finalizar digite '-1'.")
        while email != "-1":
            email = input(f"\tDigite um e-mail: ")
            if email != "-1":
                lista.append(email)
    elif escolha == "telefone":
        telefone = ""
        print("Iniciada repetição para adicionar telefones (Formato (00) 0000-0000 ou (00) 00000-0000). Para finalizar digite '-1'.")
        while telefone != "-1":
            telefone = input("Digite um telefone: ")
            if telefone != "-1":
                lista.append(telefone)
    return lista

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
    print("==================== Menu principal ====================")
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
    print("========== Menu de Profissionais de Medicina ===========")
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
    print("================== Menu de Pacientes ===================")
    print("1. Mostrar todos;")
    print("2. Pesquisar paciente;")
    print("3. Adicionar paciente;")
    print("4. Alterar cadastro de paciente;")
    print("5. Excluir cadastro de paciente;")
    print("6. Retornar ao Menu Principal;")
    print("7. Encerrar.")
    
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
        
        #Para cada elemento em banco[escolha] chama a função de pesquisar 
        for cpf in banco[escolha]:
            pesquisar_paciente(banco,cpf)
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
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------
def pesquisar_paciente(banco, cpf):
    paciente = banco["Pacientes"]
    if cpf in paciente:
        print(f"CPF: {cpf}")
        print(f"Nome: {paciente[cpf][0]}")
        print(f"Data de nascimento: {paciente[cpf][1]}")
        print(f"Sexo: {paciente[cpf][2]}")
        print(f"Plano de Saúde: {paciente[cpf][3]}")
        print(f"Emails:")
        for email in paciente[cpf][4]:
                print(f"\t- {email}")
        print("Telefones:")
        for telefone in paciente[cpf][5]:
                print(f"\t- {telefone}")
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------
def adicionar_profissional(banco):
    crm = input("Digite o CRM do profissional: ")
    if crm in banco["Medicina"]:
        return False #retorno para mensagem na main
    else:
        banco["Medicina"][crm] = []
        banco["Medicina"][crm].append(input("Digite o nome: "))
        banco["Medicina"][crm].append(input("Digite a data de nascimento (Formato: DD/MM/AAAA): "))
        banco["Medicina"][crm].append(input("Digite o sexo (Formato: Masculino ou Feminino): "))
        banco["Medicina"][crm].append(input("Digite a especialidade (Ex: Cardiologista): "))
        banco["Medicina"][crm].append(input("Digite a universidade de formação (Ex: UFSCar): "))
        emails = []
        banco["Medicina"][crm].append(adicionar_email_telefone(emails, "email")) #chama função para adicionar
        telefones = []
        banco["Medicina"][crm].append(adicionar_email_telefone(telefones, "telefone")) #chama função para adicionar
        return True #retorno para mensagem na main


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
                    print(f"\n********** Pesquisar profissional de medicina *********** ")
                    crm = input("Digite o CRM do profissional: ")
                    print(f"\n****************** Resultado da busca ******************* ")
                    if not pesquisar_profissional(Banco, crm):
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente") # FUNCIONANDO
                        print("--------------------------------------------------------------")

                elif subopt == 3:
                    print(f"\n*************** Adicionando profissional ****************")
                    if adicionar_profissional(Banco): #FUNCIONANDO
                        print(f"\n------------------------------------")
                        print("Profissional adicionado com sucesso!")
                        print("------------------------------------")
                    else:
                        print(f"\n---------------------------------------")
                        print("Já existe um profissional com este CRM.")
                        print("---------------------------------------")

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
                    print(f"\n****************** Pesquisar paciente ******************* ")
                    cpf=input("Digite o CPF do paciente: ")
                    print()
                    print(f"\n****************** Resultado da busca ******************* ") # FUNCIONANDO
                    if not pesquisar_paciente(Banco,cpf):
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente") # FUNCIONANDO
                        print("----------------------------------------------------------")

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


#### Programa principal ======================================================================
main()