require 'citronella'
require_relative '../components/header_menu'

class GemsPage
  include HeaderMenu

  def a_button
    ui(css: 'a.gems__nav-link:nth-child(1)')
  end

  def b_button
    ui(css: 'a.gems__nav-link:nth-child(2)')
  end
end
