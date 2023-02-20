class PageTab:
    _pages = []

    @property
    def current_page(self):
        return self._pages[-1]

    def append(self, new_page):
        self._pages.append(new_page)
        if len(self._pages) > 5:
            self._pages.pop(0)

    def pop(self):
        self._pages.pop()
