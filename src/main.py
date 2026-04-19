from textual.app import App, ComposeResult
from textual.widgets import Label, Checkbox, Digits
from textual.containers import HorizontalGroup, VerticalScroll

class CountDown(Digits):
    """ A widget to display time remaining until deadline """

class Task(HorizontalGroup):
    """ A task to-do """

    def compose(self) -> ComposeResult:
        """ Create child-widgets of an task """
        yield Checkbox()
        yield Label("Test Title for TODO")
        yield CountDown("00:00:00")


class TODOTUI(App):
    """ A textual app to manage tasks"""
    def compose(self) -> ComposeResult:
        """ Create child widgets for the app """
        yield VerticalScroll(Task(), Task(), Task())

if __name__ == "__main__":
    app = TODOTUI()
    app.run()
