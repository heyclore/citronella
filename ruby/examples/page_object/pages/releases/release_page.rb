require 'citronella'
require_relative '../contents_page'

class ReleasePage < ContentsPage.new.header_menu
  def all_gems_button
    ui(css: 'a.news__nav-link:nth-child(1)')
  end

  def popular_gems_button
    ui(css: 'a.news__nav-link:nth-child(1)')
  end
end
