from abc import ABC, abstractmethod


class IUserService(ABC):
    @staticmethod
    @abstractmethod
    def create_profile(cleaned_data: dict):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def save_profile(username: str, password: str):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def change_password(user, new_password: str):
        raise NotImplementedError


class IRegistrationService(ABC):
    @staticmethod
    @abstractmethod
    def register(cleaned_data: dict):
        raise NotImplementedError
