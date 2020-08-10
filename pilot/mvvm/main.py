from kivy.app import App
from viewmodels.helloviewmodel import HelloViewModel
from views.helloview import HelloView

class HelloApp(App):
    def build(self):
        self.hello_view_model = HelloViewModel()
        return HelloView()

if __name__ == "__main__":
    HelloApp().run()