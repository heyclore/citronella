class PageTab:
    """This is a page page tab class."""
    _pages = []

    @property
    def current_page(self):
        """return the last page object stored."""
        return self._pages[-1]

    def append(self, new_page):
        """store the page object in _pages."""
        self._pages.append(new_page)
        if len(self._pages) > 5:
            self._pages.pop(0)

    def pop(self):
        """delete the last item of the _pages lists."""
        if len(self._pages) == 0:
            return
        self._pages.pop()
