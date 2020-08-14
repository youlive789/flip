from kivy.app import App
from view.mainview import MainView
from viewmodel.mainviewmodel import MainViewModel

from kivy.config import Config
Config.set('graphics','borderless',1)
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '350')

class FlipApp(App):
    def build(self):
        self.main_view_model = MainViewModel()
        return MainView()

if __name__ == "__main__":
    FlipApp().run()