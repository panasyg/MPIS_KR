class SecurityService:
    def configure_parameters(self):
        # Логіка налаштування параметрів безпеки
        print("Налаштування параметрів безпеки...")

        # Фіктивні параметри безпеки для прикладу
        password_complexity = True
        two_factor_authentication = False
        encryption_enabled = True

        # Перевірка та вивід налаштувань
        if password_complexity:
            print("Вимагається складний пароль.")
        else:
            print("Складний пароль необов'язковий.")

        if two_factor_authentication:
            print("Включений двоетапний аутентифікацій.")
        else:
            print("Двоетапний аутентифікацій вимкнений.")

        if encryption_enabled:
            print("Включено шифрування даних.")
        else:
            print("Шифрування даних вимкнене.")

        # Додаткова логіка за необхідності
        print("Параметри безпеки налаштовано успішно.")
