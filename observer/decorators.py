def notify_observers(message=''):
    def decorated_method(func):
        def wrapped(obj, *args, **kwargs):
            result = func(obj, *args, **kwargs)
            for observer in obj.observers:
                observer.send(message)
            return result

    return decorated_method