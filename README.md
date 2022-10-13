<h1>SUAP-API-PYTHON</h1> 

> Status do Projeto: em desenvolvimento

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Informações importantes](#informações-importantes)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar os testes](#como-rodar-os-testes)

## Descrição do projeto 

<p align="justify">
    'GETTER' que tem o objetivo de se comunicar com API do SUAP e coletar as informações expecificadas
</p>

## Informações importantes
- Versão python utilizada: Python - 3.10.6

## Pré-requisitos
- requests==2.28.1

```
pip install requests==2.28.1
```

## Como rodar os testes
No terminal, clone o projeto: 

```
git clone 
```

```
cd dir
python3 tests/test.py # ON LINUX
# Escreva sua matricula e sua senha
202110******** password
```

## Casos de Uso
A aplicação pode ser utilizada como base para projetos que precise utilizar informações dos alunos do SUAP,
por exemplo alunos presentes em uma turma virtual ...
```
def getMeusDados(self):
    """
    Retorna todos os dados pessoais do usuario
    """

    url = self.endpoint+'minhas-informacoes/meus-dados/'
    return self.doGETRequest(url)
```
```
def getTurmasVirtuais(self, year, periodo):
    """
    Retorna todas as turmas virtuais do usuario em determinado ano e periodo
    """

    url = self.endpoint+f"minhas-informacoes/turmas-virtuais/{year}/{periodo}"
    return self.doGETRequest(url)
```

## Licença 
The [MIT License]() (MIT)

Copyright :copyright: 2022 - suap-api-python