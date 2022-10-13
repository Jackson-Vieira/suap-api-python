# API-SUAP-PYTHON

Aplicação 'helper' para se comunicar com <a href="https://suap.ifrn.edu.br/api/docs/"> SUAP API </a> e pegar informações permitidas com facilidade

> Status do Projeto: em desenvolvimento

### Contents
- [Pré-requisitos](#pré-requisitos)
- [Métodos/Utilidades](#métodos-utilidades)
- [Casos de Uso](#casos-de-uso)
- [Como clonar o repositório](#como-clonar-o-repositório)
- [Como rodar os testes](#como-rodar-os-testes)
- [Como contribuir para o projeto](#como-contribuir-para-o-projeto)
___

### Pré-requisitos
- python3
- requests==2.28.1

```
pip3 install requests==2.28.1
```

### Métodos-Utilidades
- ```def getMeusDados(self)``` Pegar dados pessoais de um (usuario) 
- ```def getMeusPeriodosLetivos(self)``` Pegar Periodos Letivos de um (usuario)
- ```def getMeuBoletim(self, year, periodo)``` Pegar Boletim de um (usuario)
- ```def getTurmasVirtuais(self, year, periodo)``` Pegar Turmas Virtuais de um (usuario)
- ```def getTurmaVirtual(self, id_turma_virtual)``` Pegar Informações de Determinada Turma de um (usuario)

### Casos de Uso
A aplicação pode ser utilizada como base para projetos que precise utilizar informações dos alunos do SUAP, por exemplo pegar alunos presentes na turma do usuario, ...

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


### Como clonar o repositório
```
git clone https://github.com/Jackson-Vieira/suap-api-python.git
```

### Como rodar os testes

```
cd suap-api-python
python3 tests/test.py # ON LINUX
# Escreva sua matricula e sua senha
202110******** password
```

### Como contribuir para o projeto
Steps:
1. Fork este repositório. <a href="https://docs.github.com/pt/get-started/quickstart/fork-a-repo"> help </a>
2. Clone este repositório. `git clone https://github.com/YOUR-USERNAME/suap-api-python`
3. Acesse a pasta principal. `cd suap-api-python`
4. Definir um novo remoto (remote). `git remote add upstream git@github.com:Jackson-Vieira/suap-api-python.git`
5. Acessar a branch principal. `git checkout main`
6. Sincronizar sua cópia local antes de criar o branch.`git pull upstream main && git push origin main`
7. Crie uma branch. `git checkout -b '<your_branch_name>'`
8. Faça suas mudanças e adicione ao controle de versão. `git add . && git commit -m '<mensagem_commit>'`
9. Push para a branch principal. `git push -u origin <your_branch_name>`
10. Create the pull request.

Ou consulte <a href="https://docs.github.com/pt/get-started/quickstart/contributing-to-projects">GitHub quickstart</a>

## Licença 
The [MIT License]() (MIT)

Copyright :copyright: 2022 - suap-api-python
