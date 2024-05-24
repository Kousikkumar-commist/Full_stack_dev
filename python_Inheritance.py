class front_page:
    _hi="kousik"
    def __init__(self):
        print(self._hi)
class back_page(front_page):
    __fi="kumar"
    def __init__(self):
        print(self._hi)
        print(self.__fi)
class page(back_page):
    def __init__(self):
        print(self._hi)
        print(self.__fi)
page()