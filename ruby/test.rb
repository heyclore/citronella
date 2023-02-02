require_relative 'citronella.rb'



class HomePage
  def search_input
    ui(:q) 
  end

  def search_button
    ui(:xpath, SearchPage)
  end
end

class SearchPage
  def home_button
    ui(:name, HomePage)
  end
end



web = Citronella::WebPage.new(:asutenan)
web.page_object(HomePage)
web.page.search_input.text
web.page.search_button.click
web.page.home_button.click
web.page.search_button.click
web.page.home_button.click
web.page.search_button.click
