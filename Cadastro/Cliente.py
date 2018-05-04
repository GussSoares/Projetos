

class Client:

    def __init__(self, login, password):
        self.login = login                      # login
        self.password = password                # senha
        self.balance = 0                        # saldo

    def get_login(self):
        return self.login                       # get login

    def get_password(self):
        return self.password                    # set login

    def set_login(self, login):
        self.login = login                      # get senha

    def set_password(self, password):
        self.password = password                # set senha

    def deposit(self, cash):
        self.balance += cash                    # deposita uma quantia

    def cashout(self, cash):
        self.balance -= cash                    # sacar uma quantia