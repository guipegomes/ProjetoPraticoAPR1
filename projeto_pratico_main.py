#############################################################################################
#                                  Projeto Prático de APR1                                  #
#           Alunos: SC3044653: Guilherme Perez Gomes                                        #
#                   SC3045668: Stephanie Marys                                              #
#                                                                                           #
#           Professora: Eloize                                                              #
#############################################################################################

#### Importações ============================================================================
import os
import datetime

#############################################################################################
#### Repetições =============================================================================
#############################################################################################

# recebe numero_de_opcoes de cada menu com o numero maximo de opcoes que aquele menu tem
def obter_e_validar_escolha_do_usuario(numero_de_opcoes): 
    while True: 
        entrada = input("Digite a opção escolhida: ")
        
        if entrada.isdigit():
            escolha = int(entrada)

            if escolha >= 1  and escolha <= numero_de_opcoes: 
                return escolha
            
            else:
                print()
                print("-----------------------------------------------------------")
                print(f"Atenção! Opção inválida. Digite apenas números entre 1 e {numero_de_opcoes}.")
                print("-----------------------------------------------------------")
                print()

        else: 
            print()
            print("-----------------------------------------------------------")
            print(f"Atenção! Opção inválida. Digite apenas números entre 1 e {numero_de_opcoes}.")
            print("-----------------------------------------------------------")
            print()

#--------------------------------------------------------------------------------------------

# recebe chave como crm, cpf ou tupla(crm, cpf, data, hora)
def chave_existe_no_dicionario(dicionario, chave): 
    if chave in dicionario:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def criar_tupla_de_chaves(): 
    crm = input("Digite o CRM do profissional: ")
    cpf = input("Digite o CPF do paciente (Somente números): ")
    data_da_consulta = input("Digite a data da consulta (DD-MM-AAAA): ")
    hora_da_consulta =  input("Digite a hora da consulta (Formato 24h: 9h00, 15h30): ")
    tupla_de_chaves = (crm, cpf, data_da_consulta, hora_da_consulta)

    return tupla_de_chaves

#--------------------------------------------------------------------------------------------
def adicionar_email(lista_emails): 
        email = "entrada loop"
        print("Iniciada repetição para adicionar e-mails.")

        while email != "":
            email = input(f"\tDigite um e-mail (ou pressione Enter para terminar): ")

            if email != "":
                lista_emails.append(email)

            else:
                if len(lista_emails) == 0:
                    print()
                    print("Nenhum e-mail adicionado.")
                    print()

#--------------------------------------------------------------------------------------------
def adicionar_telefone(lista_telefones): 
        telefone = "entrada loop"
        print("Iniciada repetição para adicionar telefones (Formato (00)00000-0000)")

        while telefone != "":
            telefone = input("Digite um telefone (ou pressione Enter para terminar): ")
            
            if telefone != "":
                lista_telefones.append(telefone.replace(" ", ""))

            else:
                if len(lista_telefones) == 0:
                    print()
                    print("Atenção! É obrigatório ao menos 1(um) telefone para contato.")
                    print()
                    telefone = "continua loop"

#--------------------------------------------------------------------------------------------
def adicionar_medicamentos_e_posologias(lista_medicamentos, lista_posologias): 
    medicamento = "entrada loop"
    posologia = "entrada verificação"

    while medicamento != "":
        medicamento = input("Digite um medicamento indicado (Formato: Losartana 50mg) (ou pressione Enter para terminar): ")

        if medicamento == "" and len(lista_medicamentos) == 0:
            print()
            print(f"Atenção! É necessário acrescentar um medicamento.")
            print()
            medicamento = "continua loop"

        else:
            if medicamento != "":
                lista_medicamentos.append(medicamento)

                while posologia != "adicionada" or len(lista_posologias) != len(lista_medicamentos):
                    posologia = input(f"Digite a posologia para {medicamento} (Formatos: 1x dia; 8h/8h): ")

                    if posologia == "" and medicamento != "":
                        print()
                        print(f"Atenção! É necessário acrescentar uma posologia ao medicamento {medicamento}.")

                    else:
                        lista_posologias.append(posologia)
                        print()
                        print("Medicamento adicionado.")
                        print()
                        posologia = "adicionada"

