from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

class TaskScreen(Screen):
    def __init__(self, name='tasks'):
        super().__init__(name=name)
        self.id = 0
        btn = Button(text='Добавить задачу')
        btn.on_press = self.add_task
        vl = BoxLayout(orientation='vertical')
        self.tasks_lay = BoxLayout(orientation='vertical')
        vl.add_widget(self.tasks_lay)
        vl.add_widget(btn)
        self.add_widget(vl)
    def add_task(self):
        vl = BoxLayout(orientation='vertical')
        self.task_input = TextInput()
        btn = Button(text='OK')
        btn.on_press = self.close_popup
        vl.add_widget(self.task_input)
        vl.add_widget(btn)
        self.popup = Popup(title='Задача', content=vl, auto_dismiss=False)
        self.popup.open()
    def close_popup(self):
        self.id += 1
        task = Task(text=self.task_input.text, task_id=self.id, remove_task=self.del_task)
        self.tasks_lay.add_widget(task)
        self.popup.dismiss()
    
    def del_task(self, task):
        self.tasks_lay.remove_widget(task)


class Task(BoxLayout):
    def __init__(self, text, task_id, remove_task):
        super().__init__()
        self.task_id = task_id
        self.ok_btn = Button(text='OK')
        self.del_btn = Button(text='X')
        task_lbl = Label(text=text)
        self.add_widget(task_lbl)
        self.add_widget(self.ok_btn)
        self.add_widget(self.del_btn)
        self.del_btn.on_press = lambda: remove_task(self)
class TaskApp(App):
    def build(self):
        scr = TaskScreen()
        return scr

app = TaskApp()
app.run()