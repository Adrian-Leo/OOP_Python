from abc import ABC,abstractmethod

class Button(ABC):
    def __init__(self,inputLink):
        self.link=inputLink

    def __str__(self):
        return  self.link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    def click(self):
        print("go to : {}".format(self.link))

    @Button.link.setter
    def link(self,input):
        self.__link=input

    @link.getter
    def link(self):
        return self.__link

tombol1=PushButton("www.google.com")
print(tombol1)
print(tombol1.link)
