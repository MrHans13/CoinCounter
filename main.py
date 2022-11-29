from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1280')


class MainView(FloatLayout):
    def __init__(self):
        super(MainView, self).__init__()


class ViewOne(FloatLayout):
    def __init__(self):
        super(ViewOne, self).__init__()


class ViewTwo(FloatLayout):
    def __init__(self):
        super(ViewTwo, self).__init__()


class CoinCounter(App):
    def __init__(self):
        super().__init__()
        self.sm, self.main_view, self.view_one, self.view_two = (None,) * 4

    def build(self):
        self.sm = ScreenManager()

        self.main_view = MainView()
        screen = Screen(name="mainview")
        screen.add_widget(self.main_view)
        self.sm.add_widget(screen)

        self.view_one = ViewOne()
        screen = Screen(name="viewone")
        screen.add_widget(self.view_one)
        self.sm.add_widget(screen)

        self.view_two = ViewTwo()
        screen = Screen(name="viewtwo")
        screen.add_widget(self.view_two)
        self.sm.add_widget(screen)

        return self.sm

    @staticmethod
    def change_view(view, slide):
        """change to window level one"""
        app.sm.transition.direction = slide
        app.sm.current = view


if __name__ == "__main__":
    app = CoinCounter()
    app.run()
