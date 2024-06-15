#############################################################################################
#### Repetições =============================================================================
#############################################################################################
def verifica_escolha_do_usuario(numero_de_opcoes): # max é o número de escolhas dos menus
    while True: 
        entrada = input("Digite a opção escolhida: ")
        
        if entrada.isdigit():
            opcao = int(entrada)
            if opcao >= 1  and opcao <= numero_de_opcoes: 
                return opcao
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
def chave_existe_no_dicionario(dicionario, chave): # chave vem como crm, cpf ou tupla(crm, cpf, data, hora)
    if chave in dicionario:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def criar_tupla_chaves():
    crm = input("Digite o CRM do profissional: ")
    cpf = input("Digite o CPF do paciente (Somente números): ")
    data_da_consulta = input("Digite a data da consulta (DD/MM/AAAA): ")
    hora_da_consulta =  input("Digite a hora da consulta (Formato: 9:00, 15:30): ")
    tupla_chaves = (crm, cpf, data_da_consulta, hora_da_consulta)
    return tupla_chaves

#--------------------------------------------------------------------------------------------
def adicionar_email(lista): 
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

#--------------------------------------------------------------------------------------------
def adicionar_telefone(lista): 
        telefone = "0"
        print("Iniciada repetição para adicionar telefones (Formato (00)00000-0000)")
        while telefone != "":
            telefone = input("Digite um telefone (ou pressione Enter para terminar): ")
            if telefone != "":
                lista.append(telefone.replace(" ", "")) # remove todos os espaços em branco
            else:
                if len(lista) == 0:
                    print()
                    print("Atenção! É obrigatório ao menos 1(um) telefone para contato.")
                    print()
                    telefone = "0"

#--------------------------------------------------------------------------------------------
def adicionar_medicamentos_e_posologias(lista_medicamentos, lista_posologias):
    medicamento = "vazio"
    posologia = "vazio"
    while medicamento != "":
        medicamento = input("Digite um medicamento indicado (Formato: Losartana 50mg) (ou pressione Enter para terminar): ")
        if medicamento == "" and len(lista_medicamentos) == 0:
            print()
            print(f"Atenção! É necessário acrescentar um medicamento.")
            print()
        else:
            if medicamento != "":
                lista_medicamentos.append(medicamento)
                posologia = input(f"Digite a posologia para {medicamento} (Formatos: 1x dia; 8h/8h): ")
                if posologia == "" and medicamento != "":
                    print()
                    print(f"Atenção! É necessário acrescentar uma posologia ao medicamento {medicamento}.")
                else:
                    lista_posologias.append(posologia)

