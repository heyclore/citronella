require 'citronella'
require_relative '../components/header_menu'

class HomePage
  include HeaderMenu

  def search_button
    ui(class: 'home__search__icon')
  end

  def code_link_button
    ui(css: 'div.nav--v > a:nth-child(3)')
  end
end
