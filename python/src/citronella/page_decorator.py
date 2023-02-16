from .web_ui import WebUi

class PageDecorator:
    """This is a decorator class."""
    def __init__(self, driver, webdriver_wait, pages):
        self.cls = pages.current_page()
        self.driver = driver
        self.pages = pages
        self.webdriver_wait = webdriver_wait

    def __getattr__(self,attr):
        cls_attr = self.cls.__getattribute__(attr)
        if callable(cls_attr):
            def wrap(*args, **kwargs):
                """This is a wrapper function."""
                f = cls_attr(*args, **kwargs)
                return WebUi(self.driver, self.webdriver_wait, self.pages,
                          f['by'], f['value'], f['page'], attr,
                          self.cls.__class__.__name__)

                #cls._driver = self.driver
                #cls._pages = self.setter
                #cls._function_name = attr
                #cls._class_name = self.cls.__class__.__name__
                #cls._wait = self.webdriver_wait
                #if cls == self.cls:
                #    return self

                #return ui

            return wrap()

        #else:
        #    return cls_attr
