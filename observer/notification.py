from abc import ABC, abstractmethod

class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass

class EmailNotification(Observer):
    @staticmethod
    def send(cls, message=''):
        print(f"Sending email message {message}")

class SMSNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"send sms message {message}")

class PushNotification(Observer):
    @staticmethod
    def send(message=''):
        print(f"send push notification {message}")