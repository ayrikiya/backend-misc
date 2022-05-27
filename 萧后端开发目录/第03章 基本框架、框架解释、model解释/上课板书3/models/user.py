from models import Model


class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def validate_login(self):
        return self.username == 'summer' and self.password == '0621'

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2

