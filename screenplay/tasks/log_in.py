from screenpy import Actor
from screenpy_playwright.actions import Click, Enter

from screenplay.ui.log_in_page import LogInPage


class LogIn:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor: Actor) -> None:
        """The actor attempts to log in using their credentials."""
        actor.attempts_to(
            Enter.the_text(self.username).into(LogInPage.USERNAME_FIELD),
            Enter.the_text(self.password).into(LogInPage.PASSWORD_FIELD),
            Click.on(LogInPage.LOGIN_BUTTON)
        )