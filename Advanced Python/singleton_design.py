from abc import ABCMeta


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class IPerson(ABCMeta):

    @staticmethod
    def get_data():
        """Implement in inheritance"""


if __name__ == '__main__':
    # Usage
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # True
