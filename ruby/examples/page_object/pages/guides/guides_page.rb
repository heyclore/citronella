require 'citronella'
require_relative '../components/header_menu'

class GuidesPage
  include HeaderMenu

  def rubybems_basic_button
    ui(css: 'a.nav--v__link:nth-child(1)')
  end

  def what_is_gem_button
    ui(css: 'a.nav--v__link:nth-child(2)')
  end
end
