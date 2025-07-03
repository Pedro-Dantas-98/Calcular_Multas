def multaLocalidade(velocidade: int):
    if velocidade > 50:
        print("Multa a atribuir: 60€")
    elif velocidade >= 90:
        print("Multa a atribuir: 120€")
    elif velocidade >= 120:
        print("Multa a atribuir: 320€")                
    else:
        print("Não ocorreu qualquer infração.")
        
def multaFora(velocidade: int):
    if velocidade > 90:
        print("Multa a atribuir: 60€")
    elif velocidade >= 120:
        print("Multa a atribuir: 120€")                
    else:
        print("Não ocorreu qualquer infração.")
        
def multaAutoestrada(velocidade: int):
    if velocidade > 120:
        print("Multa a atribuir: 60€")
    elif velocidade > 150:
        print("Multa a atribuir: 120€")
    elif velocidade >= 175:
        print("Multa a atribuir: 360€")                
    else:
        print("Não ocorreu qualquer infração.")  

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