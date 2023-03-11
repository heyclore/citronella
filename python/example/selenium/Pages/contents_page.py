class ContentsPage:

    def header():
        from Pages.components import Header
        return Header

    def footer():
        from Pages.components import Footer
        return Footer

    def sidebar_account():
        from Pages.components import SidebarAccount
        return SidebarAccount

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
