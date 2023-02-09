from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from random import choice
import string
from itertools import combinations_with_replacement


class Testeapp(MDApp):
    Window.size = (300, 600)

    def build(self):
        return Builder.load_file('telas/senha.kv')

    def tema_dark(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def get_data(self):
        valor = self.root.ids.quant.text
        tamanho = int(valor)
        valores = string.ascii_letters + string.digits
        senha = ''
        for i in range(tamanho):
            senha += choice(valores)
        dialog = MDDialog(
                text=senha)
        dialog.open()


Testeapp().run()
