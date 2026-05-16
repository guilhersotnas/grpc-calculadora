from concurrent import futures
import grpc
import math
import time

import exemplo_pb2
import exemplo_pb2_grpc


class CalculadoraServicer(exemplo_pb2_grpc.CalculadoraServicer):

    def Somar(self, request, context):
        resultado = request.numero1 + request.numero2
        return exemplo_pb2.Resultado(resultado=resultado)

    def Subtrair(self, request, context):
        resultado = request.numero1 - request.numero2
        return exemplo_pb2.Resultado(resultado=resultado)

    def Multiplicar(self, request, context):
        resultado = request.numero1 * request.numero2
        return exemplo_pb2.Resultado(resultado=resultado)

    def Dividir(self, request, context):

        if request.numero2 == 0:
            return exemplo_pb2.Resultado(
                resultado=0,
                mensagem="Erro: divisão por zero"
            )

        resultado = request.numero1 / request.numero2
        return exemplo_pb2.Resultado(resultado=resultado)

    def CalcularPotencia(self, request, context):
        resultado = request.numero1 ** request.numero2
        return exemplo_pb2.Resultado(resultado=resultado)

    def CalcularRaizQuadrada(self, request, context):

        if request.valor < 0:
            return exemplo_pb2.Resultado(
                resultado=0,
                mensagem="Erro: número negativo"
            )

        resultado = math.sqrt(request.valor)
        return exemplo_pb2.Resultado(resultado=resultado)

    def SomarStream(self, request_iterator, context):

        total = 0

        for numero in request_iterator:
            total += numero.valor

        return exemplo_pb2.Resultado(resultado=total)

    def GerarTabuada(self, request, context):

        numero = request.valor

        for i in range(1, 11):

            resultado = numero * i

            yield exemplo_pb2.Resultado(
                resultado=resultado,
                mensagem=f"{numero} x {i} = {resultado}"
            )

            time.sleep(0.5)

    def CalcularMediaMovel(self, request_iterator, context):

        numeros = []

        for numero in request_iterator:

            numeros.append(numero.valor)

            media = sum(numeros) / len(numeros)

            yield exemplo_pb2.Resultado(
                resultado=media,
                mensagem=f"Média atual: {media}"
            )


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    exemplo_pb2_grpc.add_CalculadoraServicer_to_server(
        CalculadoraServicer(),
        server
    )

    server.add_insecure_port('[::]:50051')

    server.start()

    print("Servidor gRPC rodando na porta 50051...")

    server.wait_for_termination()


serve()
