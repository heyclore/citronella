require 'citronella'
require_relative '../contents_page'

class GemsPage < ContentsPage.new.header_menu
  def a_button
    ui(css: 'a.gems__nav-link:nth-child(1)')
  end

  def b_button
    ui(css: 'a.gems__nav-link:nth-child(2)')
  end
end
