
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
'''
Função criada para evitar repetição de código ao adicionar telefones e emails para profissionais e pacientes
'''
# @lista é uma lista de e-mails ou telefones criada anteriormente, e @escolha vem como string "email" OU "telefone" para entrar na condição certa
def adicionar_email_telefone(lista, escolha): 
    if escolha == "email":
        email = "0"
        print("Iniciada repetição para adicionar e-mails.")
        while email != "":
            email = input(f"\tDigite um e-mail (ou pressione Enter para terminar): ")
            if email != "":
                lista.append(email)
            else:
                if len(lista) == 0:
                    print()
                    print("Nenhum e-mail adicionado.")
                    print()

    elif escolha == "telefone":
        telefone = "0"
        print("Iniciada repetição para adicionar telefones (Formato (00)00000-0000)")
        while telefone != "":
            telefone = input("Digite um telefone (ou pressione Enter para terminar): ")
            if telefone != "":
                lista.append(telefone)
            else:
                if len(lista) == 0:
                    print()
                    print("Atenção! É obrigatório ao menos 1(um) telefone para contato.")
                    print()
                    telefone = "0"

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

#---------------------------------------------------------------------------------------------
def submenu_Consultas():
    return "========================================\nCONSULTAS"

#---------------------------------------------------------------------------------------------
def submenu_Relatorios():
    return "========================================\nRELATÓRIOS"


#### Funções =================================================================================

# Recebe o dicionário Banco e 'escolha' vem como "Medicina", "Pacientes" ou "Consulta" dependendo de qual menu foi selecionado
def mostrar_todos(banco, escolha):
    if escolha == "Medicina":

        # Para cada elemento em banco[escolha] chama a função de pesquisar 1
        for crm in banco[escolha]:
            pesquisar_profissional(banco, crm) 
            print("----------------------------------------------------")

    elif escolha == "Pacientes":

        #Para cada elemento em banco[escolha] chama a função de pesquisar 
        for cpf in banco[escolha]:
            pesquisar_paciente(banco,cpf)
            print("----------------------------------------------------")
        
    elif escolha == "Consultas":
        print()
        print("Mostrando todas as consultas: ")

#---------------------------------------------------------------------------------------------
def pesquisar_profissional(banco, crm):
    medicina = banco["Medicina"] 
    if crm in medicina:
        print(f"CRM: {crm}")
        print(f"Nome: {medicina[crm][0]}")
        print(f"Data de nascimento: {medicina[crm][1]}")
        print(f"Sexo: {medicina[crm][2]}")
        print(f"Especialidade: {medicina[crm][3]}")
        print(f"Formação: {medicina[crm][4]}")
        print("E-mails:")
        if len(medicina[crm][5]) == 0:
            print(f"\t- Não há e-mails cadastrados")
        else:
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
        if len(paciente[cpf][5]) == 0:
            print(f"\t- Não há e-mails cadastrados")
        else:
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

    # inicializa listas que serão usadas
    profissional = []
    emails = []
    telefones = []

    crm = input("Digite o CRM do profissional: ")

    # verifica se já está cadastrado e retorna falso caso esteja
    if crm in banco["Medicina"]: 
        return False
    else:

        # aqui ao invés de colocar cada input em uma variável e depois adicionar cada variável na lista "profissional", eu já coloquei um append direto
        profissional.append(input("Digite o nome: "))
        profissional.append(input("Digite a data de nascimento (Formato: DD/MM/AAAA): "))
        profissional.append(input("Digite o sexo (Masculino, Feminino ou Não-binário: "))
        profissional.append(input("Digite a especialidade (Ex: Cardiologista): "))
        profissional.append(input("Digite a universidade de formação (Ex: UFSCar): "))

        # função que adiciona e-mail ou telefone. Tá lá em cima no código, nas repetições
        adicionar_email_telefone(emails, "email") 
        profissional.append(emails) 
        adicionar_email_telefone(telefones, "telefone")
        profissional.append(telefones) 

        # Passa para o CRM certo as informações do profissional criado aqui
        banco["Medicina"][crm] = profissional 
        return True

#---------------------------------------------------------------------------------------------
def adicionar_paciente(banco): #fiz a minha de adicionar_profissional baseada na que vc fez dá uma olhada lá
    '''
    add_paciente.append(cpf,nome,nascimento,sexo,plano_de_saude,emails,telefone)

    Essa parte do código que vc tinha feito não dá certo, porque .append() só aceita 1 argumento de cada vez, então o certo seria
    add_paciente.append(cpf)
    add_paciente.append(nome)
    etc...

    por isso alterei lá na função adicionar_profissional, e já fui fazendo append direto
    '''

