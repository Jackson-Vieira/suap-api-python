import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))
from SUAP.suap import Suap

input_data = input().split()

token_access = False

if (len(input_data)) == 2:
    student_id = input_data[0]
    suap_key = input_data[1]
elif (len(input_data) == 1):
    token_access = input_data[1]

try:
    suap = Suap()

    if token_access:
        suap.setToken(token_access)

    else:
        suap.autenticar(student_id, suap_key)

    periodosLetivos = suap.getMeusPeriodosLetivos()
    print(periodosLetivos,"\n")

    ano, periodo = 2022, 1
    meuBoletim = suap.getMeuBoletim(ano, periodo)
    print(meuBoletim,"\n")

    turmasVirtuais = suap.getTurmasVirtuais(ano, periodo)
    print(turmasVirtuais,"\n")

    turmaVirtual = suap.getTurmaVirtual(turmasVirtuais[0]['id'])
    print(turmaVirtual['participantes'],"\n")

except:
    # Mostrar erros
    print("FAIL!")