#--------------------------------------------------------------------------------------------
def alterar_emails(dicionario, chave): # chave pode ser crm ou cpf
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os e-mails;")
    print("2. Alterar um e-mail existente;")
    print("3. Adicionar um ou mais novos e-mails;")
    print("4. Excluir e-mail existente;")
    print("5. Manter e-mail(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        emails = []
        adicionar_email(emails)
        dicionario[chave][5] = emails
        return True
    
    elif opcao == "2":
        i = 0

        for email in dicionario[chave][5]:
            print(f"{i} - {email}")
            i+=1

        index = int(input("Qual e-mail deseja alterar? Digite apenas o número: "))

        dicionario[chave][5][index] = input("Digite o novo e-mail: ")
        return True
    
    elif opcao == "3":
        adicionar_email(dicionario[chave][5])
        return True
    
    elif opcao == "4":
        i = 0
        for email in dicionario[chave][5]:
            print(f"{i} - {email}")
            i+=1
        index = int(input("Qual e-mail deseja excluir? Digite apenas o número: "))
        del dicionario[chave][5][index]
        return True
    
    elif opcao == "5":
        return False
    
    else:
        print(f"\nAtenção! Opção inválida.")
        return False

#--------------------------------------------------------------------------------------------
def alterar_telefones(dicionario, chave):
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os telefones;")
    print("2. Alterar um telefone existente;")
    print("3. Adicionar um ou mais novos telefones;")
    print("4. Excluir telefone existente;")
    print("5. Manter telefone(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        telefones = []
        adicionar_telefone(telefones)
        dicionario[chave][6] = telefones
        return True
    
    elif opcao == "2":
        i = 0
        for telefone in dicionario[chave][6]:
            print(f"{i} - {telefone}")
            i+=1
        escolha = int(input("Qual telefone deseja alterar? Digite apenas o número: "))
        dicionario[chave][6][escolha] = input("Digite o novo telefone (Formato: (00)00000-0000): ")
        return True
    
    elif opcao == "3":
        adicionar_telefone(dicionario[chave][6])
        return True
    
    elif opcao == "4":
        i = 0
        for telefone in dicionario[chave][6]:
            print(f"{i} - {telefone}")
            i+=1
        escolha = int(input("Qual telefone deseja excluir? Digite apenas o número: "))
        del dicionario[chave][6][escolha]
        if len(dicionario[chave][6]) == 0:
            print("Atenção! Nenhum telefone cadastrado. É obrigatório possuir pelo menos 1 telefone para contato.")
            adicionar_telefone(dicionario[chave][6])
        return True
    
    elif opcao == "5":
        return False
    
    else:
        print(f"\nAtenção! Opção inválida.")
        return False
    
#--------------------------------------------------------------------------------------------
def alterar_medicamentos(dicionario, tupla_chaves):
    opcao = ""
    print("Escolha uma opção: ")
    print("1. Alterar todos os medicamentos;")
    print("2. Alterar um medicamento existente;")
    print("3. Adicionar um ou mais novos medicamentos;")
    print("4. Excluir medicamento existente;")
    print("5. Manter medicamento(s) atual(is);")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        medicamentos = []
        posologias = []
        adicionar_medicamentos_e_posologias(medicamentos, posologias)
        dicionario[tupla_chaves][1] = medicamentos
        dicionario[tupla_chaves][2] = posologias
        return True
    
    elif opcao == "2":
        i = 0
        for medicamento in dicionario[tupla_chaves][1]:
            print(f"{i} - {medicamento}")
            i+=1
        escolha = int(input("Qual medicamento deseja alterar? Digite apenas o número: "))
        dicionario[tupla_chaves][1][escolha] = input("Digite o novo medicamento (Formato: Losartana 50mg): ")
        dicionario[tupla_chaves][2][escolha] = input("Digite a nova posologia (Formatos: 1x dia; 8h/8h): ")
        return True
    
    elif opcao == "3":
        adicionar_medicamentos_e_posologias(dicionario[tupla_chaves][1], dicionario[tupla_chaves][2])
        return True
    
    elif opcao == "4":
        i = 0
        for medicamento in dicionario[tupla_chaves][1]:
            print(f"{i} - {medicamento}")
            i+=1
        escolha = int(input("Qual medicamento deseja excluir? Digite apenas o número: "))
        del dicionario[tupla_chaves][1][escolha]
        del dicionario[tupla_chaves][2][escolha]
        if len(dicionario[tupla_chaves][6]) == 0:
            print("Atenção! Nenhum medicamento cadastrado. É obrigatório possuir pelo menos 1 medicamento.")
            adicionar_medicamentos_e_posologias(dicionario[tupla_chaves][1], dicionario[tupla_chaves][2])
        return True
    
    elif opcao == "5":
        return False
    
    else:
        print(f"\nAtenção! Opção inválida.")
        return False

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

    # chama função que contém loop de repetição com 5 opções
    return verifica_escolha_do_usuario(5)

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

    # chama função que contém loop de repetição com 7 opções    
    return verifica_escolha_do_usuario(7)

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
    
    return verifica_escolha_do_usuario(7)

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
    
    return verifica_escolha_do_usuario(7)

#--------------------------------------------------------------------------------------------
def submenu_relatorios():
    return "========================================\nRELATÓRIOS"

#############################################################################################
#### Funções Específicas ====================================================================
#############################################################################################
def mostrar_todos_os_profissionais(dicionario):
        # Para cada elemento em banco chama a função de pesquisar 1
        if len(dicionario) == 0:
            return False
        else:
            for crm in dicionario:
                pesquisar_profissional_medicina(dicionario, crm) 
                print("----------------------------------------------------")
            return True

#---------------------------------------------------------------------------------------------
def mostrar_todos_os_pacientes(dicionario):  
       if len(dicionario) == 0:
        return False
       else:
        for cpf in dicionario:
            pesquisar_paciente(dicionario, cpf)
            print("----------------------------------------------------")
        return True

#--------------------------------------------------------------------------------------------
def mostrar_todas_as_consultas(dict_consultas, dict_medicina, dict_pacientes): 
        if len(dict_consultas) == 0:
            return False
        else:
            for tupla in dict_consultas:
                pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla)
                print("----------------------------------------------------")
            return True

#--------------------------------------------------------------------------------------------
def pesquisar_profissional_medicina(dicionario, crm): 
    if chave_existe_no_dicionario(dicionario, crm):
        print(f"CRM: {crm}")
        print(f"Nome: {dicionario[crm][0]}")
        print(f"Data de nascimento: {dicionario[crm][1]}")
        print(f"Sexo: {dicionario[crm][2]}")
        print(f"Especialidade: {dicionario[crm][3]}")
        print(f"Formação: {dicionario[crm][4]}")
        print("E-mails:")
        if len(dicionario[crm][5]) == 0:
            print(f"\t- Não há e-mails cadastrados")
        else:
            for email in dicionario[crm][5]:
                print(f"\t- {email}")
        print("Telefones: ")
        for telefone in dicionario[crm][6]:
            print(f"\t- {telefone}")
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------
def pesquisar_paciente(dicionario, cpf):
    if chave_existe_no_dicionario(dicionario, cpf):
        print(f"CPF: {cpf}")
        print(f"Nome: {dicionario[cpf][0]}")
        print(f"Data de nascimento: {dicionario[cpf][1]}")
        print(f"Sexo: {dicionario[cpf][2]}")
        print(f"Plano de Saúde: {dicionario[cpf][3]}")
        print(f"Emails:")
        if len(dicionario[cpf][5]) == 0:
            print(f"\t- Não há e-mails cadastrados")
        else:
            for email in dicionario[cpf][4]:
                print(f"\t- {email}")
        print("Telefones:")
        for telefone in dicionario[cpf][5]:
                print(f"\t- {telefone}")
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------
def pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla_chaves):
    if chave_existe_no_dicionario(dict_consultas, tupla_chaves):

        nome_profissional = dict_medicina[tupla_chaves[0]][0]
        nome_paciente = dict_pacientes[tupla_chaves[1]][0]

        print(f"Profissional: {nome_profissional}")
        print(f"Paciente: {nome_paciente}")
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
def cadastrar_profissional_medicina(dicionario, caminho_arquivo):
    profissional = []
    emails = []
    telefones = []

    crm = input("Digite o CRM do profissional: ")

    if chave_existe_no_dicionario(dicionario, crm): 
        return False
    else:
        profissional.append(input("Digite o nome: "))
        profissional.append(input("Digite a data de nascimento (Formato: DD/MM/AAAA): "))
        profissional.append(input("Digite o sexo (Masculino, Feminino ou Não-binário): "))
        profissional.append(input("Digite a especialidade (Ex: Cardiologista): "))
        profissional.append(input("Digite a universidade de formação (Ex: UFSCar): "))

        adicionar_email(emails) 
        profissional.append(emails) 
        adicionar_telefone(telefones)
        profissional.append(telefones) 

        dicionario[crm] = profissional

        return salvar_dicionario_no_arquivo(dicionario, caminho_arquivo)
    
