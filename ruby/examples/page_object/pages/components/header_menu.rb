require_relative '../contents_page'

class HeaderMenu
  def home_logo
    ui(class: 'header__logo', page: ContentsPage.new.home_page)
  end

  def search_input
    ui(id: 'home_query', page: ContentsPage.new.search_page)
  end

  def releases_button
    ui(css: 'a[href="https://rubygems.org/releases"]', page: ContentsPage.new.search_page)
  end

  def blog_button
    ui(css: 'a[href="https://blog.rubygems.org"]', page: ContentsPage.new.blog_page)
  end

  def gems_button
    ui(css: 'a[href="/gems"]', page: ContentsPage.new.gems_page)
  end

  def guides_button
    ui(css: 'a[href="https://guides.rubygems.org"]', page: ContentsPage.new.guides_page)
  end

  def sign_in_button
    ui(css: 'a[href="/sign_in"]', page: ContentsPage.new.sign_in_page)
  end

  def sign_up_button
    ui(css: 'a[href="/sign_up"]', page: ContentsPage.new.sign_up_page)
  end
end
