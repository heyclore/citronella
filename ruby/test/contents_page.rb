class ContentsPage
  def components
    require_relative 'components'
    Components
  end

  def home_page
    require_relative 'home_page'
    HomePage
  end

  def search_page
    require_relative 'search_page'
    SearchPage
  end
end
