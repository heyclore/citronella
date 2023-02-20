from .web_ui import WebUi

class PageDecorator:
    """This is a decorator class."""
    def __init__(self, driver, webdriver_wait, pages, logger):
        self.cls = pages.current_page()
        self.driver = driver
        self.pages = pages
        self.logger = logger
        self.webdriver_wait = webdriver_wait

    def __getattr__(self,attr):
        cls_attr = self.cls.__getattribute__(attr)
        if callable(cls_attr):
            def wrap(*args, **kwargs):
                """This is a wrapper function."""
                f = cls_attr(*args, **kwargs)
                return WebUi(self.driver, self.webdriver_wait, self.pages,
                             self.logger, f['by'], f['value'], f['page'], attr,
                             self.cls.__class__.__name__)

            return wrap()
