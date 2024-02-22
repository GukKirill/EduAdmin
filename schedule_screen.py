from screen_template import ScreenTemplate
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ScheduleScreen(ScreenTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def _create_schedule_display(self):
        schedule_display = BoxLayout(orientation="horizontal",
                                     size_hint=(0.825, 1),
                                     )
        return schedule_display

    def _create_info_display(self):
        info_display = BoxLayout(orientation="vertical")
        return info_display
