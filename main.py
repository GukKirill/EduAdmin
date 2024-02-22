from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from schedule_screen import ScheduleScreen
from groups_screen import GroupsScreen
from students_screen import StudentsScreen
from payment_screen import PaymentScreen
from statistics_screen import StatisticsScreen


class EduAdminApp(App):
    def build(self):
        #current_screen =
        sm = ScreenManager()
        sm.add_widget(ScheduleScreen(name='schedule_screen'))
        sm.add_widget(GroupsScreen(name='groups_screen'))
        sm.add_widget(StudentsScreen(name='students_screen'))
        sm.add_widget(PaymentScreen(name='payment_screen'))
        sm.add_widget(StatisticsScreen(name='statistics_screen'))

        return sm


if __name__ == "__main__":
    EduAdminApp().run()
