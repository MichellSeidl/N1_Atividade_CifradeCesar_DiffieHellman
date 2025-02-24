from socket import *
import random

# Função para gerar a chave compartilhada usando Diffie-Hellman
def diffie_hellman(private_key, public_key, p):
    return pow(public_key, private_key, p)

# Função para encriptar o texto (cifra de César utilizando a tabela ASCII)
def cifra_cesar_encriptar(texto, deslocamento):
    resultado = ""
    for char in texto:
        # Obtém o valor ASCII do caractere
        ascii_val = ord(char)
        
        # Aplica o deslocamento ao valor ASCII
        novo_ascii = ascii_val + deslocamento
        
        # Caso o valor ASCII ultrapasse o limite do intervalo imprimível (de 32 a 255), ajustamos
        if novo_ascii > 255:
            novo_ascii -= 256  # Volta para o começo (32)
        elif novo_ascii < 0:
            novo_ascii += 256  # Volta para o final (255)

        # Converte o novo valor ASCII de volta para o caractere e adiciona ao resultado
        resultado += chr(novo_ascii)
    
    return resultado

# Função para desencriptar o texto (simulação com cifra de César baseada na tabela ASCII)
def cifra_cesar_desencriptar(texto, deslocamento):
    return cifra_cesar_encriptar(texto, -deslocamento)

# Função principal do cliente
def cliente():
    serverName = "10.1.70.9"  # Endereço IP do servidor
    serverPort = 1300  # Porta do servidor
    clientSocket = socket(AF_INET, SOCK_STREAM)  # Cria o socket TCP
    clientSocket.connect((serverName, serverPort))  # Conecta-se ao servidor

    # Parâmetros públicos para Diffie-Hellman
    p = 23  # Número primo
    g = 5   # Gerador

    # Gerando a chave privada e a chave pública do cliente
    private_key = random.randint(1000000, 10000000 - 1)
    print(f"Chave privada gerada: {private_key}")
    
    public_key = pow(g, private_key, p)
    
    # Enviando a chave pública para o servidor
    clientSocket.send(bytes(str(public_key), "utf-8"))

    # Recebendo a chave pública do servidor
    server_public_key = int(clientSocket.recv(1024).decode("utf-8"))

    # Calculando a chave compartilhada
    shared_key = diffie_hellman(private_key, server_public_key, p)
    print(f"Chave compartilhada gerada: {shared_key}")

    # Usando a chave compartilhada para encriptar a mensagem
    sentence = input("Input sentence: ")  # Entrada do usuário (pode incluir caracteres especiais)
    deslocamento = shared_key % 95  # Gerando deslocamento para a cifra de César a partir da chave compartilhada
    sentence_encriptada = cifra_cesar_encriptar(sentence, deslocamento)

    # Enviando a mensagem encriptada
    clientSocket.send(bytes(sentence_encriptada, "utf-8"))

    # Recebendo a resposta do servidor
    modifiedSentence = clientSocket.recv(65000)
    texto = str(modifiedSentence, "utf-8")

    # Desencriptando a resposta do servidor
    texto_desencriptado = cifra_cesar_desencriptar(texto, deslocamento)
    print("Received from Server (after decryption): ", texto_desencriptado)

    clientSocket.close()

# Executando o cliente
cliente()
