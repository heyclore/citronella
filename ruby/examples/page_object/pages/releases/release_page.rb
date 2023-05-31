require 'citronella'
require_relative '../components/header_menu.rb'

class ReleasePage
  include HeaderMenu

  def all_gems_button
    ui(css: 'a.news__nav-link:nth-child(1)')
  end

  def popular_gems_button
    ui(css: 'a.news__nav-link:nth-child(1)')
  end
end
