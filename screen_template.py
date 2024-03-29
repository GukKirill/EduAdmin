from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ScreenTemplate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_box = self._create_main_box()
        self.top_menu = self._create_top_menu()
        self.working_space = self._create_working_space()
        self.bottom_info = self._create_bottom_info()
        self.main_box.add_widget(self.top_menu)
        self.main_box.add_widget(self.working_space)
        self.main_box.add_widget(self.bottom_info)
        self.add_widget(self.main_box)

    def _create_main_box(self):
        main_box = BoxLayout(orientation="vertical",
                             spacing=1,
                             padding=[2],
                             )
        return main_box

    def _create_top_menu(self):
        top_menu = BoxLayout(orientation="horizontal",
                             size_hint=(1, 0.03),
                             )
        menu_buttons = {"schedule": ("Расписание", self._on_press_button_schedule),
                        "groups": ("Группы", self._on_press_button_groups),
                        "students": ("Студенты", self._on_press_button_students),
                        "payment": ("Оплата", self._on_press_button_payment),
                        "statistics": ("Статистика", self._on_press_button_statistics),
                        }

        for screen, value in menu_buttons.items():
            button = Button(
                text=value[0],
                background_color=[2, 1.5, 3, 1],
                on_press=value[1],
                )
            top_menu.add_widget(button)
        return top_menu

    def _create_working_space(self):
        working_space = BoxLayout(orientation="horizontal",
                                  spacing=1,
                                  )
        info_display = BoxLayout(orientation="horizontal",
                                 size_hint=(0.85, 1),
                                 )
        info_display.add_widget(ColoredLabel((255, 255, 255, 1),
                                             text="info",
                                             color=(0, 0, 0, 1),
                                             ))
        control_display = BoxLayout(orientation="vertical",
                                    size_hint=(0.15, 1),
                                    )
        control_display.add_widget(ColoredLabel((255, 255, 255, 1),
                                                text="control",
                                                color=(0, 0, 0, 1),
                                                ))
        working_space.add_widget(info_display)
        working_space.add_widget(control_display)
        return working_space

    def _create_bottom_info(self):
        bottom_info = ColoredLabel((255, 255, 255, 1),
                                   text="info about nearest lesson",
                                   size_hint=(1, 0.03),
                                   color=(0, 0, 0, 1),
                                   )
        return bottom_info

    def _get_working_space(self):
        return self.working_space

    def _on_press_button_schedule(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'schedule_screen'

    def _on_press_button_groups(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'groups_screen'

    def _on_press_button_students(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'students_screen'

    def _on_press_button_payment(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'payment_screen'

    def _on_press_button_statistics(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'statistics_screen'


class ColoredLabel(Label):
    def __init__(self, background_color: tuple, **kwargs) -> None:
        super().__init__(**kwargs)
        self.background_color = background_color

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)
