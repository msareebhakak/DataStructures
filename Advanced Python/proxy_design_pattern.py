from abc import ABCMeta, abstractstaticmethod


# Example 1
class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        """Interface method"""


class Person(IPerson):

    def person_method(self):
        print("I am a person")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()


# Example 2
class ProtectedResource:
    @staticmethod
    def access_resource():
        return "ProtectedResource: Access granted"


class Proxy:
    def __init__(self):
        self._protected_resource = ProtectedResource()
        self._access_granted = False

    def authenticate(self, password):
        if password == "secret":
            self._access_granted = True
        else:
            self._access_granted = False

    def access_resource(self):
        if self._access_granted:
            return self._protected_resource.access_resource()
        else:
            return "Proxy: Access denied. Authentication required."


if __name__ == '__main__':
    p1 = Person()
    p1.person_method()

    p2 = ProxyPerson()
    p2.person_method()

    proxy = Proxy()

    print(proxy.access_resource())  # Without authentication

    proxy.authenticate("password")
    print(proxy.access_resource())  # With wrong password

    proxy.authenticate("secret")
    print(proxy.access_resource())  # With correct password