#--------------------------------------------------------------------------------------------
# dicionario = Medicina ou Pacientes
# chave = crm ou cpf
# posicao = posicao da lista de e-mails no dicionário '4' para pacientes e '5' para medicina
def alterar_emails(dicionario, chave, posicao):
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os e-mails;")
    print("2. Alterar um e-mail existente;")
    print("3. Adicionar um ou mais novos e-mails;")
    print("4. Excluir e-mail existente;")
    print("5. Manter e-mail(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    # Alterar todos os e-mails
    if opcao == "1":
        emails = []
        adicionar_email(emails)
        dicionario[chave][posicao] = emails
        return True
    
    # Alterar um e-mail existente
    elif opcao == "2":
        print()
        print("E-mails por índice: ")
        index = 0
        for email in dicionario[chave][posicao]:
            print(f"\t{index} - {email}")
            index+=1
        print()
        escolha = int(input("Qual e-mail deseja alterar? Digite apenas o índice: "))
        dicionario[chave][posicao][escolha] = input("Digite o novo e-mail: ")
        return True
    
    # Adicionar um ou mais novos e-mails aos existentes
    elif opcao == "3":
        adicionar_email(dicionario[chave][posicao])
        return True
    
    # Excluir e-mail existente
    elif opcao == "4":
        print()
        print("E-mails por índice: ")
        index = 0
        for email in dicionario[chave][posicao]:
            print(f"\t{index} - {email}")
            index+=1
        print()
        escolha = int(input("Qual e-mail deseja excluir? Digite apenas o número: "))
        del dicionario[chave][posicao][escolha]
        return True
    
    # Manter os e-mails atuais
    elif opcao == "5":
        return False
    
    # Opção inválida mantém os e-mails atuais também
    else:
        print(f"\nAtenção! Opção inválida.")
        return False

#--------------------------------------------------------------------------------------------
# dicionario = Medicina ou Pacientes
# chave = crm ou cpf
# posicao = posicao da lista de e-mails no dicionário '5' para pacientes e '6' para medicina
def alterar_telefones(dicionario, chave, posicao):
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os telefones;")
    print("2. Alterar um telefone existente;")
    print("3. Adicionar um ou mais novos telefones;")
    print("4. Excluir telefone existente;")
    print("5. Manter telefone(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    # Alterar todos os telefones
    if opcao == "1":
        telefones = []
        adicionar_telefone(telefones)
        dicionario[chave][posicao] = telefones
        return True
    
    # Alterar um telefone existente
    elif opcao == "2":
        print()
        print("Telefones por índice: ")
        index = 0
        for telefone in dicionario[chave][posicao]:
            print(f"\t{index} - {telefone}")
            index+=1
        print()
        escolha = int(input("Qual telefone deseja alterar? Digite apenas o índice: "))
        dicionario[chave][posicao][escolha] = input("Digite o novo telefone (Formato: (00)00000-0000): ")
        return True
    
    # Adicionar um ou mais telefones aos existentes
    elif opcao == "3":
        adicionar_telefone(dicionario[chave][posicao])
        return True
    
    # Excluir telefone existente
    elif opcao == "4":
        print()
        print("Telefones por índice: ")
        index = 0
        for telefone in dicionario[chave][posicao]:
            print(f"\t{index} - {telefone}")
            index+=1
        print()
        escolha = int(input("Qual telefone deseja excluir? Digite apenas o índice: "))
        del dicionario[chave][posicao][escolha]

        # Não é permite lista de telefones vazia
        if len(dicionario[chave][posicao]) == 0:
            print("Atenção! Nenhum telefone cadastrado. É obrigatório possuir pelo menos 1 telefone para contato.")
            adicionar_telefone(dicionario[chave][posicao])
        return True
    
    # Mantém os telefones atuais
    elif opcao == "5":
        return False
    
    # Opção inválida mantém os telefones atuais
    else:
        print(f"\nAtenção! Opção inválida.")
        return False
    
#--------------------------------------------------------------------------------------------
def alterar_medicamentos_e_posologias(dict_consultas, tupla_chaves):
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os medicamentos;")
    print("2. Alterar um medicamento existente;")
    print("3. Adicionar um ou mais novos medicamentos;")
    print("4. Excluir medicamento existente;")
    print("5. Manter medicamento(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    # Altera todos os medicamentos
    if opcao == "1":
        medicamentos = []
        posologias = []
        adicionar_medicamentos_e_posologias(medicamentos, posologias)
        dict_consultas[tupla_chaves][1] = medicamentos
        dict_consultas[tupla_chaves][2] = posologias
        return True
    
    # Altera medicamento existente
    elif opcao == "2":
        index = 0
        for medicamento in dict_consultas[tupla_chaves][1]:
            print(f"{index} - {medicamento}")
            index+=1
        escolha = int(input("Qual medicamento deseja alterar? Digite apenas o número: "))
        dict_consultas[tupla_chaves][1][escolha] = input("Digite o novo medicamento (Formato: Losartana 50mg): ")
        dict_consultas[tupla_chaves][2][escolha] = input("Digite a nova posologia (Formatos: 1x dia; 8h/8h): ")
        return True
    
    # Adiciona novos medicamento(s) aos existentes
    elif opcao == "3":
        adicionar_medicamentos_e_posologias(dict_consultas[tupla_chaves][1], dict_consultas[tupla_chaves][2])
        return True
    
    # Exclui medicamento existente
    elif opcao == "4":
        index = 0
        for medicamento in dict_consultas[tupla_chaves][1]:
            print(f"{index} - {medicamento}")
            index+=1
        escolha = int(input("Qual medicamento deseja excluir? Digite apenas o número: "))
        del dict_consultas[tupla_chaves][1][escolha]
        del dict_consultas[tupla_chaves][2][escolha]

        # Não é permite lista de medicamentos vazia
        if len(dict_consultas[tupla_chaves][1]) == 0:
            print("Atenção! Nenhum medicamento cadastrado. É obrigatório possuir pelo menos 1 medicamento.")
            adicionar_medicamentos_e_posologias(dict_consultas[tupla_chaves][1], dict_consultas[tupla_chaves][2])
        return True
    
    # Mantém os medicamentos atuais
    elif opcao == "5":
        return False
    
    # Opção inválida mantém os medicamentos atuais
    else:
        print(f"\nAtenção! Opção inválida.")
        return False

#--------------------------------------------------------------------------------------------
def obter_datetime_agora_data_e_hora():
    agora = datetime.datetime.now()
    data = agora.strftime("%d-%m-%Y")
    hora = agora.strftime("%Hh%Mm%Ss")
    return agora, data, hora

#--------------------------------------------------------------------------------------------
def calcular_idade(dicionario, chave, agora):
    from datetime import datetime
    data_nascimento = datetime.strptime(dicionario[chave][1], "%d-%m-%Y")
    idade_pessoa = agora.year - data_nascimento.year
    if agora.month == data_nascimento.month and agora.day < data_nascimento.day:
            idade_pessoa -= 1
            return idade_pessoa
    elif agora.month < data_nascimento.month:
        idade_pessoa -= 1
        return idade_pessoa
    else:
        return idade_pessoa

#############################################################################################
#### Mensagens ==============================================================================
#############################################################################################
def msg_encerrado():
    print()
    print("========================================")
    print("Programa encerrado.")
    print()

#############################################################################################
##### Menus =================================================================================
#############################################################################################
def menu_principal():
    print()
    print("==================== Menu principal ====================")
    print("1. Profissionais de Medicina;")
    print("2. Pacientes;")
    print("3. Consultas;")
    print("4. Relatórios;")
    print("5. Encerrar;")
    escolha = obter_e_validar_escolha_do_usuario(5)
    return escolha

#--------------------------------------------------------------------------------------------
def submenu_medicina():
    print()
    print("========== Menu de Profissionais de Medicina ===========")
    print("1. Mostrar todos;")
    print("2. Pesquisar profissional;")
    print("3. Adicionar profissional;")
    print("4. Alterar cadastro de profissional;")
    print("5. Excluir cadastro de profissional;")
    print("6. Retornar ao Menu Principal;")
    print("7. Encerrar.")  
    escolha = obter_e_validar_escolha_do_usuario(7)
    return escolha

#--------------------------------------------------------------------------------------------
def submenu_pacientes():
    print()
    print("================== Menu de Pacientes ===================")
    print("1. Mostrar todos;")
    print("2. Pesquisar paciente;")
    print("3. Adicionar paciente;")
    print("4. Alterar cadastro de paciente;")
    print("5. Excluir cadastro de paciente;")
    print("6. Retornar ao Menu Principal;")
    print("7. Encerrar.")
    escolha = obter_e_validar_escolha_do_usuario(7)
    return escolha

#--------------------------------------------------------------------------------------------
def submenu_consultas():
    print()
    print("================== Menu de Consultas ===================")
    print("1. Mostrar todas;")
    print("2. Pesquisar consulta;")
    print("3. Adicionar consulta;")
    print("4. Alterar consulta;")
    print("5. Excluir consulta;")
    print("6. Retornar ao Menu Principal;")
    print("7. Encerrar.")
    escolha = obter_e_validar_escolha_do_usuario(7)
    return escolha

#--------------------------------------------------------------------------------------------
def submenu_relatorios():
    print()
    print("================== Menu de Relatórios ===================")
    print("1. Gerar relatório de especialidade médica específica;")
    print("2. Gerar relatório de pacientes até a idade específica;")
    print("3. Gerar relatório de consultas dos últimos dias;")
    print("4. Retornar ao Menu Principal;")
    print("5. Encerrar.")
    escolha = obter_e_validar_escolha_do_usuario(5)
    return escolha


#############################################################################################
#### Funções Específicas ====================================================================
#############################################################################################
def mostrar_todos_os_profissionais(dict_medicina):
    if len(dict_medicina) == 0:
        return False
    else:
        # Chama a função "pesquisar", que imprime dados no terminal
        for crm in dict_medicina:
            pesquisar_profissional_medicina(dict_medicina, crm) 
            print("----------------------------------------------------")
        return True

#---------------------------------------------------------------------------------------------
def mostrar_todos_os_pacientes(dict_pacientes):  
    if len(dict_pacientes) == 0:
        return False
    else:
        # Chama a função "pesquisar", que imprime dados no terminal
        for cpf in dict_pacientes:
            pesquisar_paciente(dict_pacientes, cpf)
            print("----------------------------------------------------")
        return True

#--------------------------------------------------------------------------------------------
def mostrar_todas_as_consultas(dict_consultas, dict_medicina, dict_pacientes): 
    if len(dict_consultas) == 0:
        return False
    else:
        # Chama a função "pesquisar", que imprime dados no terminal
        for tupla in dict_consultas:
            pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla)
            print("----------------------------------------------------")
        return True

#--------------------------------------------------------------------------------------------
def pesquisar_profissional_medicina(dict_medicina, crm): 
    if chave_existe_no_dicionario(dict_medicina, crm):
        print(f"CRM: {crm}")
        print(f"Nome: {dict_medicina[crm][0]}")
        print(f"Data de nascimento: {dict_medicina[crm][1]}")
        print(f"Sexo: {dict_medicina[crm][2]}")
        print(f"Especialidade: {dict_medicina[crm][3]}")
        print(f"Formação: {dict_medicina[crm][4]}")
        print("E-mails:")
        if len(dict_medicina[crm][5]) == 0:
            print(f"\t- Não há e-mails cadastrados")
        else:
            for email in dict_medicina[crm][5]:
                print(f"\t- {email}")
        print("Telefones: ")
        for telefone in dict_medicina[crm][6]:
            print(f"\t- {telefone}")
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def pesquisar_paciente(dict_pacientes, cpf):
    if chave_existe_no_dicionario(dict_pacientes, cpf):
        print(f"CPF: {cpf}")
        print(f"Nome: {dict_pacientes[cpf][0]}")
        print(f"Data de nascimento: {dict_pacientes[cpf][1]}")
        print(f"Sexo: {dict_pacientes[cpf][2]}")
        print(f"Plano de Saúde: {dict_pacientes[cpf][3]}")
        print(f"Emails:")
        if len(dict_pacientes[cpf][4]) == 0: 
            print(f"\t- Não há e-mails cadastrados")
        else:
            for email in dict_pacientes[cpf][4]:
                print(f"\t- {email}")
        print("Telefones:")
        for telefone in dict_pacientes[cpf][5]:
                print(f"\t- {telefone}")
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves):
    if chave_existe_no_dicionario(dict_consultas, tupla_chaves):

        nome_profissional = dict_medicina[tupla_chaves[0]][0]
        nome_paciente = dict_pacientes[tupla_chaves[1]][0]

        print(f"Profissional: {nome_profissional} - CRM: {tupla_chaves[0]}")
        print(f"Paciente: {nome_paciente} - CPF: {tupla_chaves[1]}")
        print(f"Data: {tupla_chaves[2]} às {tupla_chaves[3]}")
        print(f"Diagnóstico: {dict_consultas[tupla_chaves][0]}")

        medicamentos = dict_consultas[tupla_chaves][1]
        posologias = dict_consultas[tupla_chaves][2]

        print("Medicamentos e posologias:")
        for i in range(len(medicamentos)):
            print(f"\t- {medicamentos[i]} - {posologias[i]}")
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def cadastrar_profissional_medicina(dict_medicina, caminho_arquivo):
    profissional = []
    lista_emails_profissional = []
    lista_telefones_profissional = []
    crm = input("Digite o CRM do profissional: ")

    if chave_existe_no_dicionario(dict_medicina, crm): 
        return False
    else:
        profissional.append(input("Digite o nome: "))
        profissional.append(input("Digite a data de nascimento (Formato: DD-MM-AAAA): "))
        profissional.append(input("Digite o sexo (Masculino, Feminino ou Não-binário): "))
        profissional.append(input("Digite a especialidade (Ex: Cardiologia): "))
        profissional.append(input("Digite a universidade de formação (Ex: UFSCar): "))
        adicionar_email(lista_emails_profissional)
        profissional.append(lista_emails_profissional) 
        adicionar_telefone(lista_telefones_profissional)
        profissional.append(lista_telefones_profissional) 

        dict_medicina[crm] = profissional
        salvar_dicionario_no_arquivo(dict_medicina, caminho_arquivo)
        return True
    
#--------------------------------------------------------------------------------------------
def cadastrar_paciente(dict_pacientes, caminho_arquivo): 
    paciente = []
    lista_emails_paciente = []
    lista_telefones_paciente = []
    cpf = input("Digite o CPF do paciente: ")
    
    if chave_existe_no_dicionario(dict_pacientes, cpf):
        return False
    else:
        paciente.append(input("Digite o nome: "))
        paciente.append(input("Digite a data de nascimento (Formato: DD-MM-AAAA): "))
        paciente.append(input("Digite o sexo (Masculino, Feminino ou Não-binário): "))
        paciente.append(input("Digite o Plano de Saúde (Ex: Unimed): "))
        adicionar_email(lista_emails_paciente)
        paciente.append(lista_emails_paciente)
        adicionar_telefone(lista_telefones_paciente)
        paciente.append(lista_telefones_paciente)

        dict_pacientes[cpf] = paciente
        salvar_dicionario_no_arquivo(dict_pacientes, caminho_arquivo)
        return True
        
#--------------------------------------------------------------------------------------------
def cadastrar_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    consulta = []
    lista_medicamentos = []
    lista_posologias = []

    tupla_chaves = criar_tupla_de_chaves()
    crm, cpf = tupla_chaves[:2]

    if not chave_existe_no_dicionario(dict_medicina, crm):
        return "falha_crm"
    elif not chave_existe_no_dicionario(dict_pacientes, cpf):
        return "falha_cpf"
    else:
        if chave_existe_no_dicionario(dict_consultas, tupla_chaves):
            return "falha_cadastro"
        else:
            if pode_agendar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves):
                consulta.append(input("Digite o diagnóstico do paciente: "))

                adicionar_medicamentos_e_posologias(lista_medicamentos, lista_posologias)
                consulta.append(lista_medicamentos)
                consulta.append(lista_posologias)

                dict_consultas[tupla_chaves] = consulta
                salvar_dicionario_no_arquivo(dict_consultas, caminho_arquivo)
                return "concluido"
            else:
                return "conflito"

