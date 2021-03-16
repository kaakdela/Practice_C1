class Client:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
class Guests(Client):
    def __init__(self, name, adress, status):  # Исправленный код
        super().__init__(name)
        self.adress = adress
        self.status = status
    def get_adress(self):
        return self.adress
    def get_status(self):
        return self.status
db = [{'name': 'Коля',
       'adress': 'Москва',
       'status': 'Ментор'
       },
      {'name': 'Петя',
       'adress': 'Орел',
       'status': 'Наставник'}
      ]
print('Список приглашенных гостей')
for i in db:
    client = Guests(name=i.get('name'), adress=i.get('adress'), status=i.get('status'))
    print(f'{client.name}, г. {client.adress}, статус {client.status}')
