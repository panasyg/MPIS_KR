import random

class AnalyticsService:
    def generate_report(self):
        # Логіка генерації та виведення звітів
        print("Генерація аналітичного звіту...")

        # Загальна кількість користувачів у системі
        total_users = random.randint(100, 1000)

        # Кількість активних користувачів
        active_users = random.randint(50, total_users)

        # Кількість створених даних у системі
        total_data = random.randint(500, 5000)

        # Середня кількість даних на користувача
        avg_data_per_user = total_data / total_users

        # Логіка додавання інших параметрів звіту за необхідності

        # Виведення результатів
        print(f"Загальна кількість користувачів: {total_users}")
        print(f"Кількість активних користувачів: {active_users}")
        print(f"Загальна кількість даних: {total_data}")
        print(f"Середня кількість даних на користувача: {avg_data_per_user:.2f}")

        # Додаткова логіка за необхідності
        print("Аналітичний звіт згенеровано успішно.")