#--------------------------------------------------------------------------------------------

# Verifica se existe conflito de horário na hora do cadastro de consulta. 
# Impede que uma consulta com o mesmo CPF ou CRM seja marcada para uma mesma
# data e hora já existente. Ou seja, o mesmo paciente (ou medico) não pode ter
# duas consultas no mesmo dia e no mesmo horário.
def pode_agendar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves):
    crm, cpf, data_consulta, hora_consulta = tupla_chaves

    for tupla in dict_consultas:
        crm_existente, cpf_existente, data_existente, hora_existente = tupla

        if (crm == crm_existente or cpf == cpf_existente) and data_consulta == data_existente and hora_consulta == hora_existente:
            if crm == crm_existente:
                print()
                print("Atenção! Já existe uma consulta com este profissional neste dia e horário: ")
                pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla)

            elif cpf == cpf_existente:
                print()
                print("Atenção! Já existe uma consulta com este paciente neste dia e horário: ")
                pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla)
            return False
    return True

#--------------------------------------------------------------------------------------------
def alterar_profissional_medicina(dict_medicina, caminho_arquivo): 
    crm = input("Digite o CRM: ")

    if chave_existe_no_dicionario(dict_medicina, crm): 
        print()
        print("------------ Informações atuais ------------" )
        pesquisar_profissional_medicina(dict_medicina, crm) 

        print()
        print("*************** Alteração dos dados ***************")
        
        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") 
        if nome != "": 
            dict_medicina[crm][0] = nome
            print("Nome alterado.")
            print()

        else: 
            print("Nome mantido.")
            print()

        nascimento = input("Digite a nova data de nascimento (Formato: DD-MM-AAAA) (ou pressione Enter para manter o atual): ")
        if nascimento != "":
            dict_medicina[crm][1] = nascimento
            print("Data de nascimento alterada.")
            print()
        else:
            print("Data de nascimento mantida.")
            print()

        sexo = input("Digite o novo sexo (ou pressione Enter para manter o atual): ")
        if sexo != "":
            dict_medicina[crm][2] = sexo
            print("Sexo alterado.")
            print()
        else:
            print("Sexo mantido.")
            print()

        especialidade = input("Digite a nova especialidade (ou pressione Enter para manter o atual): ")
        if especialidade != "":
            dict_medicina[crm][3] = especialidade
            print("Especialidade alterada.")
            print()
        else:
            print("Especialidade mantida.")
            print()

        universidade = input("Digite a nova universidade (ou pressione Enter para manter o atual): ")
        if universidade != "":
            dict_medicina[crm][4] = universidade
            print("Universidade alterada.")
            print()
        else:
            print("Universidade mantida.")
            print()

        if alterar_emails(dict_medicina, crm, 5):
            print("E-mail(s) alterado(s).")
            print()
        else:
            print("E-mail(s) mantido(s).")
            print()

        if alterar_telefones(dict_medicina, crm, 6):
            print("Telefone(s) alterado(s).")
            print()
        else:
            print("Telefone(s) mantido(s).")
            print()
        
        salvar_dicionario_no_arquivo(dict_medicina, caminho_arquivo)
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def alterar_paciente(dict_pacientes, caminho_arquivo): 
    cpf = input("Digite o CPF: ")

    if chave_existe_no_dicionario(dict_pacientes, cpf): 
        print()
        print("------------ Informações atuais ------------" )
        pesquisar_paciente(dict_pacientes, cpf) 

        print()
        print("*************** Alteração dos dados ***************")

        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") 
        if nome != "": 
            dict_pacientes[cpf][0] = nome
            print("Nome alterado.")
            print()

        else: 
            print("Nome mantido.")
            print()

        nascimento = input("Digite a nova data de nascimento (Formato: DD-MM-AAAA) (ou pressione Enter para manter o atual): ")
        if nascimento != "":
            dict_pacientes[cpf][1] = nascimento
            print("Data de nascimento alterada.")
            print()
        else:
            print("Data de nascimento mantida.")
            print()

        sexo = input("Digite o novo sexo (ou pressione Enter para manter o atual): ")
        if sexo != "":
            dict_pacientes[cpf][2] = sexo
            print("Sexo alterado.")
            print()
        else:
            print("Sexo mantido.")
            print()

        plano = input("Digite o novo Plano de Saúde (Ex: Unimed) (ou pressione Enter para manter o atual): ")
        if plano != "":
            dict_pacientes[cpf][3] = plano
            print("Plano de Saúde alterado.")
            print()
        else:
            print("Plano de Saúde mantido.")
            print()
            
        if alterar_emails(dict_pacientes, cpf, 4):
            print("E-mail(s) alterado(s).")
            print()
        else:
            print("E-mail(s) mantido(s).")
            print()

        if alterar_telefones(dict_pacientes, cpf, 5):
            print("Telefone(s) alterado(s).")
            print()
        else:
            print("Telefone(s) mantido(s).")
            print()
        
        salvar_dicionario_no_arquivo(dict_pacientes, caminho_arquivo)
        return True
    
    else:
        return False

