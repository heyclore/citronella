require_relative 'contents_page'

class HomePage < ContentsPage.new.components
  @url = "https://rubygems.org/"

  def search_button
    ui(class: 'home__search__icon', page: ContentsPage.new.search_page)
  end
end
