from screenpy import Actor
from screenpy_playwright.actions import Click, Enter
from screenpy_playwright.target import Target

# Define the UI Targets
USERNAME_FIELD = Target.the("username field").located_by("input[name='username']")
PASSWORD_FIELD = Target.the("password field").located_by("input[name='password']")
LOGIN_BUTTON = Target.the("login button").located_by("input[value='Log In']")

class LogIn:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor: Actor) -> None:
        """The actor attempts to log in using their credentials."""
        actor.attempts_to(
            Enter.the_text(self.username).into(USERNAME_FIELD),
            Enter.the_text(self.password).into(PASSWORD_FIELD),
            Click.on(LOGIN_BUTTON)
        )