from socket import *
import random

# Função para encriptar o texto (cifra de César utilizando a tabela ASCII 0-255)
def cifra_cesar_encriptar(texto, deslocamento):
    resultado = ""
    for char in texto:
        # Obtém o valor ASCII do caractere
        ascii_val = ord(char)
        
        # Aplica o deslocamento ao valor ASCII
        novo_ascii = ascii_val + deslocamento
        
        # Ajusta o valor para manter dentro do intervalo de 0 a 255
        if novo_ascii > 255:
            novo_ascii -= 256  # Volta para o início (0)
        elif novo_ascii < 0:
            novo_ascii += 256  # Volta para o final (255)

        # Converte o novo valor ASCII de volta para o caractere
        resultado += chr(novo_ascii)
    
    return resultado

# Função para desencriptar o texto (simulação com cifra de César baseada na tabela ASCII 0-255)
def cifra_cesar_desencriptar(texto, deslocamento):
    return cifra_cesar_encriptar(texto, -deslocamento)

# Função para gerar a chave compartilhada usando Diffie-Hellman
def diffie_hellman(private_key, public_key, p):
    return pow(public_key, private_key, p)

# Função principal do servidor
def servidor():
    serverPort = 1300
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(5)  # O número 5 indica o tamanho da fila de conexões

    print("TCP Server\n")
    connectionSocket, addr = serverSocket.accept()

    # Recebendo a chave pública do cliente
    client_public_key = int(connectionSocket.recv(1024).decode("utf-8"))

    # Parâmetros públicos para Diffie-Hellman
    p = 23  # Número primo
    g = 5   # Gerador

    # Gerando a chave privada e a chave pública do servidor
    private_key = random.randint(1000000, 10000000 - 1)


    print(f"Chave privada gerada: {private_key}")

    server_public_key = pow(g, private_key, p)
    
    # Enviando a chave pública do servidor para o cliente
    connectionSocket.send(bytes(str(server_public_key), "utf-8"))

    # Calculando a chave compartilhada
    shared_key = diffie_hellman(private_key, client_public_key, p)
    print(f"Chave compartilhada gerada: {shared_key}")

    # Usando a chave compartilhada para o deslocamento da cifra de César
    deslocamento = shared_key % 256  # Ajuste para lidar com o intervalo completo de ASCII (0-255)
    print(f"Deslocamento calculado: {deslocamento}")

    # Recebendo a mensagem encriptada do cliente
    sentence = connectionSocket.recv(65000)
    received = str(sentence, "utf-8")
    print("Received from Client (encrypted):", received)

    # Desencriptando a mensagem recebida
    mensagem_desencriptada = cifra_cesar_desencriptar(received, deslocamento)
    print("Received from Client (decrypted):", mensagem_desencriptada)

    # Processamento: Convertendo a sentença para maiúsculas
    capitalizedSentence = mensagem_desencriptada.upper()

    # Encriptando a resposta antes de enviar
    resposta_encriptada = cifra_cesar_encriptar(capitalizedSentence, deslocamento)

    # Enviando a resposta ao cliente
    connectionSocket.send(bytes(resposta_encriptada, "utf-8"))
    print("Sent back to Client (encrypted):", resposta_encriptada)
    
    connectionSocket.close()

# Executando o servidor
servidor()