#--------------------------------------------------------------------------------------------
def alterar_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    tupla_chaves = criar_tupla_de_chaves()
    crm, cpf, data_da_consulta, hora_da_consulta = tupla_chaves
    nova_tupla = ()

    if chave_existe_no_dicionario(dict_consultas, tupla_chaves):
        print()
        print("------------ Informações atuais ------------" )
        pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves)

        print()
        crm = input("Digite o novo CRM (ou pressione Enter para manter o atual): ")
        if crm != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("CRM alterado.")
            print()

        else: 
            crm = tupla_chaves[0]
            print("CRM mantido.")
            print()

        cpf = input("Digite o novo CPF (Somente números) (ou pressione Enter para manter o atual): ")
        if cpf != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("CPF alterado.")
            print()

        else: 
            cpf = tupla_chaves[1]
            print("CPF mantido.")
            print()

        data_da_consulta = input("Digite a nova data da consulta (Formato: DD-MM-AAAA) (ou pressione Enter para manter a atual): ")
        if data_da_consulta != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("Data da consulta alterada.")
            print()

        else: 
            data_da_consulta = tupla_chaves[2]
            print("Data da consulta mantida.")
            print()
        
        hora_da_consulta = input("Digite a nova hora da consulta (Formato 24h: 07h00; 19h00) (ou pressione Enter para manter a atual): ")
        if hora_da_consulta != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("Hora da consulta alterada.")
            print()

        else: 
            hora_da_consulta = tupla_chaves[3]
            print("Hora da consulta mantida.")
            print()

        dict_consultas[nova_tupla] = dict_consultas[tupla_chaves]
        del dict_consultas[tupla_chaves]

        diagnostico = input("Digite o novo diagnóstico (Ex: Hipertensão) (ou pressione Enter para manter o atual): ")
        if diagnostico != "":
            dict_consultas[nova_tupla][0] = diagnostico
            print("Diagnóstico alterado.")
            print()
        else:
            print("Diagnóstico mantido.")
            print()

        if alterar_medicamentos_e_posologias(dict_consultas, nova_tupla):
            print("Medicamento(s) e posologia(s) alterado(s).")
            print()
        else:
            print("Medicamento(s) e posologia(s) mantido(s).")
            print()

        salvar_dicionario_no_arquivo(dict_consultas,caminho_arquivo)
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def excluir_profissional_medicina(dict_medicina, caminho_arquivo):
    crm = input("Digite o CRM: ")

    if chave_existe_no_dicionario(dict_medicina, crm):
        print("------------ Profissional encontrado ------------")
        pesquisar_profissional_medicina(dict_medicina, crm)

        print()
        confirmar = input("Tem certeza que deseja excluir este profissional? Os dados não poderão ser recuperados.\nDigite 'Confirmar' para excluir ou 'Cancelar' para manter os dados: ")

        if confirmar.lower() == 'confirmar':
            del dict_medicina[crm]
            salvar_dicionario_no_arquivo(dict_medicina, caminho_arquivo)
            return "confirmado" 
        
        elif confirmar.lower() == 'cancelar':
            return "cancelado"

        else:
            return "erro"
    else:
        return "falha"