#---------------------------------------------------------------------------------------------

# Função de alteração dos dados cadastrados
def alterar_profissional(banco): 
    crm = input("Digite o CRM: ")

    # Verifica se está ou não cadastrado, se não estiver já retorna false
    if crm not in banco["Medicina"]: 
        return False
    
    else:
        print("------------ Informações atuais ------------" )

        # Usei a função de pesquisar, que imprime os dados para mostrar ao uduário quais dados estão cadastrados pelo CRM informado
        pesquisar_profissional(banco, crm) 

        print("*************** Alteração dos dados ***************")
        
        # Quando o usuário aperta Enter a variavel fica vazia
        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") 

        # Se não estiver vazia é alterada no banco e uma mensagem que foi alterada é mostrada
        if nome != "": 
            banco["Medicina"][crm][0] = nome
            print("Nome alterado!")
            print()

        # Ae estiver vazio ele é mostrada mensagem que a variável foi mantida
        else: 
            print("Nome mantido.")
            print()

        # A mesma estrutura se repete daqui em diante para cada variável
        nascimento = input("Digite a nova data de nascimento (ou pressione Enter para manter o atual): ")
        if nascimento != "":
            banco["Medicina"][crm][1] = nascimento
            print("Data de nascimento alterada.")
            print()
        else:
            print("Data de nascimento mantida.")
            print()

        sexo = input("Digite o novo sexo (ou pressione Enter para manter o atual): ")
        if sexo != "":
            banco["Medicina"][crm][2] = sexo
            print("Sexo alterado.")
            print()
        else:
            print("Sexo mantido.")
            print()

        especialidade = input("Digite a nova especialidade (ou pressione Enter para manter o atual): ")
        if especialidade != "":
            banco["Medicina"][crm][3] = especialidade
            print("Especialidade alterada.")
            print()
        else:
            print("Especialidade mantida.")
            print()

        universidade = input("Digite a nova universidade (ou pressione Enter para manter o atual): ")
        if universidade != "":
            banco["Medicina"][crm][4] = universidade
            print("Especialidade alterada.")
            print()
        else:
            print("Especialidade mantida.")
            print()

        # Chama nova função para alterar e-mail, com opções para o usuário escolher
        if alterar_emails(banco, "Medicina", crm):
            print("E-mail(s) alterado(s).")
            print()
        else:
            print("E-mail(s) mantido(s).")
            print()

        # Chama nova função para alterar telefone, com opções para o usuário escolher
        if alterar_telefones(banco, "Medicina", crm):
            print("Telefone(s) alterado(s).")
            print()
        else:
            print("Telefone(s) mantido(s).")
            print()
        
        return True

#---------------------------------------------------------------------------------------------

#Função usada tanto para profissionais quanto para pacientes, por isso está separada
def alterar_emails(banco, dicionario, elemento):
    #inicializa variável de opções
    opt = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os e-mails;")
    print("2. Alterar um e-mail existente;")
    print("3. Adicionar um ou mais novos e-mails;")
    print("4. Excluir e-mail existente;")
    print("5. Manter e-mail(s) atual(is);")
    opt = input("Digite sua escolha: ")

    # Para alterar todos os e-mails é criada uma nova lista, e chamada a função de adicionar, depois é passado ao banco
    if opt == "1":
        emails = []
        adicionar_email_telefone(emails, "email")
        banco[dicionario][elemento][5] = emails
        return True
    
    # Para alterar somente um e-mail existente 
    elif opt == "2":
        i = 0

        # Mostra ao usuário os e-mails cadastrados com index i
        for email in banco[dicionario][elemento][5]:
            print(f"{i} - {email}")
            i+=1
        
        # Pede para que ele escolha o index do e-mail que quer alterar
        index = int(input("Qual e-mail deseja alterar? Digite apenas o número: "))

        # Altera o e-mail com base na escolha do usuário
        banco[dicionario][elemento][5][index] = input("Digite o novo e-mail: ")
        return True
    
    # Para adicionar e-mail aos que já existem, a ideia é a mesma da opção 1, mas não é criara uma nova lista, apenas é chamada a função de adicionar com a lista já existente no banco
    elif opt == "3":
        adicionar_email_telefone(banco[dicionario][elemento][5], "email")
        return True
    
    # Para a pessoa excluir um e-mail existente a ideia é a mesma da opção de alterar existentes, mas usa o del para deletar o index escolhido
    elif opt == "4":
        i = 0
        for email in banco[dicionario][elemento][5]:
            print(f"{i} - {email}")
            i+=1
        index = int(input("Qual e-mail deseja excluir? Digite apenas o número: "))
        del banco[dicionario][elemento][5][index]
        return True
    
    elif opt == "5":
        return False
    
    else:
        print(f"\nAtenção! Opção inválida.")
        return False

