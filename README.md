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
