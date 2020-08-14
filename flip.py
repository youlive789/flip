from kivy.app import App
from view.mainview import MainView
from viewmodel.mainviewmodel import MainViewModel

class FlipApp(App):
    def build(self):
        self.main_view_model = MainViewModel()
        return MainView()

if __name__ == "__main__":
    FlipApp().run()