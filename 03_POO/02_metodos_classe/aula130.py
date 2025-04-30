# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'): # Método construtor padrão
        self.host = host
        self.user = None # Não tem valor como padrão
        self.password = None

    def set_user(self, user): # Toda vez que preciso usar self, é um método de insancia
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user # Parecido com um self
        connection.password = password
        return connection # Precisamos dar return

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection() 
# c1.set_user('luiz')
# c1.set_password('123')
c1 = Connection.create_with_auth('luiz', '1234')
print(Connection.log('Essa é a mensagem de log'))
print(connection_log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)