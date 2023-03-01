#MIT License
#
#Copyright (c) 2023 Eko Purnomo
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from .web_ui import WebUi


class PageDecorator:
    """This is a page decorator class."""
    def __init__(self, driver, webdriver_wait, pages, logger):
        self.cls = pages.current_page()
        self.driver = driver
        self.pages = pages
        self.logger = logger
        self.webdriver_wait = webdriver_wait

    def __getattr__(self, attr):
        """look up the attr / method name inside page object."""
        cls_attr = self.cls.__getattribute__(attr)
        def wrap(*args, **kwargs):
            """This is a wrapper function."""
            f = cls_attr(*args, **kwargs)
            return WebUi(self.driver, self.webdriver_wait, self.pages,
                         self.logger, f['by'], f['value'], f['page'], attr,
                         self.cls.__class__.__name__)

        return wrap()
