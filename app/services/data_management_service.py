
from app.models.data_model import DataModel

class DataManagementService:
    def __init__(self):
        self.data_list = []

    def create_data(self, data):
        new_data = DataModel(data)
        self.data_list.append(new_data)
        print(f"Data {data} created successfully.")

    def edit_data(self, old_data, new_data):
        for data in self.data_list:
            if data.data == old_data:
                data.data = new_data
                print(f"Data {old_data} edited successfully.")
                return
        print(f"Data {old_data} not found.")

    def delete_data(self, data):
        for item in self.data_list:
            if item.data == data:
                self.data_list.remove(item)
                print(f"Data {data} deleted successfully.")
                return
        print(f"Data {data} not found.")

    def search_data(self, keyword):
        results = [data.data for data in self.data_list if keyword.lower() in data.data.lower()]
        print(f"Search results for '{keyword}': {results}")
