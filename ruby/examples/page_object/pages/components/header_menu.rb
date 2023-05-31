require 'citronella'
require_relative '../contents_page'

module HeaderMenu
  def home_logo
    ui(class: 'header__logo')
  end

  def search_input
    ui(id: 'home_query')
  end

  def releases_button
    ui(css: 'a[href="https://rubygems.org/releases"]')
  end

  def blog_button
    ui(css: 'a[href="https://blog.rubygems.org"]')
  end

  def gems_button
    ui(css: 'a[href="/gems"]')
  end

  def guides_button
    ui(css: 'a[href="https://guides.rubygems.org"]')
  end

  def sign_in_button
    ui(css: 'a[href="/sign_in"]')
  end

  def sign_up_button
    ui(css: 'a[href="/sign_up"]')
  end
end
