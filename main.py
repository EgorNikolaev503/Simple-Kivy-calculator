from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=4, rows=5)
        self.main_layout = BoxLayout(orientation='vertical')

        self.top_layout = BoxLayout()

        self.calculation = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.main_layout.add_widget(self.calculation)
        self.func_text = ''
        self.error = 0

        buttons_middle = [
            ('1', self.on_button_press),
            ('2', self.on_button_press),
            ('3', self.on_button_press),
            ('/', self.on_button_press),
            ('4', self.on_button_press),
            ('5', self.on_button_press),
            ('6', self.on_button_press),
            ('*', self.on_button_press),
            ('7', self.on_button_press),
            ('8', self.on_button_press),
            ('9', self.on_button_press),
            ('-', self.on_button_press),
            ('0', self.on_button_press),
            ('.', self.on_button_press),
            ('+', self.on_button_press),
            ('=', self.on_solution),
            ('C', self.on_clear),
            ('(', self.on_button_press),
            (')', self.on_button_press)
        ]

        for label, func in buttons_middle:
            button = Button(text=label, font_size=32)
            button.bind(on_press=func)
            layout.add_widget(button)

        self.return_button = Button(text='del', font_size=32)
        self.return_button.bind(on_press=self.del_but)
        layout.add_widget(self.return_button)

        self.main_layout.add_widget(layout)

        return self.main_layout

    def on_button_press(self, instance):
        if self.error == 1:
            self.calculation.text = ''
        current = self.calculation.text
        current_func = self.func_text
        button_text = instance.text
        new_text = current + button_text
        self.calculation.text = new_text
        self.func_text = current_func + button_text
        self.error = 0

    def on_solution(self, instance):
        try:
            text = self.func_text
            self.calculation.text = str(eval(text))
            self.func_text = str(eval(text))
        except ZeroDivisionError:
            self.calculation.text = "Division by zero !"
            self.error = 1
        except Exception:
            self.calculation.text = "Error"
            self.error = 1

    def on_clear(self, instance):
        self.calculation.text = ''
        self.func_text = ''

    def del_but(self, *args):
        self.calculation.text = self.calculation.text[0:-1]
        self.func_text = self.func_text[0:-1]


if __name__ == "__main__":
    CalculatorApp().run()
