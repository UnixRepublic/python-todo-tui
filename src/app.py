from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, Checkbox, Digits, Footer
from textual.containers import HorizontalGroup, VerticalScroll

class CountDown(Digits):
    """ A widget to display time remaining until deadline """

class CreateNewTaskScreen(ModalScreen):
    """ Screen with a form to create a new task """

    BINDINGS = [("Q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Label("TO DO IRONICALLY")

    def action_quit(self) -> None:
        self.app.pop_screen()

class Task(HorizontalGroup):
    """ A task to-do """

    def compose(self) -> ComposeResult:
        """ Create child-widgets of an task """
        yield Checkbox()
        yield Label("Test Title for TODO")
        yield CountDown("00:00:00")

class TODOTUI(App):
    """ A textual app to manage tasks"""

    BINDINGS = [("Q", "quit", "Quit"), ("N", "create_new_task", "Create new task")]

    def compose(self) -> ComposeResult:
        """ Create child widgets for the app """
        yield Footer()
        yield VerticalScroll(Task(), Task(), Task())

    def action_quit(self) -> None:
        """ An action to quit the app """
        self.exit(0)

    def action_create_new_task(self) -> None:
        self.push_screen(CreateNewTaskScreen())


if __name__ == "__main__":
    app = TODOTUI()
    app.run()
