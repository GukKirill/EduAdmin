from kivy.uix.screenmanager import ScreenManager, Screen
from screen_template import ScreenTemplate
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScheduleScreen(ScreenTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = super()._get_bl()
        boxlayout2 = BoxLayout(orientation="horizontal", spacing=5, padding=[10])

        button_schedule = Button(
            text="Расписание",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_schedule,
        )
        button_groups = Button(
            text="Группы",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_groups,
        )
        button_students = Button(
            text="Студенты",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_students,
        )

        boxlayout2.add_widget(button_schedule)
        boxlayout2.add_widget(button_groups)
        boxlayout2.add_widget(button_students)
        boxlayout.add_widget(boxlayout2)

    def _on_press_button_schedule(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'schedule_screen'

    def _on_press_button_groups(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'groups_screen'

    def _on_press_button_students(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'students_screen'


        # boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        # tm = TopMenu()
        # boxlayout.add_widget(tm)
        # tm2 = TopMenu()
        # boxlayout.add_widget(tm2)
        # self.add_widget(boxlayout)
    #     boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
    #
    #     button_new_pasword = Button(
    #         text="New Pasword",
    #         background_color=[0, 1.5, 3, 1],
    #         size_hint=[1, 0.1],
    #         on_press=self._on_press_button_new_pasword,
    #     )
    #
    #     boxlayout.add_widget(button_new_pasword)
    #     self.add_widget(boxlayout)
    #
    # def _on_press_button_new_pasword(self, *args):
    #     self.manager.transition.direction = 'left'
    #     self.manager.current = 'lenpasword'
