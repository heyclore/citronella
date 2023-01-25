class PageDecorator:
    """This is a decorator class."""
    def __init__(self, cls, driver, setter, webdriver_wait):
        self.cls = cls()
        self.driver = driver
        self.setter = setter
        self.webdriver_wait = webdriver_wait

    def __getattr__(self,attr):
        cls_attr = self.cls.__getattribute__(attr)
        if callable(cls_attr):
            def wrap(*args, **kwargs):
                """This is a wrapper function."""
                cls = cls_attr(*args, **kwargs)
                cls._driver = self.driver
                cls._page_object = self.setter
                cls._function_name = attr
                cls._class_name = self.cls.__class__.__name__
                cls._wait = self.webdriver_wait
                if cls == self.cls:
                    return self

                return cls

            return wrap()

        else:
            return cls_attr
