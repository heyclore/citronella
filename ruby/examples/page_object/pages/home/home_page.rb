require_relative '../contents_page'

class HomePage < ContentsPage.new.header_menu
  @url = "https://rubygems.org/"

  def search_button
    ui(class: 'home__search__icon', page: ContentsPage.new.search_page)
  end
end