#--------------------------------------------------------------------------------------------
def excluir_paciente(dict_pacientes, caminho_arquivo):
    cpf = input("Digite o CPF: ")

    if chave_existe_no_dicionario(dict_pacientes, cpf):
        print("------------ Paciente encontrado ------------")
        pesquisar_paciente(dict_pacientes, cpf)

        print()
        confirmar = input("Tem certeza que deseja excluir este paciente? Os dados não poderão ser recuperados.\nDigite 'Confirmar' para excluir ou 'Cancelar' para manter os dados: ")

        if confirmar.lower() == 'confirmar':
            del dict_pacientes[cpf]
            salvar_dicionario_no_arquivo(dict_pacientes,caminho_arquivo)
            return "confirmado" 
        
        elif confirmar.lower() == 'cancelar':
            return "cancelado"
        
        else:
            return "erro" 
    else:
        return "falha"
    
#--------------------------------------------------------------------------------------------
def excluir_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    tupla_chaves = criar_tupla_de_chaves()

    if chave_existe_no_dicionario(dict_consultas, tupla_chaves):
        print("------------ Consulta encontrada ------------")
        pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves)

        print()
        confirmar = input("Tem certeza que deseja excluir esta consulta? Os dados não poderão ser recuperados.\nDigite 'Confirmar' para excluir ou 'Cancelar' para manter os dados: ")

        if confirmar.lower() == 'confirmar':
            del dict_consultas[tupla_chaves]
            salvar_dicionario_no_arquivo(dict_consultas, caminho_arquivo)
            return "confirmado"
        
        elif confirmar.lower() == "cancelar":
            return "cancelado"
        
        else:
            return "erro"
    else:
        return "falha"
    
#############################################################################################
#### Relatórios =============================================================================
#############################################################################################
def gerar_relatorio_medicos_por_especialidade(dict_medicina, especialidade):
    _, data, hora = obter_datetime_agora_data_e_hora()
    nome_relatorio = f"REL_ESP_{especialidade}_-_{data}_às_{hora}.txt"
    diretorio_atual = os.getcwd()
    caminho_relatorio = os.path.join(diretorio_atual, nome_relatorio)

    chaves = []
    for crm, valor in dict_medicina.items():
        if especialidade in valor:
            chaves.append(crm)
    
    if len(chaves) > 0:
        relatorio = open(caminho_relatorio, 'w')
        relatorio.write(f"=================================================================\n")
        relatorio.write(f"Relatório de profissionais de medicina\n")
        relatorio.write(f"Especialidade: {especialidade}\n")
        relatorio.write(f"Gerado dia {data} às {hora}.\n")
        relatorio.write(f"=================================================================\n")

        for crm in chaves:
            relatorio.write(f"CRM: {crm}\n")
            relatorio.write(f"Nome: {dict_medicina[crm][0]}\n")
            relatorio.write(f"Data de nascimento: {dict_medicina[crm][1]}\n")
            relatorio.write(f"Sexo: {dict_medicina[crm][2]}\n")
            relatorio.write(f"Universidade de formação: {dict_medicina[crm][4]}\n")
            
            relatorio.write(f"E-mails:\n")
            for email in dict_medicina[crm][5]:
                relatorio.write(f"\t- {email}\n")
            
            relatorio.write(f"Telefones:\n")
            for telefone in dict_medicina[crm][6]:
                relatorio.write(f"\t- {telefone}\n")
            relatorio.write("-------------------------------------------------------------------\n")
        print()
        print(f"Gerando relatório em {caminho_relatorio}")
        relatorio.close()
        return True
    else:
        print()
        print(f"Não existem médicos cadastrados com a especialidade {especialidade}.")
        return False

