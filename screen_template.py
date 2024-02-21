from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScreenTemplate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boxlayout = BoxLayout(orientation="horizontal", spacing=5, padding=[10])

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

        self.boxlayout.add_widget(button_schedule)
        self.boxlayout.add_widget(button_groups)
        self.boxlayout.add_widget(button_students)
        self.add_widget(self.boxlayout)

    def _get_bl(self):
        return self.boxlayout

    def _on_press_button_schedule(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'schedule_screen'

    def _on_press_button_groups(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'groups_screen'

    def _on_press_button_students(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'students_screen'
