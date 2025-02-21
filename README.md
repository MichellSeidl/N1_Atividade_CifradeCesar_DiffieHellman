# N1_Atividade_CifradeCesar_DiffieHellman

## Visão Geral

Este projeto implementa um sistema de comunicação simples entre um cliente e um servidor, utilizando o algoritmo de troca de chaves Diffie-Hellman e a cifra de César para encriptação/desencriptação. A comunicação ocorre via uma conexão TCP, e os dados trocados são criptografados usando uma cifra de César personalizada baseada na tabela ASCII (0-255). O algoritmo Diffie-Hellman garante que tanto o cliente quanto o servidor compartilhem a mesma chave para encriptação e decriptação, mesmo trocando apenas as chaves públicas.

O sistema é composto por duas partes:

- **Cliente:** Conecta-se ao servidor, troca as chaves, envia uma mensagem criptografada e recebe a resposta criptografada do servidor.
- **Servidor:** Escuta por conexões dos clientes, recebe a mensagem criptografada, desencripta, processa a mensagem, criptografa a resposta e envia-a de volta ao cliente.

## Requisitos

- Python 3.x
- Biblioteca `socket` (para comunicação TCP)
- Biblioteca `random` (para geração de chaves aleatórias)

## Instalação

Para rodar o sistema, basta executar os scripts do servidor e do cliente em terminais diferentes.

1. **Servidor:**
   - Execute o script do servidor em um terminal com o seguinte comando:

   ```bash
   python3 servidor.py

# Como Funciona

## Troca de Chaves Diffie-Hellman

O cliente gera uma chave privada e calcula sua chave pública usando a fórmula:


Onde `g` é o gerador e `p` é um número primo.

O cliente envia sua chave pública ao servidor.

O servidor gera sua própria chave privada e calcula sua chave pública da mesma maneira. Ele envia sua chave pública ao cliente.

Tanto o cliente quanto o servidor calculam a chave compartilhada de forma independente, usando a chave pública do outro e sua própria chave privada:


Esta chave compartilhada é usada para gerar um valor de deslocamento para a cifra de César, que será usado na encriptação/desencriptação.

## Cifra de César (Encriptação/Desencriptação)

### Encriptação:

1. Cada caractere da mensagem é convertido para seu valor ASCII.
2. Um deslocamento (baseado na chave compartilhada) é aplicado ao valor ASCII de cada caractere.
3. O valor resultante é convertido de volta para um caractere e adicionado ao resultado final.

### Desencriptação:

1. O processo reverso da encriptação é aplicado, usando o deslocamento negativo da chave compartilhada para recuperar a mensagem original.

## Interação Cliente-Servidor

### Cliente:

1. O cliente se conecta ao servidor e troca as chaves públicas.
2. Ele encripta uma mensagem usando a chave compartilhada e envia a mensagem criptografada ao servidor.
3. O cliente recebe a resposta criptografada do servidor, desencripta e exibe o resultado.

### Servidor:

1. O servidor aguarda uma conexão de cliente e troca as chaves públicas.
2. Ele desencripta a mensagem recebida do cliente utilizando a chave compartilhada.
3. O servidor processa a mensagem (por exemplo, convertendo-a para maiúsculas) e a criptografa novamente antes de enviar a resposta ao cliente.
4. O servidor fecha a conexão após a interação ser concluída.

## Explicação do Código

### Script do Cliente (`cliente.py`)

1. **Estabelecendo uma Conexão TCP:** O cliente cria um socket e se conecta ao servidor no IP e na porta especificados.
2. **Geração de Chaves (Diffie-Hellman):** O cliente gera uma chave privada e calcula sua chave pública, que envia ao servidor.
3. **Encriptação da Mensagem:** Usando a chave compartilhada derivada do Diffie-Hellman, o cliente encripta a entrada do usuário utilizando a cifra de César e envia a mensagem criptografada ao servidor.
4. **Recebendo a Resposta:** O cliente recebe a resposta criptografada do servidor, desencripta e imprime o resultado.

### Script do Servidor (`servidor.py`)

1. **Aguardando Conexões:** O servidor escuta as conexões de entrada na porta especificada.
2. **Geração de Chaves (Diffie-Hellman):** Após receber a chave pública do cliente, o servidor gera sua chave privada e calcula sua chave pública, que envia de volta ao cliente.
3. **Desencriptação da Mensagem:** O servidor desencripta a mensagem recebida do cliente utilizando a chave compartilhada.
4. **Processamento da Mensagem:** O servidor converte a mensagem recebida para maiúsculas e a criptografa novamente com a cifra de César antes de enviar a resposta ao cliente.

## Tutorial de execução
1. Abra a pasta do projeto no Visual Studio Code em ambos os computadores.
2. No arquivo `Simple_tcpServer.txt`, ajuste o endereço de IP conforme necessário.
3. No computador que será o **servidor**, abra o terminal do VS Code e execute o comando:
   ```bash
   py .\Simple_tcpServer.txt

4. No computador que será o cliente, abra o terminal do VS Code e execute o comando:
    ```bash
   py .\Simple_tcpClient.txt
5. No computador cliente, digite a frase desejada no terminal.
6. O resultado será exibido em ambos os terminais (cliente e servidor).

## Notas

- A cifra de César utilizada aqui é uma variação que opera sobre a tabela ASCII completa (0-255), garantindo que todos os caracteres, incluindo caracteres especiais, possam ser encriptados e desencriptados.
- O algoritmo Diffie-Hellman de troca de chaves garante que o cliente e o servidor possam estabelecer uma chave compartilhada de forma segura, mesmo em um canal não seguro.




