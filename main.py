while True:
    print("Cálculo de Multas\n")
    print("Onde circulava o veículo?") 
    print("1 - Localidade")
    print("2 - Fora da Localidade") 
    print("3 - Autoestrada")
    print("4 - Cancelar Cálculo")
    print()
        
    local = input("Selecione o local: ")
    
    velocidade = int(input("Introduza a velocidade a que circulava o veículo (km/h): "))
        
    if local == "1":
        multaLocalidade(velocidade)
    elif local == "2":
        multaFora(velocidade)
    elif local == "3":
        multaAutoestrada(velocidade)
    elif local == "4":
        continue                               
    else:
        print("Local inválido.")