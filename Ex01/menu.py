import math

# MENU PRINCIPAL
while True:

    print (12 * "=", " Unidade de Medida ", 12 * "=")
    print (2 * "\t", "[1]  Milha")
    print (2 * "\t", "[2]  Polegada")
    print (2 * "\t", "[3]  Pé")
    print (2 * "\t", "[4]  Centímetro")
    print (2 * "\t", "[5]  Metro")
    print (2 * "\t", "[6]  Quilômetrico")
    print (2 * "\t", "[0]  Sair")
    print (50 * "=")

    opcao = int(input("Digite a categoria desejada: \n"))

    if opcao == 1:
        print(12 * "=", "A opção escolhida para converter de MILHA(s) para:", 12 * "=")
        valor = float(input("Digite o valor desejado em MILHA(s): \n"))
        print(valor, "Milha(s) equivalem a %.3f milha(s)." % (valor))
        print(valor, "Milha(s) equivalem a %.3f polegada(s)." % (valor * 63360))
        print(valor, "Milha(s) equivalem a %.3f pé(s)." % (valor * 5280))
        print(valor, "Milha(s) equivalem a %.3f centímetro(s)." % (valor * 160934))
        print(valor, "Milha(s) equivalem a %.3f metro(s)." % (valor * 1609.34))
        print (valor,"Milha(s) equivalem a %.3f quilômetro(s)." %( valor * 1.60934 ))

    elif opcao == 2:
        print(12 * "=", "A opção escolhida para converter de POLEGADA(s) para:", 12 * "=")
        valor = float(input("Digite o valor desejado em polegada(s): \n"))
        print(valor, "Polegada(s) equivalem a %.2f polegada(s)." % (valor))
        print(valor, "Polegada(s) equivalem a %.2f milha(s)." % (valor / 63360))
        print(valor, "Polegada(s) equivalem a %.2f pé(s)." % (valor / 12))
        print(valor, "Polegada(s) equivalem a %.2f centímetro(s)." % (valor * 2.54))
        print(valor, "Polegada(s) equivalem a %.2f metro(s)." % (valor / 39.37))
        print(valor, "Polegada(s) equivalem a %.2f quilômetro(s)." % (valor / 39370))


    elif opcao == 3:
        print(12 * "=", "A opção escolhida para converter de PÉ(s) para:", 12 * "=")
        valor = float(input("Digite o valor desejado em pé(s): \n"))
        print(valor, "Pé(s) equivalem a %.2f pé(s)." % (valor))
        print(valor, "Pé(s) equivalem a %.2f milha(s)." % (valor / 5280))
        print(valor, "Pé(s) equivalem a %.2f polegada(s)." % (valor * 12))
        print(valor, "Pé(s) equivalem a %.2f centímetro(s)." % (valor * 30.48))
        print(valor, "Pé(s) equivalem a %.2f metro(s)." % (valor / 3.281))
        print(valor, "Pé(s) equivalem a %.2f quilômetro(s)." % (valor / 3281))


    elif opcao == 4:
        print(12 * "=", "A opção escolhida para converter de CENTÍMETRO(s) para:", 12 * "=")
        valor = float(input("Digite o valor desejado em Centímetro(s): \n"))
        print(valor, "Centímetro(s) equivalem a %.2f centímetro(s)." % (valor))
        print(valor, "Centímetro(s) equivalem a %.2f milha(s)." % (valor / 160934))
        print(valor, "Centímetro(s) equivalem a %.2f polegada(s)." % (valor / 2.54))
        print(valor, "Centímetro(s) equivalem a %.2f pé(s)." % (valor / 30.48))
        print(valor, "Centímetro(s) equivalem a %.2f metro(s)." % (valor / 100))
        print(valor, "Centímetro(s) equivalem a %.2f quilômetro(s)." % (valor / 100000))


        elif opcao == 5:
        print(12 * "=", "A opção escolhida para converter de METRO(s) para:", 12 * "=")
        valor = float(input("Digite o valor desejado em metro(s): \n"))
        print(valor, "Metro(s) equivalem a %.2f metro(s)." % (valor))
        print(valor, "Metro(s) equivalem a %.2f milha(s)." % (valor / 1609))
        print(valor, "Metro(s) equivalem a %.2f polegada(s)." % (valor * 39.37))
        print(valor, "Metro(s) equivalem a %.2f pé(s)." % (valor * 3.281))
        print(valor, "Metro(s) equivalem a %.2f centímetro(s)." % (valor * 100))
        print(valor, "Metro(s) equivalem a %.2f quilômetro(s)." % (valor / 1000))

elif opcao == 6:
        print(12 * "=", "A opção escolhida para converter de KM para:", 12 * "=")
        valor = float(input("Digite o valor desejado em KM: \n"))
        print(valor, "Quilômetro(s) equivalem a %.2f quilômetro(s)." % (valor))
        print(valor, "Quilômetro(s) equivalem a %.2f milha(s)." % (valor / 1.609))
        print(valor, "Quilômetro(s) equivalem a %.2f polegada(s)." % (valor * 39370))
        print(valor, "Quilômetro(s) equivalem a %.2f pé(s)." % (valor * 3281))
        print(valor, "Quilômetro(s) equivalem a %.2f centímetro(s)." % (valor * 100000))
        print(valor, "Quilômetro(s) equivalem a %.2f metro(s)." % (valor * 1000))

elif opcao> 6 or opcao < 0:
        print (50 * "=")
        print ("Selecione uma das opções abaixo:")

    elif opcao == 0:
        break