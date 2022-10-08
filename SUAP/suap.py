import requests

class Suap:
    """
    Construtor, que pode ou não receber um token de acesso
    """
    def __init__(self,token=False):

        if token:
            self.token = token
        self.token = None

        self.endpoint = 'https://suap.ifrn.edu.br/api/v2/'

    """
    Autentica um usuário e retorna um token de acesso.
    """
    def autenticar(self, username, password, acessKey=False, setToken=True):
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
        url = self.endpoint+'minhas-informacoes/meus-dados/'
        return self.doGETRequest(url)

    def getMeusPeriodosLetivos(self):
        url = self.endpoint+'minhas-informacoes/meus-periodos-letivos/'
        return self.doGETRequest(url)

    def getMeuBoletim(self, year, periodo):
        url = self.endpoint+f'minhas-informacoes/boletim/{year}/{periodo}'
        return self.doGETRequest(url)

    def getTurmasVirtuais(self,year, periodo):
        url = self.endpoint+f"minhas-informacoes/turmas-virtuais/{year}/{periodo}"
        return self.doGETRequest(url)
    
    def getTurmaVirtual(self, id):
        url = self.endpoint+f"minhas-informacoes/turma-virtual/{id}/"
        return self.doGETRequest(url)

    def doGETRequest(self, url):
        response = requests.get(url, headers={'Authorization': f'Bearer {self.token}'})

        data = False

        if response.status_code == 200:
            data = response.json()
        
        return data