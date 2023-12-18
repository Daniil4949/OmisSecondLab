from abc import ABC, abstractmethod


class IBudgetService(ABC):
    @staticmethod
    @abstractmethod
    def create_instance(cleaned_data: dict):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_info():
        raise NotImplementedError
