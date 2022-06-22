class Page_Decorator:
    """This is a decorator class."""
    def __init__(self, cls, driver, setter):
        self.cls = cls()
        self.driver = driver
        self.setter = setter

    def __getattr__(self,attr):
        cls_attr = self.cls.__getattribute__(attr)
        if callable(cls_attr):
            def wrap(*args, **kwargs):
                """This is a wrapper function."""
                cls = cls_attr(*args, **kwargs)
                cls._driver = self.driver
                cls._page_object = self.setter
                cls._name = attr
                if cls == self.cls:
                    return self

                return cls

            return wrap()

        else:
            return cls_attr
