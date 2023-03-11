require 'citronella'
require_relative '../contents_page'

class GuidesPage < ContentsPage.new.header_menu
  def rubybems_basic_button
    ui(css: 'a.nav--v__link:nth-child(1)')
  end

  def what_is_gem_button
    ui(css: 'a.nav--v__link:nth-child(2)')
  end
end
