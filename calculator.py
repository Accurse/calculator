from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 270)
Config.set("graphics", "height", 480)

count = 0
operations = ["/", "*", "+", "-"]
set(operations)

def checkSymbol(text):
    if text == "÷":
        return "/"
    elif text == "×":
        return "*"
    else:
        return text


def isThereAnError(text):
    if text == "ERROR":
        return True
    return False


class BoxApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text="", font_size=40, halign="right", size_hint=(1, 0.4), text_size=(270, 50))
        self.formula = ""

    def operativeSymbolsBehaviour(self, text):
        if isThereAnError(self.formula) is True:
            self.formula = ""
            self.updateLabel()
        elif self.formula != "":
            if self.formula[-1].isdigit() is True:
                self.addTextToLabel(text)
            else:
                self.changeLastSymbol(text)

    def changeLastSymbol(self, text):
        self.formula = self.formula[:-1]
        self.formula += str(text)
        self.updateLabel()

    def addNumber(self, instance):
        if isThereAnError(self.formula) is True:
            self.formula = ""
            self.updateLabel()
        self.formula += str(instance.text)
        self.updateLabel()

    def addTextToLabel(self, text):
        self.formula += str(text)
        self.updateLabel()

    def deleteAll(self, instance):
        self.formula = ""
        self.updateLabel()

    def deleteOneSymbol(self, instance):
        if isThereAnError(self.formula) is True:
            self.formula = ""
            self.updateLabel()
        elif self.formula != "":
            self.formula = self.formula[:-1]
            self.updateLabel()

    def updateLabel(self):
        self.lbl.text = self.formula

    def multiplication(self, instance):
        self.operativeSymbolsBehaviour(instance.text)

    def division(self, instance):
        self.operativeSymbolsBehaviour(instance.text)

    def subtraction(self, instance):
        self.operativeSymbolsBehaviour(instance.text)

    def addition(self, instance):
        self.operativeSymbolsBehaviour(instance.text)

    def addPoint(self, instance):
        count = 1
        for i in self.formula:
            if i in operations:
                count += 1
            elif i == ".":
                count -= 1
        if self.formula != "":
            if self.formula[-1].isdigit() is True:
                if count > 0:
                    self.addTextToLabel(instance.text)
                    count -= 1

    def calculate(self, instance):
        if self.formula != "" and isThereAnError(self.formula) is False:
            while self.formula[-1].isdigit() is False:
                self.formula = self.formula[:-1]
                self.updateLabel()
            try:
                self.formula = str(eval(self.formula))
                self.updateLabel()
            except SyntaxError:
                self.formula = "ERROR"
                self.updateLabel()
            except NameError:
                self.formula = "ERROR"
                self.updateLabel()

    def build(self):
        bl = BoxLayout(orientation="vertical")
        gl = GridLayout(cols=4, rows=5)
        bl.add_widget(self.lbl)
        gl.add_widget(Button(text="CE", on_press=self.deleteOneSymbol))
        gl.add_widget(Button(text="C", on_press=self.deleteAll))
        gl.add_widget(Button(text=""))
        gl.add_widget(Button(text="/", on_press=self.division))
        gl.add_widget(Button(text="7", on_press=self.addNumber))
        gl.add_widget(Button(text="8", on_press=self.addNumber))
        gl.add_widget(Button(text="9", on_press=self.addNumber))
        gl.add_widget(Button(text="*", on_press=self.multiplication))
        gl.add_widget(Button(text="4", on_press=self.addNumber))
        gl.add_widget(Button(text="5", on_press=self.addNumber))
        gl.add_widget(Button(text="6", on_press=self.addNumber))
        gl.add_widget(Button(text="-", on_press=self.subtraction))
        gl.add_widget(Button(text="1", on_press=self.addNumber))
        gl.add_widget(Button(text="2", on_press=self.addNumber))
        gl.add_widget(Button(text="3", on_press=self.addNumber))
        gl.add_widget(Button(text="+", on_press=self.addition))
        gl.add_widget(Button(text=""))
        gl.add_widget(Button(text="0", on_press=self.addNumber))
        gl.add_widget(Button(text=".", on_press=self.addPoint))
        gl.add_widget(Button(text="=", on_press=self.calculate))
        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    BoxApp().run()
