# Page Object Design / Strategy

Usually, when importing a module, you can simply import it at the top of the file. However, in this situation, the module is forced to be imported inside the module due to circular import issues, like this:

```python
from selenium.webdriver.common.by import By
from citronella import ui


class Header:
    def home_page_icon_menu(self):
        from Pages.home.home_page import HomePage
        return ui(By.CLASS_NAME, 'site-header__logo', HomePage)

    def help_button(self):
        from Pages.help.help_page import HelpPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', HelpPage)

    def sponsors_button(self):
        from Pages.sponsors.sponsors_page import SponsorPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', SponsorPage)

    def login_button(self):
        from Pages.account.login.login_page import LoginPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', LoginPage)

    def register_button(self):
        from Pages.account.register.register_page import RegisterPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', RegisterPage)

    def search_input(self):
        from Pages.search.search_page import SearchPage
        return ui(By.ID, 'search', SearchPage)

    def search_button(self):
        from Pages.search.search_page import SearchPage
        return ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)
```

There's an alternative to make it more reusable, like this:
```python
class Module:

    def home_page():
        from Pages.home.home_page import HomePage
        return HomePage

    def search_page():
        from Pages.search.search_page import SearchPage
        return SearchPage

    def help_page():
        from Pages.help.help_page import HelpPage
        return HelpPage

    def sponsors_page():
        from Pages.sponsors.sponsors_page import SponsorPage
        return SponsorPage

    def login_page():
        from Pages.account.login.login_page import LoginPage
        return LoginPage

    def register_page():
        from Pages.account.register.register_page import RegisterPage
        return RegisterPage

    def sitemap_page():
        from Pages.sitemap.sitemap_page import SiteMapPage
        return SiteMapPage

    def projects_page():
        from Pages.manage.projects.projects_page import ProjectsPage
        return ProjectsPage
```

```python
from selenium.webdriver.common.by import By
from citronella import ui
from Pages.module import Module


class Header:
    def home_page_icon_menu(self):
        return ui(By.CLASS_NAME, 'site-header__logo', Module.home_page())

    def help_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', Module.help_page())

    def sponsors_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', Module.sponsors_page())

    def login_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', Module.login_page())

    def register_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', Module.register_page())

    def search_input(self):
        return ui(By.ID, 'search', Module.search_page())

    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', Module.search_page())
```


There may also be an alternative way to import the module, such as using the `importlib` library, etc.
