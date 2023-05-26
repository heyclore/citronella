class ContentsPage
  def header_menu
    require_relative 'components/header_menu'
    HeaderMenu
  end

  def home_page
    require_relative 'home/home_page'
    HomePage
  end

  def search_page
    require_relative 'search/search_page'
    SearchPage
  end

  def release_page
    require_relative 'releases/release_page'
    ReleasePage
  end

  def blog_page
    require_relative 'blog/blog_page'
    BlogPage
  end

  def gems_page
    require_relative 'gems/gems_page'
    GemsPage
  end

  def guides_page
    require_relative 'guides/guides_page'
    GuidesPage
  end

  def sign_in_page
    require_relative 'sign_in/sign_in_page'
    SignInPage
  end

  def sign_up_page
    require_relative 'sign_up/sign_up_page'
    SignUpPage
  end
end
