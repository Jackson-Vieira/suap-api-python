import requests

class Suap:
    def __init__(self,token=False):
        if token:
            self.token = token
        self.token = None

        self.endpoint = 'https://suap.ifrn.edu.br/api/v2/'

   
    def autenticar(self, username, password, acessKey=False, setToken=True):
        """
        Faz a autenticação de  um usuário e retorna um token de acesso.
        """

        if acessKey:
            url = self.endpoint+'autenticacao/acesso_responsaveis/'
            params = {
                'matricula': username,
                'chave': password,
                }
        else:
            url = self.endpoint+'autenticacao/token/'
            params = {
                'username':username,
                'password':password,
            }

        response = requests.post(url, data=params)
        
        data = False

        if response.status_code == 200:
            data = response.json()
            if setToken:
                try:
                    self.setToken(data['token'])  
                except:
                    self.setToken(data['access']) 

        return data
    
    def setToken(self, token):
        self.token = token

    def getMeusDados(self):
        """
        Retorna todos os dados pessoais do usuario
        """

        url = self.endpoint+'minhas-informacoes/meus-dados/'
        return self.doGETRequest(url)

    def getMeusPeriodosLetivos(self):
        """
        Retorna todos os periodos letivos do usuario
        """

        url = self.endpoint+'minhas-informacoes/meus-periodos-letivos/'
        return self.doGETRequest(url)

    def getMeuBoletim(self, year, periodo):
        """
        Retorna o boletim de todas matérias em determinado ano e periodo
        """

        url = self.endpoint+f'minhas-informacoes/boletim/{year}/{periodo}'
        return self.doGETRequest(url)

    def getTurmasVirtuais(self, year, periodo):
        """
        Retorna todas as turmas virtuais do usuario em determinado ano e periodo
        """

        url = self.endpoint+f"minhas-informacoes/turmas-virtuais/{year}/{periodo}"
        return self.doGETRequest(url)
    
    def getTurmaVirtual(self, id_turma_virtual):
        """
        Retorna todas as informações de uma turma virtual do usuario

        id --> ID da turma virtual
        """

        url = self.endpoint+f"minhas-informacoes/turma-virtual/{id_turma_virtual}/"
        return self.doGETRequest(url)

    def doGETRequest(self, url):
        response = requests.get(url, headers={'Authorization': f'Bearer {self.token}'})

        data = False

        if response.status_code == 200:
            data = response.json()
        
        return data