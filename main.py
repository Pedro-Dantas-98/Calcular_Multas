def multaLocalidade(velocidade: int):
    if velocidade >= 120:
        print("Multa a atribuir: 320€")
        print() 
    elif velocidade >= 90:
        print("Multa a atribuir: 120€")
        print()
    elif velocidade > 50:
        print("Multa a atribuir: 60€")
        print()                
    else:
        print("Não ocorreu qualquer infração.")
        print()
        
def multaFora(velocidade: int):
    if velocidade >= 120:
        print("Multa a atribuir: 120€")
        print()
    elif velocidade > 90:
        print("Multa a atribuir: 60€")
        print()               
    else:
        print("Não ocorreu qualquer infração.")
        print()
        
def multaAutoestrada(velocidade: int):
    if velocidade >= 175:
        print("Multa a atribuir: 360€")
        print()
    elif velocidade > 150:
        print("Multa a atribuir: 120€")
        print()
    elif velocidade > 120:
        print("Multa a atribuir: 60€")
        print()                
    else:
        print("Não ocorreu qualquer infração.")
        print()        

while True:
    try:
        print("Cálculo de Multas")
        print("-------------------------")
        print("Onde circulava o veículo?") 
        print("1 - Localidade")
        print("2 - Fora da Localidade") 
        print("3 - Autoestrada")
        print()         
            
        local = input("Selecione o local: ")
        
        velocidade = int(input("Introduza a velocidade a que circulava o veículo (km/h): "))
            
        if local == "1":
            multaLocalidade(velocidade)
        elif local == "2":
            multaFora(velocidade)
        elif local == "3":
            multaAutoestrada(velocidade)                           
        else:
            print("Local inválido.")
    
        encerro = input("Quer encerrar o programa? (S/N): ").lower()
        
        if encerro == "s":
            print("A encerrar o programa.")
            print()
            break
        else:
            print("A resumir o programa.")
            print()             
    except ValueError:
        print("A velocidade do véiculo tem de ser um número inteiro.")
        print()        