#---------------------------------------------------------------------------------------------
def cadastrar_paciente(dicionario,caminho_arquivo): 
    paciente = []
    emails = []
    telefones = []
    
    cpf = input("Digite o CPF do paciente:")
    
    if chave_existe_no_dicionario(dicionario, cpf):
        return False
    
    else:
        paciente.append(input("Digite o nome: "))
        paciente.append(input("Digite a data de nascimento (Formato: DD/MM/AAAA): "))
        paciente.append(input("Digite o sexo (Masculino, Feminino ou Não-binário): "))
        paciente.append(input("Digite o Plano de Saúde (Ex: Unimed): "))
        
        adicionar_email(emails) 
        paciente.append(emails) 
        adicionar_telefone(telefones)
        paciente.append(telefones) 

        # Passa para o CPF certo as informações do paciente criado aqui
        dicionario = paciente 
        return salvar_dicionario_no_arquivo(dicionario, caminho_arquivo)
        
#--------------------------------------------------------------------------------------------
def cadastrar_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    consulta = []
    lista_medicamentos = []
    lista_posologias = []

    tupla_chaves = criar_tupla_chaves()
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
                print("Atenção! Já existe uma consulta para este paciente neste dia e horário: ")
                pesquisar_consulta(dict_consultas, dict_medicina, dict_pacientes, tupla)
            return False
    return True

