from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from schedule_screen import ScheduleScreen
from groups_screen import GroupsScreen
from students_screen import StudentsScreen


class EduAdminApp(App):
    def build(self):
        #current_screen =
        sm = ScreenManager()
        sm.add_widget(ScheduleScreen(name='schedule_screen'))
        sm.add_widget(GroupsScreen(name='groups_screen'))
        sm.add_widget(StudentsScreen(name='students_screen'))

        return sm


if __name__ == "__main__":
    EduAdminApp().run()
