from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import pandas as pd
import numpy as np
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class TasklistApp(App):

    
    def build(self):
        self.df_tasks= pd.DataFrame(columns=["Task","Due Date","Status"])
        
        def import_task(instance):

            #new_task = {"Task":"Bu toolu bitirmek","Due Date": "01.12.2021","Status": "Started"}
            new_task = {"Task": str(textinput1.text),
                        "Due Date": str(textinput2.text),
                        "Status": str(textinput3.text)}
            self.df_tasks = add_task(new_task)
            print(self.df_tasks)
            return

        def add_task(new_task):
    
            #new_task = {"Task":"Bu toolu bitirmek","Due Date": "01.12.2021","Status": "Started"}
            self.df_tasks = self.df_tasks.append(new_task,ignore_index=True)
            #print(self.df_tasks)  
            #new_task = {"Task": str(textinput1.text),
            #            "Due Date": str(textinput2.text),
            #            "Status": str(textinput3.text)}
            return self.df_tasks

        def dataframes(instance):

            self.df_tasks= pd.DataFrame(columns=["Task","Due Date","Status"])            
            print(self.df_tasks)

            return

        def clear_tasks(instance):

            self.df_tasks= pd.DataFrame(columns=["Task","Due Date","Status"])
            print(self.df_tasks)

            return
        
        popup_box = BoxLayout(orientation='vertical')
        textinput1 = TextInput(text='', multiline=True)
        textinput2 = TextInput(text='', multiline=False)
        textinput3 = TextInput(text='', multiline=False)
              
        popup_box.add_widget(Label(text='Task'))
        popup_box.add_widget(textinput1)
        popup_box.add_widget(Label(text='Due Date'))
        popup_box.add_widget(textinput2)
        popup_box.add_widget(Label(text='Status'))
        popup_box.add_widget(textinput3)

        popup_box_button = Button(text='Add task')
        popup_box.add_widget(popup_box_button)

        popup2_box = GridLayout(cols = 3)
        popup2_box.add_widget(Label(text='Task'))
        popup2_box.add_widget(Label(text='Due Date'))
        popup2_box.add_widget(Label(text='Status'))
        for row,index in self.df_tasks.iterrows():
            popup2_box.add_widget(Label(text=str(row[0])))
            popup2_box.add_widget(Label(text=str(row[1])))
            popup2_box.add_widget(Label(text=str(row[2])))

        self.df_tasks = popup_box_button.bind(on_press=import_task)
        
        popup_box = Popup(title='Task List Menu', content=popup_box, size_hint=(None, None), size=(400, 400))
        popup2_box = Popup(title='Task List', content=popup2_box, size_hint=(None, None), size=(400, 400))       

        layout = BoxLayout(orientation='vertical')
        b1 = Button(text='Create Task List')
        b2 = Button(text='Add New Task')
        b3 = Button(text='Clear Task List')
        b4 = Button(text='Show Task List')
        b5 = Button(text='Close',background_color= (1, 0, 0, 1))

        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)
        layout.add_widget(b4)
        layout.add_widget(b5)

        b1.bind(on_press=dataframes)
        b2.bind(on_press=popup_box.open)
        b3.bind(on_release=clear_tasks)
        b4.bind(on_release=popup2_box.open)
        b5.bind(on_release=exit)

        return layout

        

TasklistApp().run()