#--------------------------------------------------------------------------------------------
def gerar_relatorio_paciente_por_idade(dict_pacientes, idade_maxima):
    agora, data, hora = obter_datetime_agora_data_e_hora()
    nome_relatorio = f"REL_PAC_até_{idade_maxima}_anos_-_{data}_as_{hora}.txt"
    diretorio_atual = os.getcwd()
    caminho_relatorio = os.path.join(diretorio_atual, nome_relatorio)

    chaves = []
    for cpf in dict_pacientes:
        idade_paciente = calcular_idade(dict_pacientes, cpf, agora)
        if idade_paciente <= idade_maxima:
            chaves.append(cpf)

    if len(chaves) > 0:
        relatorio = open(caminho_relatorio, 'w')
        relatorio.write(f"=================================================================\n")
        relatorio.write(f"Relatório de Pacientes por idade\n")
        relatorio.write(f"Idade máxima: {idade_maxima}\n")
        relatorio.write(f"Gerado dia {data} às {hora}.\n")
        relatorio.write(f"=================================================================\n")

        for cpf in chaves:
            relatorio.write(f"CPF: {cpf}\n")
            relatorio.write(f"Nome: {dict_pacientes[cpf][0]}\n")
            relatorio.write(f"Data de nascimento: {dict_pacientes[cpf][1]}\n")
            relatorio.write(f"Idade: {calcular_idade(dict_pacientes, cpf, agora)}\n")
            relatorio.write(f"Sexo: {dict_pacientes[cpf][2]}\n")
            relatorio.write(f"Plano de Saúde: {dict_pacientes[cpf][3]}\n")
            
            relatorio.write(f"E-mails:\n")
            for email in dict_pacientes[cpf][4]:
                relatorio.write(f"\t- {email}\n")
            
            relatorio.write(f"Telefones:\n")
            for telefone in dict_pacientes[cpf][5]:
                relatorio.write(f"\t- {telefone}\n")
            relatorio.write("-------------------------------------------------------------------\n")
        print()
        print(f"Gerando relatório em {caminho_relatorio}")
        relatorio.close()
        return True
    else: 
        print()
        print(f"Não existem pacientes menores que {idade_maxima} anos.")
        return False

#--------------------------------------------------------------------------------------------
def gerar_relatorio_consultas_ultimos_dias(dict_consultas, dict_medicina, dict_pacientes, numero_dias):
    from datetime import datetime, timedelta
    agora, data, hora = obter_datetime_agora_data_e_hora()
    nome_relatorio = f"REL_CONS_Ultimos_{numero_dias}_dias_-_{data}_às_{hora}.txt"
    diretorio_atual = os.getcwd()
    caminho_relatorio = os.path.join(diretorio_atual, nome_relatorio)

    data_limite = agora - timedelta(days=numero_dias)
    data_agora = datetime.strptime(data, '%d-%m-%Y')

    chaves = []
    for tupla_chaves in dict_consultas:
        data_da_consulta = datetime.strptime(tupla_chaves[2], '%d-%m-%Y')
        if data_da_consulta >= data_limite and data_da_consulta <= data_agora:
            chaves.append(tupla_chaves)

    if len(chaves) > 0:
        relatorio = open(caminho_relatorio, 'w')
        relatorio.write(f"=================================================================\n")
        relatorio.write(f"Relatório de Consultas nos últimos {numero_dias} dia(s). \n")
        relatorio.write(f"Gerado dia {data} às {hora}.\n")
        relatorio.write(f"=================================================================\n")

        for tupla_chaves in chaves:
            relatorio.write(f"Profissional: {dict_medicina[tupla_chaves[0]][0]} - CRM: {tupla_chaves[0]}\n")
            relatorio.write(f"Paciente: {dict_pacientes[tupla_chaves[1]][0]} - CPF: {tupla_chaves[1]}\n")
            relatorio.write(f"Data da consulta: {tupla_chaves[2]}\n")
            relatorio.write(f"Hora da consulta: {tupla_chaves[3]}\n")
            relatorio.write(f"Diagnóstico: {dict_consultas[tupla_chaves][0]}\n")
            lista_medicamentos = dict_consultas[tupla_chaves][1]
            lista_posologias = dict_consultas[tupla_chaves][2]
            relatorio.write(f"Medicamentos e posologias:\n")
            for i in range(len(lista_medicamentos)):
                relatorio.write(f"\t- {lista_medicamentos[i]} - {lista_posologias[i]}\n")
            relatorio.write("-------------------------------------------------------------------\n")
        print()
        print(f"Gerando relatório em {caminho_relatorio}")
        return True
    else: #caso não encontre nenhum só passa a mensagem que não existem pacientes
        print()
        print(f"Não existem consultas cadastradas nos últimos {numero_dias} dias.")
        return False


#############################################################################################
#### Funções de arquivo =====================================================================
#############################################################################################
def arquivo_existe(nome_arquivo):
    return os.path.isfile(nome_arquivo) 

#--------------------------------------------------------------------------------------------
def criar_arquivo(caminho_arquivo):
    print()
    print(f"O arquivo {caminho_arquivo[2:]} não foi encontrado neste diretório. Será criado um novo arquivo no diretório atual.")
    arquivo = open(caminho_arquivo, 'w')
    arquivo.close()

#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_medicina(dicionario, caminho_arquivo):
    arquivo_medicina = open(caminho_arquivo, 'r')

    for linha in arquivo_medicina:
        linha = linha.strip() 

        chave, valor = linha.split(": ", 1) 

        elementos_do_valor = valor.split(", ") 

        emails = elementos_do_valor[5]
        if emails != "[]":
            emails = emails[1:-1].strip().split("; ")
        else:
            emails = []

        telefones = elementos_do_valor[6]
        telefones = telefones[1:-1].strip().split("; ")

        dicionario[chave] = elementos_do_valor[:5] + [emails] + [telefones]
    arquivo_medicina.close()

#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_pacientes(dicionario, caminho_arquivo):
    arquivo_paciente = open(caminho_arquivo, 'r')

    for linha in arquivo_paciente:
        linha = linha.strip()

        chave,valor = linha.split(": ", 1)

        elementos_do_valor = valor.split(", ")

        emails = elementos_do_valor[4]
        if emails != "[]":
            emails = emails[1:-1].strip().split("; ")
        else:
            emails = []

        telefones=elementos_do_valor[5]
        telefones=telefones[1:-1].strip().split("; ")

        dicionario[chave] = elementos_do_valor[:4] + [emails] + [telefones]
    arquivo_paciente.close()

#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_consultas(dicionario, caminho_arquivo):
    arquivo_consultas = open(caminho_arquivo, 'r')

    for linha in arquivo_consultas:
        linha = linha.strip() 
        chaves, valor = linha.split(": ", 1) 
        chaves = chaves.strip('()')

        valores_chaves = chaves.split(", ")

        lista_chaves = []
        for elem in valores_chaves:
            lista_chaves.append(elem.strip("'"))
        tupla_chaves = tuple(lista_chaves)
        
        elementos_do_valor = valor.split(", ") 

        medicamentos = elementos_do_valor[1] 
        medicamentos = medicamentos[1:-1].strip().split("; ") 

        posologias = elementos_do_valor[2]
        posologias = posologias[1:-1].strip().split("; ")

        dicionario[tupla_chaves] = elementos_do_valor[:1] + [medicamentos] + [posologias]
    arquivo_consultas.close()