#--------------------------------------------------------------------------------------------
def alterar_profissional_medicina(dicionario, caminho_arquivo): 
    crm = input("Digite o CRM: ")

    if chave_existe_no_dicionario(dicionario, crm): 
        print()
        print("------------ Informações atuais ------------" )
        pesquisar_profissional_medicina(dicionario, crm) 

        print()
        print("*************** Alteração dos dados ***************")
        
        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") 
        if nome != "": 
            dicionario[crm][0] = nome
            print("Nome alterado!")
            print()

        else: 
            print("Nome mantido.")
            print()

        nascimento = input("Digite a nova data de nascimento (ou pressione Enter para manter o atual): ")
        if nascimento != "":
            dicionario[crm][1] = nascimento
            print("Data de nascimento alterada.")
            print()
        else:
            print("Data de nascimento mantida.")
            print()

        sexo = input("Digite o novo sexo (ou pressione Enter para manter o atual): ")
        if sexo != "":
            dicionario[crm][2] = sexo
            print("Sexo alterado.")
            print()
        else:
            print("Sexo mantido.")
            print()

        especialidade = input("Digite a nova especialidade (ou pressione Enter para manter o atual): ")
        if especialidade != "":
            dicionario[crm][3] = especialidade
            print("Especialidade alterada.")
            print()
        else:
            print("Especialidade mantida.")
            print()

        universidade = input("Digite a nova universidade (ou pressione Enter para manter o atual): ")
        if universidade != "":
            dicionario[crm][4] = universidade
            print("Especialidade alterada.")
            print()
        else:
            print("Especialidade mantida.")
            print()

        if alterar_emails(dicionario, crm):
            print("E-mail(s) alterado(s).")
            print()
        else:
            print("E-mail(s) mantido(s).")
            print()

        if alterar_telefones(dicionario, crm):
            print("Telefone(s) alterado(s).")
            print()
        else:
            print("Telefone(s) mantido(s).")
            print()
        
        return salvar_dicionario_no_arquivo(dicionario, caminho_arquivo)
    else:
        return False

#--------------------------------------------------------------------------------------------
def alterar_paciente(dicionario,caminho_arquivo): 
    cpf = input("Digite o CPF: ")

    if chave_existe_no_dicionario(dicionario, cpf): 
        print()
        print("------------ Informações atuais ------------" )
        pesquisar_paciente(dicionario, cpf) 

        print()
        print("*************** Alteração dos dados ***************")

        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") 
        if nome != "": 
            dicionario[cpf][0] = nome
            print("Nome alterado!")
            print()

        else: 
            print("Nome mantido.")
            print()

        nascimento = input("Digite a nova data de nascimento (ou pressione Enter para manter o atual): ")
        if nascimento != "":
            dicionario[cpf][1] = nascimento
            print("Data de nascimento alterada.")
            print()
        else:
            print("Data de nascimento mantida.")
            print()

        sexo = input("Digite o novo sexo (ou pressione Enter para manter o atual): ")
        if sexo != "":
            dicionario[cpf][2] = sexo
            print("Sexo alterado.")
            print()
        else:
            print("Sexo mantido.")
            print()

        plano = input("Digite o novo Plano de Saúde (ou pressione Enter para manter o atual): ")
        if plano != "":
            dicionario[cpf][3] = plano
            print("Plano de Saúde alterado.")
            print()
        else:
            print("Plano de Saúde mantido.")
            print()
            
        if alterar_emails(dicionario,  cpf):
            print("E-mail(s) alterado(s).")
            print()
        else:
            print("E-mail(s) mantido(s).")
            print()

        if alterar_telefones(dicionario,  cpf):
            print("Telefone(s) alterado(s).")
            print()
        else:
            print("Telefone(s) mantido(s).")
            print()
        
        return salvar_dicionario_no_arquivo(dicionario,caminho_arquivo)
    
    else:
        return False

