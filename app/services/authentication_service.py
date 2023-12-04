from app.models.user_model import UserModel

class AuthenticationService:
    def __init__(self):
        self.registered_users = []

    def register_user(self, username, password):
        user = UserModel(username, password)
        self.registered_users.append(user)
        print(f"User {username} registered successfully.")

    def login(self, username, password):
        for user in self.registered_users:
            if user.username == username and user.password == password:
                print(f"User {username} logged in successfully.")
                return
        print("Invalid username or password.")
