from datetime import datetime




#Definição da função de SELECT 
def gerar_SELECT(dt_log, fosforo, potassio, ph, temperatura, umidade):
        print("\n=================================    SELECT NPK_coleta   =================================")
        print(f"""SELECT ID_coleta_nutriente, Dt_log, ID_Sensor, Tipo_desc, Nitrogenio, Fosforo, Potassio, Unidades FROM NPK_Coleta WHERE Dt_log = '{dt_log}', Fosforo = {fosforo:.2f}, Potassio = {potassio:.2f};\n""")

        print("\n=================================    SELECT PH_coleta   =================================")
        print(f"""SELECT ID_coleta_ph, Dt_log , ID_Sensor, Tipo_desc, Ph, Temperatura, NTU, Condutividade, Unidades FROM PH_Coleta WHERE Dt_log = '{dt_log}', Ph ={ph:.2f}, Temperatura={temperatura:.2f};\n""")
           
        
        print("\n=================================    SELECT Umidade_coleta   =================================")
        print(f"""SELECT  ID_coleta_umidade, ID_Sensor,Dt_log, ID_Sensor, Tipo_desc, Umidade, Temperatura, Unidades FROM Umidade_Coleta WHERE Dt_log = '{dt_log}', Umidade = {umidade:.2f}, Temperatura = {temperatura:.2f};\n""")




#Definição da função de INSERT
def gerar_INSERT(dt_log, fosforo, potassio, ph, temperatura, umidade):
            print("\n=================================    INSERT NPK_coleta   =================================")
            print(f"""INSERT INTO NPK_coleta (ID_coleta_nutriente, Dt_log, ID_Sensor, Tipo_desc, Nitrogenio, Fosforo, Potassio, Unidades)
VALUES (1,'{dt_log}', 1, 'Botao RED/GREEN', 0.00, {fosforo:.2f}, {potassio:.2f}, 'mol');\n""")

            print("=================================    INSERT PH_coleta   =================================")
            print(f"""INSERT INTO PH_coleta (ID_coleta_ph, Dt_log, ID_Sensor, Tipo_desc, Ph, Temperatura, NTU, Condutividade, Unidades)
VALUES (1,'{dt_log}', 3, 'LDR Modulo sensor fotoresistor', {ph:.2f}, {temperatura:.2f}, 0.00, 0, 'ppm');\n""")

            print("=================================    INSERT Umidade_coleta   =================================")
            print(f"""INSERT INTO Umidade_coleta (ID_coleta_umidade, Dt_log, ID_Sensor, Tipo_desc, Umidade, Temperatura, Unidades)
VALUES (1,'{dt_log}', 4, 'DTH22', {umidade:.2f}, {temperatura:.2f}, 'ºC / %');\n""")




#Definição da função de UPDATE
def gerar_UPDATE(dt_log, fosforo, potassio, ph, temperatura, umidade):
           print("Entre com os novos valores (criado script para atualizar a linha ''antiga'' do log colado)\n")
           new_Data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           new_Fosforo = float(input("Novo valor de Fosforo: "))
           new_Potassio = float(input("Novo valor de Potassio: "))
           new_Ph = float(input("Novo valor do Ph: "))
           new_Temperatura = float(input("Novo valor de Temperatura: "))
           new_Umidade = float(input("Novo valor de Umidade: "))

           print(f"\n Revisão Alteração: \n Data: {dt_log} -> {new_Data} \n Fosforo: {fosforo} -> {new_Fosforo}\n Potassio: {potassio} -> {new_Potassio}\n Ph: {ph} -> {new_Ph}\n Temperatura: {temperatura} -> {new_Temperatura}\n Umidade: {umidade} -> {new_Umidade}")

           print("\n=================================    UPDATE NPK_coleta   =================================")
           print(f"""UPDATE NPK_coleta SET Dt_log = '{new_Data}', Fosforo ={new_Fosforo}, Potassio = {new_Potassio} WHERE Dt_log = '{dt_log}', Fosforo = {fosforo:.2f}, Potassio = {potassio:.2f};\n""")

           print("\n=================================    UPDATE PH_coleta   =================================")
           print(f"""UPDATE PH_coleta SET Dt_log = '{new_Data}', Ph = {new_Ph}, Temperatura = {new_Temperatura}, WHERE Dt_log = '{dt_log}', Ph ={ph:.2f}, Temperatura={temperatura:.2f};\n""")
           
           
           print("\n=================================    UPDATE Umidade_coleta   =================================")
           print(f"""UPDATE Umidade_coleta SET Dt_log = '{new_Data}', Umidade = {new_Umidade} Temperatura={new_Temperatura} WHERE Dt_log = '{dt_log}', Umidade = {umidade:.2f}, Temperatura = {temperatura:.2f};\n""")
           



#Definição da função de DELETE
def gerar_DELETE(dt_log, fosforo, potassio, ph, temperatura, umidade):
        print("\n=================================    DELETE NPK_coleta   =================================")
        print(f"""DELETE FROM NPK_Coleta WHERE Dt_log = '{dt_log}', Fosforo = {fosforo:.2f}, Potassio = {potassio:.2f};\n""")

        print("\n=================================    DELETE PH_coleta   =================================")
        print(f"""DELETE FROM PH_Coleta WHERE Dt_log = '{dt_log}', Ph ={ph:.2f}, Temperatura={temperatura:.2f};\n""")
           
        # Umidade_coleta (Dt_log, Tipo_desc, Umidade, Temperatura, Unidades, Sensores_ID_sensor)
        print("\n=================================    DELETE Umidade_coleta   =================================")
        print(f"""DELETE FROM Umidade_Coleta WHERE Dt_log = '{dt_log}', Umidade = {umidade:.2f}, Temperatura = {temperatura:.2f};\n""")




#Definição da função MENU
def menu(dt_log, fosforo, potassio, ph, temperatura, umidade):
    while True:
        print("\nMENU DE AÇÕES: Gerar script de comando DML no banco")
        print("1. SELECT")
        print("2. INSERT")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. Voltar a outro log")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerar_SELECT(dt_log, fosforo, potassio, ph, temperatura, umidade)
        if opcao == "2":
            gerar_INSERT(dt_log, fosforo, potassio, ph, temperatura, umidade)
        elif opcao == "3":
            gerar_UPDATE(dt_log, fosforo, potassio, ph, temperatura, umidade) 
        elif opcao == "4":
            gerar_DELETE(dt_log, fosforo, potassio, ph, temperatura, umidade)
        elif opcao == "5":
            break
        elif opcao == "0":
            print("Encerrando")
            exit()




#Loop do menu principal
while True:
    print("\nCole a linha copiada do SerialMonitor no formato: 'log,fosforo,potassio,ph,temperatura,umidade'")
    linha_armazenada = input("Entre com a linha copiada: ").strip()
    if linha_armazenada.lower().startswith("log"):
        partes = linha_armazenada.split(",")
        if len(partes) == 6:
            dt_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fosforo = float(partes[1])
            potassio = float(partes[2])
            ph = float(partes[3])
            temperatura = float(partes[4])
            umidade = float(partes[5])
    menu(dt_log, fosforo, potassio, ph, temperatura, umidade)

