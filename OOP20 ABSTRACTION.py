from abc import ABC,abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("push button clicked")

class RadioButton(Button):
    def click(self):
        print("radio button clicked")


button1=PushButton()
button1.click()

button2=RadioButton()
button2.click()

# button3=Button() --> tidak dapat diimplementasikan
# button3.click()