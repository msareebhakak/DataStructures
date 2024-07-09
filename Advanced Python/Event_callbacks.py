class Event:
    def __init__(self):
        self.__callbacks = []

    def notify(self, *args, **kwargs):
        for callback in self.__callbacks:
            callback(*args, **kwargs)

    def __iadd__(self, callback):
        self.__callbacks.append(callback)
        return self

    def __isub__(self, callback):
        self.__callbacks.remove(callback)
        return self


class MyClass:
    def __init__(self, value):
        self.value = value
        self.on_add = Event()
        self.on_sub = Event()

    def __add__(self, other):
        result = MyClass(self.value + other.value)
        self.on_add.notify(self, other, result)
        return result

    def __sub__(self, other):
        result = MyClass(self.value - other.value)
        self.on_sub.notify(self, other, result)
        return result


if __name__ == '__main__':

    def on_add_callback(self, other, result):
        print(f"{self.value} + {other.value} = {result.value}")

    def on_sub_callback(self, other, result):
        print(f"{self.value} - {other.value} = {result.value}")

    a = MyClass(10)
    b = MyClass(5)

    # Use the += operator to subscribe to events
    a.on_add += on_add_callback
    a.on_sub += on_sub_callback

    # Perform operations to trigger callbacks
    c = a + b  # Should trigger on_add_callback
    d = a - b  # Should trigger on_sub_callback