#--------------------------------------------------------------------------------------------
def salvar_dicionario_no_arquivo(dicionario, caminho_arquivo):
    arquivo = open(caminho_arquivo, 'w')

    for chave, valor in dicionario.items():
        linha = ""
        linha = f"{chave}: "
        for i in range(len(valor)):

            if str(valor[i]).startswith('[') and str(valor[i]).endswith(']'):
                linha += "["
                for j in range(len(valor[i])):
                    if j == (len(valor[i])-1) or len(valor[i]) == 1:
                        linha += f"{valor[i][j]}"
                    else:
                        linha += f"{valor[i][j]}; "
                linha += "], "
            else:
                linha += f"{valor[i]}, "
        if linha.endswith(', '):
            linha = linha.rstrip(', ') + f"\n"

        arquivo.write(linha)
    arquivo.close()

#############################################################################################
#### Main ===================================================================================
#############################################################################################
def main():
    Medicina = {}
    caminho_arquivo_medicina = './profissionais_medicina.txt'
    Pacientes = {}
    caminho_arquivo_pacientes = './pacientes.txt'
    Consultas = {}
    caminho_arquivo_consultas = './consultas.txt'

    opcao_menu = 1
    while opcao_menu!=5:
        opcao_menu = menu_principal()
        opcao_submenu = 0 # inicializada para entrar no 'while' em cada opção

        if opcao_menu == 1:

            if not arquivo_existe(caminho_arquivo_medicina):
                criar_arquivo(caminho_arquivo_medicina)

            pegar_dados_do_arquivo_medicina(Medicina, caminho_arquivo_medicina)

            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu = submenu_medicina()

                if opcao_submenu == 1:
                    print()
                    print("************ Profissionais de Medicina *************")

                    if not mostrar_todos_os_profissionais(Medicina): 
                        print(f"\n---------------------------------------------------")
                        print("Não há profissionais de medicina cadastrados ainda.")
                        print("---------------------------------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n********** Pesquisar profissional de medicina *********** ")
                    crm = input("Digite o CRM do profissional: ")

                    print(f"\n****************** Resultado da busca ******************* ")

                    if not pesquisar_profissional_medicina(Medicina, crm):
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
                        print("--------------------------------------------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n********** Cadastrar profissional de medicina ***********")

                    if cadastrar_profissional_medicina(Medicina, caminho_arquivo_medicina): 
                        print(f"\n------------------------------------")
                        print("Profissional cadastrado com sucesso!")
                        print("------------------------------------")

                    else:
                        print(f"\n---------------------------------------")
                        print("Já existe um profissional com este CRM.")
                        print("---------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 4:
                    print(f"\n************ Alterar cadastro profissional *************")

                    if alterar_profissional_medicina(Medicina, caminho_arquivo_medicina): 
                        print(f"\n------------------------------------")
                        print("Profissional alterado com sucesso!")
                        print("------------------------------------")

                    else:
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
                        print("--------------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 5:
                    print(f"\n************ Excluir cadastro profissional *************")
                    retorno = excluir_profissional_medicina(Medicina, caminho_arquivo_medicina)

                    if  retorno == "confirmado": 
                        print(f"\n----------------------------------")
                        print("Profissional excluído com sucesso!")
                        print("----------------------------------")

                    elif retorno == "cancelado":
                        print(f"\n----------------------------------------------------")
                        print("Procedimento cancelado pelo usuário. Dados mantidos.")
                        print("----------------------------------------------------")

                    elif retorno == "erro":
                        print(f"\n--------------------------------------------------")
                        print("Erro! Confirmação não reconhecida. Tente novamente")
                        print("--------------------------------------------------")

                    else:
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
                        print("--------------------------------------------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 6:
                    print()
                    print("Retornando ao menu principal...")

                elif opcao_submenu == 7:
                    msg_encerrado()
                    opcao_menu = 5
           
        elif opcao_menu == 2:
            if not arquivo_existe(caminho_arquivo_pacientes):
                criar_arquivo(caminho_arquivo_pacientes)
            
            pegar_dados_do_arquivo_pacientes(Pacientes, caminho_arquivo_pacientes)

            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu=submenu_pacientes()

                if opcao_submenu==1:
                    print()
                    print(("******************* Pacientes ********************"))
                    if not mostrar_todos_os_pacientes(Pacientes):
                        print(f"\n-----------------------------------")
                        print("Não há pacientes cadastrados ainda.")
                        print("-----------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n****************** Pesquisar paciente ******************* ")
                    cpf = input("Digite o CPF do paciente: ")
                    
                    print(f"\n****************** Resultado da busca ******************* ") 
                    if not pesquisar_paciente(Pacientes, cpf):
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente")
                        print("----------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n***************** Cadastrar paciente ******************")
                    if cadastrar_paciente(Pacientes,caminho_arquivo_pacientes):
                        print(f"\n--------------------------------")
                        print("Paciente cadastrado com sucesso!")
                        print("--------------------------------")
                    else:
                        print(f"\n-----------------------------------")
                        print("Já existe um paciente com este CPF.")
                        print("-----------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 4:
                    print(f"\n************ Alterar cadastro de paciente *************")
                    if alterar_paciente(Pacientes,caminho_arquivo_pacientes):
                        print(f"\n--------------------------------")
                        print("Paciente adicionado com sucesso!")
                        print("--------------------------------")
                    else:
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente")
                        print("----------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 5:
                    print(f"\n************ Excluir cadastro de paciente *************")
                    retorno = excluir_paciente(Pacientes, caminho_arquivo_pacientes)

                    if  retorno == "confirmado": 
                        print(f"\n------------------------------")
                        print("Paciente excluído com sucesso!")
                        print("------------------------------")

                    elif retorno == "cancelado":
                        print(f"\n----------------------------------------------------")
                        print("Procedimento cancelado pelo usuário. Dados mantidos.")
                        print("----------------------------------------------------")

                    elif retorno == "erro":
                        print(f"\n--------------------------------------------------")
                        print("Erro! Confirmação não reconhecida. Tente novamente")
                        print("--------------------------------------------------")

                    else:
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente")
                        print("----------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 6:
                    print()
                    print("Retornando ao menu principal...")

                elif opcao_submenu == 7:
                    msg_encerrado()
                    opcao_menu = 5
                    
        elif opcao_menu == 3:
            if not arquivo_existe(caminho_arquivo_consultas):
                criar_arquivo(caminho_arquivo_consultas)
            
            if not arquivo_existe(caminho_arquivo_medicina):
                criar_arquivo(caminho_arquivo_medicina)
            
            if not arquivo_existe(caminho_arquivo_pacientes):
                criar_arquivo(caminho_arquivo_pacientes)

            pegar_dados_do_arquivo_medicina(Medicina, caminho_arquivo_medicina)
            pegar_dados_do_arquivo_pacientes(Pacientes, caminho_arquivo_pacientes)
            pegar_dados_do_arquivo_consultas(Consultas, caminho_arquivo_consultas)

            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu = submenu_consultas()

                if opcao_submenu == 1:
                    print()
                    print("******************* Consultas ********************")
                    if not mostrar_todas_as_consultas(Consultas, Medicina, Pacientes): 
                        print(f"\n------------------------------------")
                        print("Não há consultas cadastradas ainda.")
                        print("------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n****************** Pesquisar consulta ******************* ")
                    tupla_chaves = criar_tupla_de_chaves()

                    print(f"\n****************** Resultado da busca ******************* ")
                    if not pesquisar_consulta(Consultas, Medicina, Pacientes, tupla_chaves):
                        print(f"\n-------------------------------------------------------------")
                        print("Consulta não encontrada. Verifique os dados e tente novamente")
                        print("-------------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n****************** Adicionar consulta *******************")
                    retorno = cadastrar_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas)

                    if retorno == "concluido": 
                        print(f"\n------------------------------------")
                        print("Consulta adicionada com sucesso!")
                        print("------------------------------------")

                    elif retorno == "falha_cadastro":
                        print(f"\n--------------------------------------------------------------")
                        print("Já existe uma consulta cadastrada com as informações passadas.")
                        print("--------------------------------------------------------------")

                    elif retorno == "falha_crm":
                        print(f"\n-----------------------------------------------------------------------------------")
                        print("Atenção! Não foi encontrado profissional com este CRM. Verifique e tente novamente.")
                        print("-----------------------------------------------------------------------------------")

                    elif retorno == "falha_cpf":
                        print(f"\n-------------------------------------------------------------------------------")
                        print("Atenção! Não foi encontrado paciente com este CPF. Verifique e tente novamente.")
                        print("-------------------------------------------------------------------------------")

                    elif retorno == "conflito":
                        print(f"\n---------------------------------------------------")
                        print("Altere o dia ou o horário para resolver o conflito.")
                        print("---------------------------------------------------")
                    else:
                        print(f"\n------------------")
                        print("Erro desconhecido.")
                        print("------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 4:
                    print(f"\n************ Alterar cadastro consulta *************")
                    if alterar_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas):
                        print(f"\n------------------------------")
                        print("Consulta alterada com sucesso!")
                        print("------------------------------")
                    else:
                        print(f"\n-------------------------------------------------------------")
                        print("Consulta não encontrada. Verifique os dados e tente novamente")
                        print("-------------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 5:
                    print(f"\n************ Excluir cadastro de consulta *************")
                    retorno = excluir_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas)

                    if  retorno == "confirmado": 
                        print(f"\n------------------------------")
                        print("Consulta excluída com sucesso!")
                        print("------------------------------")

                    elif retorno == "cancelado":
                        print(f"\n----------------------------------------------------")
                        print("Procedimento cancelado pelo usuário. Dados mantidos.")
                        print("----------------------------------------------------")

                    elif retorno == "erro":
                        print(f"\n--------------------------------------------------")
                        print("Erro! Confirmação não reconhecida. Tente novamente.")
                        print("--------------------------------------------------")

                    else:
                        print(f"\n-------------------------------------------------------------")
                        print("Consulta não encontrada. Verifique os dados e tente novamente")
                        print("-------------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 6:
                    print()
                    print("Retornando ao menu principal...") # FUNCIONANDO

                elif opcao_submenu == 7:
                    msg_encerrado()
                    opcao_menu = 5
            
        elif opcao_menu == 4:
            if not arquivo_existe(caminho_arquivo_consultas):
                criar_arquivo(caminho_arquivo_consultas)
            
            if not arquivo_existe(caminho_arquivo_medicina):
                criar_arquivo(caminho_arquivo_medicina)
            
            if not arquivo_existe(caminho_arquivo_pacientes):
                criar_arquivo(caminho_arquivo_pacientes)

            pegar_dados_do_arquivo_medicina(Medicina, caminho_arquivo_medicina)
            pegar_dados_do_arquivo_pacientes(Pacientes, caminho_arquivo_pacientes)
            pegar_dados_do_arquivo_consultas(Consultas, caminho_arquivo_consultas)

            while opcao_submenu != 4 and opcao_submenu != 5:
                opcao_submenu = submenu_relatorios()

                if opcao_submenu == 1:
                    print("******** Gerar relatório de profissionais por especialidade ********")
                    especialidade = input("Digite a especialidade para gerar relatório: ")

                    if gerar_relatorio_medicos_por_especialidade(Medicina, especialidade):
                        print(f"\n-----------------------------")
                        print("Relatório gerado com sucesso.")
                        print("-----------------------------")
                    else:
                        print(f"\n---------------------------")
                        print("O relatório não foi gerado.")
                        print("---------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print("******** Gerar relatório de pacientes por idade ********")
                    idade_maxima = ""
                    while not isinstance(idade_maxima, int):
                        idade_maxima = input("Digite uma idade máxima válida para gerar um relatório: ")
                        if idade_maxima.isdigit():
                            idade_maxima = int(idade_maxima)
                        else:
                            print("Digite uma idade válida. Somente número inteiro maior que zero.")
                    
                    if gerar_relatorio_paciente_por_idade(Pacientes, idade_maxima):
                        print(f"\n-----------------------------")
                        print("Relatório gerado com sucesso.")
                        print("-----------------------------")
                    else:
                        print(f"\n---------------------------")
                        print("O relatório não foi gerado.")
                        print("---------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")
                    
                elif opcao_submenu == 3:
                    print("******** Gerar relatório de Consultas dos últimos dias ********")
                    numero_dias = ""
                    while not isinstance(numero_dias, int):
                        numero_dias = input("Digite um número de dias válido para buscar as consultas: ")
                        if numero_dias.isdigit():
                            numero_dias = int(numero_dias)
                        else:
                            print("Digite um número de dias válido. Somente número inteiro maior que zero.")

                    if gerar_relatorio_consultas_ultimos_dias(Consultas, Medicina, Pacientes, numero_dias):
                        print(f"\n-----------------------------")
                        print("Relatório gerado com sucesso.")
                        print("-----------------------------")
                    else:
                        print(f"\n---------------------------")
                        print("O relatório não foi gerado.")
                        print("---------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")
                
                elif opcao_submenu == 4:
                    print()
                    print("Retornando ao menu principal...")

                elif opcao_submenu == 5:
                    msg_encerrado()
                    opcao_menu = 5

        elif opcao_menu == 5:
            msg_encerrado()
        
        else:
            print("Erro desconhecido.")

#############################################################################################
#### Programa principal =====================================================================
#############################################################################################
main()