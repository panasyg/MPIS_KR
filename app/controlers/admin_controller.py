from app.services.data_management_service import DataManagementService
from app.services.analytics_service import AnalyticsService
from app.services.integration_service import IntegrationService
from app.services.security_service import SecurityService

class AdminController:
    def __init__(self):
        self.data_service = DataManagementService()
        self.analytics_service = AnalyticsService()
        self.integration_service = IntegrationService()
        self.security_service = SecurityService()

    def create_data(self, data):
        self.data_service.create_data(data)

    def generate_report(self):
        self.analytics_service.generate_report()

    def integrate_with_external_system(self):
        self.integration_service.integrate()

    def configure_security_parameters(self):
        self.security_service.configure_parameters()