#--------------------------------------------------------------------------------------------
def alterar_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    tupla_chaves = criar_tupla_chaves()
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
            print("CRM alterado!")
            print()

        else: 
            crm = tupla_chaves[0]
            print("CRM mantido.")
            print()

        cpf = input("Digite o novo CPF (ou pressione Enter para manter o atual): ")
        if cpf != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("CRM alterado!")
            print()

        else: 
            cpf = tupla_chaves[1]
            print("CRM mantido.")
            print()

        data_da_consulta = input("Digite a nova data da consulta (Formato: DD/MM/AAAA) (ou pressione Enter para manter o atual): ")
        if data_da_consulta != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("Data da consulta alterada!")
            print()

        else: 
            data_da_consulta = tupla_chaves[2]
            print("Data da consulta mantida.")
            print()
        
        hora_da_consulta = input("Digite a nova hora da consulta (Formato 24h: 07:00; 19:00) (ou pressione Enter para manter o atual): ")
        if hora_da_consulta != "":
            nova_tupla = (crm, cpf, data_da_consulta, hora_da_consulta)
            print("Hora da consulta alterada!")
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
            print("Diagnóstico alterado!")
            print()
        else:
            print("Diagnóstico mantido.")
            print()

        if alterar_medicamentos(dict_consultas, nova_tupla):
            print("Medicamento(s) alterado(s).")
            print()
        else:
            print("Medicamento(s) mantido(s).")
            print()
        
        return salvar_dicionario_no_arquivo(dict_consultas,caminho_arquivo)
    else:
        return False

#---------------------------------------------------------------------------------------------
def excluir_profissional_medicina(dicionario, caminho_arquivo):
    crm = input("Digite o CRM: ")

    if chave_existe_no_dicionario(dicionario, crm):
        print("------------ Profissional encontrado ------------")
        pesquisar_profissional_medicina(dicionario, crm)

        print()
        confirmar = input("Tem certeza que deseja excluir este profissional? Os dados não poderão ser recuperados.\nDigite 'Confirmar' para excluir ou 'Cancelar' para manter os dados: ")

        if confirmar.lower() == 'confirmar':
            del dicionario[crm]
            salvar_dicionario_no_arquivo(dicionario, caminho_arquivo)
            return "confirmado" 
        
        elif confirmar.lower() == 'cancelar':
            return "cancelado"
        
        else:
            return "erro"
        
    else:
        return "falha"

#---------------------------------------------------------------------------------------------
def excluir_paciente(dicionario, caminho_arquivo):
    cpf = input("Digite o CPF: ")

    if chave_existe_no_dicionario(dicionario, caminho_arquivo):
        print("------------ Paciente encontrado ------------")
        pesquisar_paciente(dicionario, cpf)

        print()
        confirmar = input("Tem certeza que deseja excluir este paciente? Os dados não poderão ser recuperados.\nDigite 'Confirmar' para excluir ou 'Cancelar' para manter os dados: ")

        if confirmar.lower() == 'confirmar':
            del dicionario[cpf]
            salvar_dicionario_no_arquivo(dicionario,caminho_arquivo)
            return "confirmado" 
        
        elif confirmar.lower() == 'cancelar':
            return "cancelado"
        
        else:
            return "erro"
        
    else:
        return "falha"
    
#--------------------------------------------------------------------------------------------
def excluir_consulta(dict_consultas, dict_medicina, dict_pacientes, caminho_arquivo):
    tupla_chaves = criar_tupla_chaves()

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
#### Funções de arquivo =====================================================================
#############################################################################################
#--------------------------------------------------------------------------------------------
def arquivo_existe(nome_arquivo):
    import os
    return os.path.isfile(nome_arquivo) #retorna True se o arquivo existir e False se não existir. Além de verificar o caminho, isfile() verifica se é um arquivo legítimo e não um diretório ou link. O método .exists() só verifica se o caminho existe, mas pode ser um diretório ou link. Ele não confirma se é um arquivo.

