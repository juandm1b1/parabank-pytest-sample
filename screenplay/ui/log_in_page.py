from screenpy_playwright.target import Target

class LogInPage:
    
    USERNAME_FIELD = Target.the("username field").located_by("input[name='username']")
    PASSWORD_FIELD = Target.the("password field").located_by("input[name='password']")
    LOGIN_BUTTON = Target.the("login button").located_by("input[value='Log In']")