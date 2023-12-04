class CommunicationService:
    def __init__(self):
        # Простий чат для взаємодії користувачів
        self.chat_history = []

    def communicate(self):
        # Логіка забезпечення комунікації між користувачами
        print("Забезпечення комунікації між користувачами...")

        # Приклад взаємодії: два користувачі обмінюються повідомленнями
        user1_message = "Привіт, як у вас справи?"
        user2_message = "Привіт! Усе гаразд, дякую за запитання."

        # Додаємо повідомлення до історії чату
        self.add_to_chat(user1_message, "Користувач 1")
        self.add_to_chat(user2_message, "Користувач 2")

        # Виведення історії чату
        self.display_chat_history()

        # Додаткова логіка за необхідності
        print("Комунікація успішна.")

    def add_to_chat(self, message, sender):
        # Додає повідомлення до історії чату
        self.chat_history.append({"sender": sender, "message": message})

    def display_chat_history(self):
        # Виводить історію чату
        print("Історія чату:")
        for entry in self.chat_history:
            print(f"{entry['sender']}: {entry['message']}")