#--------------------------------------------------------------------------------------------
def criar_arquivo(caminho_arquivo):
    print()
    print(f"O arquivo {caminho_arquivo[2:]} não foi encontrado. Será criado um novo arquivo.")
    arquivo = open(caminho_arquivo, 'w')
    arquivo.close()

#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_medicina(dicionario):
    arquivo_medicina = open('./profissionais_medicina.txt', 'r')

    for linha in arquivo_medicina:
        linha = linha.strip() 

        chave, valor = linha.split(": ", 1) 

        elementos_do_valor = valor.split(", ") 

        emails = elementos_do_valor[5] 
        emails = emails[1:-1].strip().split("; ") 

        telefones = elementos_do_valor[6]
        telefones = telefones[1:-1].strip().split("; ")

        dicionario[chave] = elementos_do_valor[:5] + [emails] + [telefones]
    arquivo_medicina.close()


#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_pacientes(dicionario):
    arquivo_paciente=open('./pacientes.txt','r')

    for linha in arquivo_paciente:
        linha = linha.strip()

        chave,valor = linha.split(":", 1)

        elementos_do_valor = valor.split(", ")

        emails = elementos_do_valor[4]
        emails = emails[1:-1].strip().split("; ")

        telefones=elementos_do_valor[5]
        telefones=telefones[1:-1].strip().split("; ")

        dicionario[chave] = elementos_do_valor[:4] + [emails] + [telefones]

    arquivo_paciente.close()

#--------------------------------------------------------------------------------------------
def pegar_dados_do_arquivo_consultas(dicionario):
    arquivo_consultas = open('./consultas.txt', 'r')

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

    return True

