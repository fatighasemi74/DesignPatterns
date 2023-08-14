from observer.decorators import notify_observers
from observer.notification import EmailNotification, SMSNotification, PushNotification

class Product:
    pass

class Payment:
    observers = [PushNotification, SMSNotification]

    @notify_observers(message="purchase paid")
    def checkout(self):
        pass

class Purchase:
    observer = [EmailNotification, SMSNotification, PushNotification]

    def __init__(self, product_list):
        self.product = product_list
        self.payment = Payment()

    def checkout(self):
        self.payment.checkout()

    @notify_observers(message="purchase canceled")
    def cancel(self):
        pass