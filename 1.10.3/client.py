class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance
    
clnt = Client("Николай", 50)
print('Клиент',clnt.get_name(), '\n',
              'Баланс',clnt.get_balance() )