#---------------------------------------------------------------------------------------------

# Mesma explicação da função alterar_emails()
def alterar_telefones(banco, dicionario, elemento):
    opt = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os telefones;")
    print("2. Alterar um telefone existente;")
    print("3. Adicionar um ou mais novos telefones;")
    print("4. Excluir telefone existente;")
    print("5. Manter telefone(s) atual(is);")
    opt = input("Digite sua escolha: ")
    if opt == "1":
        telefones = []
        adicionar_email_telefone(telefones, "telefone")
        banco[dicionario][elemento][6] = telefones
        return True
    
    elif opt == "2":
        i = 0
        for telefone in banco[dicionario][elemento][6]:
            print(f"{i} - {telefone}")
            i+=1
        escolha = int(input("Qual telefone deseja alterar? Digite apenas o número: "))
        banco[dicionario][elemento][6][escolha] = input("Digite o novo telefone (Formato: (00)00000-0000): ")
        return True
    
    elif opt == "3":
        adicionar_email_telefone(banco[dicionario][elemento][6], "telefone")
        return True
    
    elif opt == "4":
        i = 0
        for telefone in banco[dicionario][elemento][6]:
            print(f"{i} - {telefone}")
            i+=1
        escolha = int(input("Qual telefone deseja excluir? Digite apenas o número: "))
        del banco[dicionario][elemento][6][escolha]
        if len(banco[dicionario][elemento][6]) == 0:
            print("Atenção! Nenhum telefone cadastrado. É obrigatório possuir pelo menos 1 telefone para contato.")
            adicionar_email_telefone(banco[dicionario][elemento][6], "telefone")
        return True
    
    elif opt == "5":
        return False
    
    else:
        print(f"\nAtenção! Opção inválida.")
        return False



#### Main ====================================================================================
def main():
    Banco = {"Medicina":{"CRM001":["Pedro de Paula", "12/12/1995", "Masculino", "Cardiologista", "UFSCar", ["pedro@gmail.com", "drpedro@unimed.com"], ["(16)99999-9999", "(16)3333-3333"]], "CRM002":["Ana Clara Souza", "06/06/2000", "Feminino", "Pneumologista", "USP", ["clara@santacasa.com"], ["(11)9999-9999", "(11)9999-8888", "(11)4444-4444"]]}, "Pacientes":{"CPF1":["Alex Nunes","27/05/1998","Masculino","Unimed",["alex@gmail.com"],["(16) 5555-5555"]],"CPF2":["Elen Maria Da Silva","06/06/1955","Feminino","SUS",["elen@gmail.com"],["(14)1234-9876"]]}, "Consultas":{}}

    # Inicializa opt em 1 para entrar no loop
    # receberá novo valor de menuPrincipal()
    opt = 1
    while opt!=5:
        opt = menu_Principal()

        #inicializa opção para submenus subopt
        subopt = 1 
        if opt == 1:

            # enquanto subopt não indicar retorno ao menu principal(6) ou encerrar(7), repete o submenu de medicina
            while subopt!=6 and subopt!=7:
                subopt = submenu_Medicina()

                # condições para acessar funções específicas
                if subopt == 1:
                    print()
                    print("************ Profissionais de Medicina *************")
                    mostrar_todos(Banco, "Medicina") # FUNCIONANDO

                elif subopt == 2:
                    print(f"\n********** Pesquisar profissional de medicina *********** ")
                    crm = input("Digite o CRM do profissional: ")
                    print(f"\n****************** Resultado da busca ******************* ")
                    if not pesquisar_profissional(Banco, crm):
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
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
                    print(f"\n************ Alterar cadastro profissional *************")
                    if alterar_profissional(Banco): # FUNCIONANDO
                        print(f"\n------------------------------------")
                        print("Profissional adicionado com sucesso!")
                        print("------------------------------------")
                    else:
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
                        print("--------------------------------------------------------------")
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
                    print()
                    print("******************** Pacientes *********************")
                    mostrar_todos(Banco, "Pacientes") # FUNCIONANDO

                elif subopt == 2:
                    print(f"\n****************** Pesquisar paciente ******************* ")
                    cpf=input("Digite o CPF do paciente: ")
                    print()
                    print(f"\n****************** Resultado da busca ******************* ") 
                    if not pesquisar_paciente(Banco,cpf): # FUNCIONANDO
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente")
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