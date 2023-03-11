require 'citronella'
require_relative '../contents_page'

class SignInPage < ContentsPage.new.header_menu
  def email_input
    ui(id: 'session_who')
  end

  def password_input
    ui(id: 'session_password')
  end
end
