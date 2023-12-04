import requests

class IntegrationService:
    def integrate(self):
        # Логіка інтеграції з зовнішньою системою
        print("Інтеграція з зовнішньою системою...")

        # Припустимо, що це URL зовнішньої системи
        external_system_url = "https://example.com/api/data"

        # Спроба взяти дані з зовнішньої системи
        try:
            response = requests.get(external_system_url)

            if response.status_code == 200:
                # Обробка отриманих даних
                data_from_external_system = response.json()
                print(f"Дані з зовнішньої системи: {data_from_external_system}")
            else:
                print(f"Не вдалося отримати дані. Помилка {response.status_code}")
        except Exception as e:
            print(f"Помилка під час інтеграції: {str(e)}")

        # Додаткова логіка за необхідності
        print("Інтеграція успішна.")
