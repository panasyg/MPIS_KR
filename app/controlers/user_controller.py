from app.services.authentication_service import AuthenticationService
from app.services.data_management_service import DataManagementService
from app.services.communication_service import CommunicationService

class UserController:
    def __init__(self):
        self.auth_service = AuthenticationService()
        self.data_service = DataManagementService()
        self.communication_service = CommunicationService()

    def register_user(self, username, password):
        self.auth_service.register_user(username, password)

    def login(self, username, password):
        self.auth_service.login(username, password)

    def create_data(self, data):
        self.data_service.create_data(data)

    def edit_data(self, old_data, new_data):
        self.data_service.edit_data(old_data, new_data)

    def delete_data(self, data):
        self.data_service.delete_data(data)

    def search_data(self, keyword):
        self.data_service.search_data(keyword)

    def communicate_with_other_users(self):
        self.communication_service.communicate()

    def personalize_system(self):
        # Логіка персоналізації
        pass