#############################################################################################
#### Main ===================================================================================
#############################################################################################
def main():
    Medicina = {}
    caminho_arquivo_medicina = './profissionais_medicina.txt'
    Pacientes = {}
    caminho_arquivo_pacientes = "./pacientes.txt"
    Consultas = {}
    caminho_arquivo_consultas = './consultas.txt'

    opcao_menu = 1
    while opcao_menu!=5:
        opcao_menu = menu_principal()

        #inicializa opção para submenus opcao_submenu
        opcao_submenu = 1 
        if opcao_menu == 1:

            # Se o arquivo não existir, cria um arquivo
            if not arquivo_existe(caminho_arquivo_medicina):
                criar_arquivo(caminho_arquivo_medicina)

            # Coloca no dicionario medicina os dados do arquivo de texto
            pegar_dados_do_arquivo_medicina(Medicina)

            # enquanto opcao_submenu não indicar retorno ao menu principal(6) ou encerrar(7), repete o submenu de medicina
            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu = submenu_medicina()

                # condições para acessar funções específicas
                if opcao_submenu == 1:
                    print()
                    print("************ Profissionais de Medicina *************")

                    if not mostrar_todos_os_profissionais(Medicina): # FUNCIONANDO
                        print(f"\n---------------------------------------------------")
                        print("Não há profissionais de medicina cadastrados ainda.")
                        print("---------------------------------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n********** Pesquisar profissional de medicina *********** ")
                    crm = input("Digite o CRM do profissional: ")

                    print(f"\n****************** Resultado da busca ******************* ")

                    if not pesquisar_profissional_medicina(Medicina, crm): # FUNCIONANDO
                        print(f"\n--------------------------------------------------------------")
                        print("Profissional não encontrado. Verifique o CRM e tente novamente")
                        print("--------------------------------------------------------------")
                    
                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n********** Adicionar profissional de medicina ***********")

                    if cadastrar_profissional_medicina(Medicina, caminho_arquivo_medicina): # FUNCIONANDO
                        print(f"\n------------------------------------")
                        print("Profissional adicionado com sucesso!")
                        print("------------------------------------")

                    else:
                        print(f"\n---------------------------------------")
                        print("Já existe um profissional com este CRM.")
                        print("---------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 4:
                    print(f"\n************ Alterar cadastro profissional *************")

                    if alterar_profissional_medicina(Medicina, caminho_arquivo_medicina): # FUNCIONANDO
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

                    retorno = excluir_profissional_medicina(Medicina, caminho_arquivo_medicina) # FUNCIONANDO

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
                    print("Retornando ao menu principal...") # FUNCIONANDO

                elif opcao_submenu == 7:
                    msg_encerrado()
                    opcao_menu = 5
           
        elif opcao_menu == 2:
            if not arquivo_existe(caminho_arquivo_pacientes):
                criar_arquivo(caminho_arquivo_pacientes)
            
            pegar_dados_do_arquivo_pacientes(Pacientes)

            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu=submenu_pacientes()

                if opcao_submenu==1:
                    print()
                    print(("******************* Pacientes ********************"))
                    if not mostrar_todos_os_pacientes(Pacientes): # FUNCIONANDO
                        print(f"\n-----------------------------------")
                        print("Não há pacientes cadastrados ainda.")
                        print("-----------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n****************** Pesquisar paciente ******************* ")
                    cpf = input("Digite o CPF do paciente: ")
                    
                    print(f"\n****************** Resultado da busca ******************* ") 
                    if not pesquisar_paciente(Pacientes, cpf): # FUNCIONANDO
                        print(f"\n----------------------------------------------------------")
                        print("Paciente não encontrado. Verifique o CPF e tente novamente")
                        print("----------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n***************** Adicionar paciente ******************")
                    if cadastrar_paciente(Pacientes,caminho_arquivo_pacientes): #FUNCIONANDO 
                        print(f"\n--------------------------------")
                        print("Paciente adicionado com sucesso!")
                        print("--------------------------------")
                    else:
                        print(f"\n-----------------------------------")
                        print("Já existe um paciente com este CPF.")
                        print("-----------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 4:
                    print(f"\n************ Alterar cadastro de paciente *************")
                    if alterar_paciente(Pacientes,caminho_arquivo_pacientes): # FUNCIONANDO
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
                    retorno = excluir_paciente(Pacientes,caminho_arquivo_pacientes) # FUNCIONANDO

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
                    print("Retornando ao menu principal...") # FUNCIONANDO

                elif opcao_submenu == 7:
                    msg_encerrado()
                    opcao_menu = 5
                    
        elif opcao_menu == 3:

            # Se o arquivo não existir, cria um arquivo
            if not arquivo_existe(caminho_arquivo_consultas):
                criar_arquivo(caminho_arquivo_consultas)
            
            if not arquivo_existe(caminho_arquivo_medicina):
                criar_arquivo(caminho_arquivo_medicina)
            
            if not arquivo_existe(caminho_arquivo_pacientes):
                criar_arquivo(caminho_arquivo_pacientes)

            pegar_dados_do_arquivo_medicina(Medicina)
            pegar_dados_do_arquivo_pacientes(Pacientes)
            pegar_dados_do_arquivo_consultas(Consultas)


            # enquanto opcao_submenu não indicar retorno ao menu principal(6) ou encerrar(7), repete o submenu de medicina
            while opcao_submenu!=6 and opcao_submenu!=7:
                opcao_submenu = submenu_consultas()

                # condições para acessar funções específicas
                if opcao_submenu == 1:
                    print()
                    print("******************* Consultas ********************")
                    if not mostrar_todas_as_consultas(Consultas, Medicina, Pacientes): # FUNCIONANDO
                        print(f"\n------------------------------------")
                        print("Não há consultas cadastradas ainda.")
                        print("------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 2:
                    print(f"\n****************** Pesquisar consulta ******************* ")
                    tupla_chaves = criar_tupla_chaves()

                    print(f"\n****************** Resultado da busca ******************* ")
                    if not pesquisar_consulta(Consultas, Medicina, Pacientes, tupla_chaves): # FUNCIONANDO
                        print(f"\n-------------------------------------------------------------")
                        print("Consulta não encontrada. Verifique os dados e tente novamente")
                        print("-------------------------------------------------------------")

                    print()
                    input("Pressione enter para retornar ao menu...")

                elif opcao_submenu == 3:
                    print(f"\n****************** Adicionar consulta *******************")
                    retorno = cadastrar_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas) # FUNCIONANDO

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
                    if alterar_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas): # FUNCIONANDO
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
                    retorno = excluir_consulta(Consultas, Medicina, Pacientes, caminho_arquivo_consultas) # FUNCIONANDO

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
            print(submenu_relatorios()) # TESTE
        elif opcao_menu == 5:
            msg_encerrado()

#############################################################################################
#### Programa principal =====================================================================
#############################################################################################
main()