from pprintpp import pprint as pp
from db.database import Graph

class PersonDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://34.201.33.19:7687',
                        user='neo4j', password='bend-humps-force')

    def read_by_age(self):
        return self.db.execute_query('MATCH (n:Pessoa WHERE n.idade > 30) RETURN(n.nome)')    
    
    def read_by_career(self):
        return self.db.execute_query('MATCH (n:Estudante) RETURN(n.profissao)')
    
    def read_by_minorAge(self):
        return self.db.execute_query('MATCH (n:Pet) RETURN MIN(n.idade)')

    def read_by_relation(self):
        return self.db.execute_query('MATCH (n:Pessoa:Estudante)-[r{ano:2018}]->(m:Pessoa:Estudante) RETURN r')

def divider():
    print('\n' + '-' * 80 + '\n')

dao = PersonDAO()

while 1:  
    print('\nO que você deseja saber?\n')  
    option = input('0. Para sair do programa\n1. Quais os nomes das pessoas da família tem mais de 30 anos?\n2. Quais as profissões dos estudantes da família? \n3. Quantos anos tem o pet mais novo da família?\n4. Qual o relacionamento entre Caroliny e Tiago?\n')

    if option == '1':
        aux = dao.read_by_age()
        pp(aux)
        divider()

    elif option == '2':
        aux = dao.read_by_career()
        pp(aux)
        divider()

    elif option == '3':
        aux = dao.read_by_minorAge()
        pp(aux)
        divider()
    
    elif option == '4':
        aux = dao.read_by_relation()
        pp(aux)
        divider()

    elif option == '0':
        break

dao.db.close()