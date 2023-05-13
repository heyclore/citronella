class ContentsPage:

    def home_page(self):
        from Pages.home.home_page import HomePage
        return HomePage

    def gallery_page(self):
        from Pages.gallery.gallery_page import GalleryPage
        return GalleryPage

    def navigation_menu(self):
        from Pages.components.navigation_menu import NavigationMenu
        return NavigationMenu
