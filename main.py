from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import math

Window.size = (500, 750)


class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=4, rows=5)
        self.main_layout = BoxLayout(orientation='vertical', spacing=30)

        self.top_layout = BoxLayout()
        self.top_grid = GridLayout(cols=4, rows=5, row_force_default=True, row_default_height=60)

        self.calculation = TextInput(font_size=32, readonly=True, halign="right", multiline=False, size_hint_y=None,
                                     height=100)
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
            ('^x', self.exponentiation_but),
            ('√', self.root_extraction_but),
        ]

        buttons_top = [
            ('(', self.on_button_press),
            (')', self.on_button_press),
            ('C', self.on_clear)
        ]

        buttons_top2 = [
            ('sin', self.trig_but),
            ('cos', self.trig_but),
            ('tg', self.trig_but),
            ('ctg', self.trig_but),
            ('arcsin', self.trig_but),
            ('arccos', self.trig_but),
            ('arctg', self.trig_but),
            ('arcctg', self.trig_but),
        ]

        for label, func in buttons_middle:
            button = Button(text=label, font_size=32)
            button.bind(on_press=func)
            layout.add_widget(button)

        for label, func in buttons_top:
            button = Button(text=label, font_size=32, size_hint_y=None,
                            height=60)
            button.bind(on_press=func)
            self.top_layout.add_widget(button)

        for label, func in buttons_top2:
            button = Button(text=label, font_size=32)
            button.bind(on_press=func)
            self.top_grid.add_widget(button)

        self.return_button = Button(text='del', font_size=32, size_hint_y=None,
                                    height=60)
        self.return_button.bind(on_press=self.del_but)
        self.top_layout.add_widget(self.return_button)

        self.main_layout.add_widget(self.top_layout)
        self.main_layout.add_widget(self.top_grid)
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
        print(self.func_text)

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

    def trig_but(self, instance):
        if self.error == 1:
            self.calculation.text = ''
        current = self.calculation.text
        current_func = self.func_text
        button_text1 = f'math.{instance.text}('
        button_text2 = f'{instance.text}('
        new_text_calculation = current + button_text2
        new_text_func = current + button_text1
        self.calculation.text = new_text_calculation
        self.func_text = new_text_func
        self.error = 0
        print(self.func_text)

    def exponentiation_but(self, instance):
        if self.error == 1:
            self.calculation.text = ''
        current = self.calculation.text
        current_func = self.func_text
        button_text1 = f'**'
        button_text2 = f'^'
        new_text_calculation = current + button_text2
        new_text_func = current + button_text1
        self.calculation.text = new_text_calculation
        self.func_text = new_text_func
        self.error = 0
        print(self.func_text)

    def root_extraction_but(self, instance):
        if self.error == 1:
            self.calculation.text = ''
        current = self.calculation.text
        current_func = self.func_text
        button_text1 = f'**0.5'
        button_text2 = f'^½'
        new_text_calculation = current + button_text2
        new_text_func = current + button_text1
        self.calculation.text = new_text_calculation
        self.func_text = new_text_func
        self.error = 0
        print(self.func_text)


if __name__ == "__main__":
    CalculatorApp().run()
