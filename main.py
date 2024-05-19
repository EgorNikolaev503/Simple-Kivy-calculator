from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=4, rows=5)

        self.calculation = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        layout.add_widget(self.calculation)

        buttons = [
            ('7', self.on_button_press),
            ('8', self.on_button_press),
            ('9', self.on_button_press),
            ('/', self.on_button_press),
            ('4', self.on_button_press),
            ('5', self.on_button_press),
            ('6', self.on_button_press),
            ('*', self.on_button_press),
            ('1', self.on_button_press),
            ('2', self.on_button_press),
            ('3', self.on_button_press),
            ('-', self.on_button_press),
            ('0', self.on_button_press),
            ('.', self.on_button_press),
            ('+', self.on_button_press),
            ('=', self.on_solution),
            ('C', self.on_clear),
        ]

        for label, func in buttons:
            button = Button(text=label, font_size=32)
            button.bind(on_press=func)
            layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        current = self.calculation.text
        button_text = instance.text
        new_text = current + button_text
        self.calculation.text = new_text

    def on_solution(self, instance):
        try:
            text = self.calculation.text
            self.calculation.text = str(eval(text))
        except Exception:
            self.calculation.text = "Error"

    def on_clear(self, instance):
        self.calculation.text = ''


if __name__ == "__main__":
    CalculatorApp().run()
