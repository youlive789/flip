from kivy.app import App
from kivy.core.window import Window
from view.mainview import MainView
from viewmodel.mainviewmodel import MainViewModel

class FlipApp(App):
    def build(self):
        Window.size = (200,350)
        self.main_view_model = MainViewModel()
        return MainView()

if __name__ == "__main__":
    FlipApp().run()