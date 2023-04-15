## O que é o RPChecker?
Trata-se de uma aplicação para a verificação do status de um ou mais sites, indicando se está online ou offline.

## Instruções

### 1. Criando o ambiente de trabalho
Para a criação do projeto, recomenda-se o uso de ambientes virtuais. Para isso, inicie um terminal e rode os seguintes comandos:

##### Usando Linux
Siga o comando:
```
cd meuprojeto/
python -m venv venv
source venv/bin/activate
```

##### Usando Windows
Siga o comando:
```
PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS>
```
### 2. Rodando o Projeto
```sh
(venv) $ python -m rpchecker -u indicium.tech
The status of "indicium.tech" is: "Online!" 👍
```
### Opções

O RPChecker fornece as seguintes opções:

- `-u` ou `--urls` checa o status de uma ou mais urls.
- `-f` ou `--file` confere o status de cada url dentro de um arquivo

Mensagem de ajuda:
```sh
(venv) $ python -m rpchecker -h
usage: rpchecker [-h] [-u URLs [URLs ...]] [-f FILE]

Confere a disponibilidade dos sites

  -h, --help            show this help message and exit
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        insira uma ou mais URLs separadas por espaço
  -f FILE, --file FILE
                        insira o caminho completo junto com o nome do arquivo
```

Confira algumas urls:
```sh
(venv) $ python -m rpchecker -u globo.com indicium.tech google.com
O status da "globo.com" é: "Online!" 👍
O status da "indicium.tech" é: "Online!" 👍
O status da "google.com" é: "Online!" 👍
```

Resultado caso um site esteja fora do ar:
```sh
(venv) $ python -m rpchecker --urls incidium.tech
O status da "incidium.tech" é: "Offline?" 👎
  Erro: "[Errno 11001] getaddrinfo failed"
```

Verificando urls a partir de um arquivo:
```sh
(venv) $ python -m rpchecker -f {caminho para o arquivo}/arquivo
O status da "google.com" é: "Online!" 👍
O status da "facebook.com" é: "Online!" 👍
O status da "folha.com.br" é: "Online!" 👍
O status da "globo.com" é: "Online!" 👍
```