from app.controllers.user_controller import UserController
from app.controllers.admin_controller import AdminController

# Використання:
if __name__ == "__main__":
    # Реєстрація / Авторизація
    user_controller = UserController()
    user_controller.register_user("username", "password")
    user_controller.login("username", "password")

    # Управління даними
    user_controller.create_data("data1")
    user_controller.edit_data("data1", "updated_data")
    user_controller.delete_data("data1")
    user_controller.search_data("keyword")

    admin_controller = AdminController()
    admin_controller.create_data("admin_data")

    # Аналітика та звітність
    admin_controller.generate_report()

    # Інтеграція з іншими системами
    admin_controller.integrate_with_external_system()

    # Безпека
    admin_controller.configure_security_parameters()

    # Співпраця та комунікація
    user_controller.communicate_with_other_users()

    # Персоналізація
    user_controller.personalize_system()
