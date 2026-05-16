import grpc
import exemplo_pb2
import exemplo_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')

stub = exemplo_pb2_grpc.CalculadoraStub(channel)


while True:

    print("\n===== CALCULADORA gRPC =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Somar Stream")
    print("8 - Gerar Tabuada")
    print("9 - Média Móvel")
    print("0 - Sair")

    opcao = input("Escolha: ")

    try:

        if opcao == "1":

            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))

            resposta = stub.Somar(
                exemplo_pb2.DoisNumeros(
                    numero1=n1,
                    numero2=n2
                )
            )

            print("Resultado:", resposta.resultado)

        elif opcao == "2":

            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))

            resposta = stub.Subtrair(
                exemplo_pb2.DoisNumeros(
                    numero1=n1,
                    numero2=n2
                )
            )

            print("Resultado:", resposta.resultado)

        elif opcao == "3":

            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))

            resposta = stub.Multiplicar(
                exemplo_pb2.DoisNumeros(
                    numero1=n1,
                    numero2=n2
                )
            )

            print("Resultado:", resposta.resultado)

        elif opcao == "4":

            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))

            resposta = stub.Dividir(
                exemplo_pb2.DoisNumeros(
                    numero1=n1,
                    numero2=n2
                )
            )

            if resposta.mensagem:
                print(resposta.mensagem)
            else:
                print("Resultado:", resposta.resultado)

        elif opcao == "5":

            base = float(input("Base: "))
            expoente = float(input("Expoente: "))

            resposta = stub.CalcularPotencia(
                exemplo_pb2.DoisNumeros(
                    numero1=base,
                    numero2=expoente
                )
            )

            print("Resultado:", resposta.resultado)

        elif opcao == "6":

            numero = float(input("Número: "))

            resposta = stub.CalcularRaizQuadrada(
                exemplo_pb2.Numero(valor=numero)
            )

            if resposta.mensagem:
                print(resposta.mensagem)
            else:
                print("Resultado:", resposta.resultado)

        elif opcao == "7":

            quantidade = int(input("Quantos números deseja somar? "))

            numeros = []

            for i in range(quantidade):

                valor = float(input(f"Número {i+1}: "))

                numeros.append(
                    exemplo_pb2.Numero(valor=valor)
                )

            resposta = stub.SomarStream(iter(numeros))

            print("Soma total:", resposta.resultado)

        elif opcao == "8":

            numero = float(input("Digite um número: "))

            respostas = stub.GerarTabuada(
                exemplo_pb2.Numero(valor=numero)
            )

            for resposta in respostas:
                print(resposta.mensagem)

        elif opcao == "9":

            quantidade = int(input("Quantos números? "))

            def gerar_numeros():

                for i in range(quantidade):

                    valor = float(input(f"Número {i+1}: "))

                    yield exemplo_pb2.Numero(valor=valor)

            respostas = stub.CalcularMediaMovel(
                gerar_numeros()
            )

            for resposta in respostas:
                print(resposta.mensagem)

        elif opcao == "0":

            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    except Exception as erro:
        print("Erro:", erro)
