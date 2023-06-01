require 'citronella'
require_relative '../components/header_menu'

class SignInPage
  include HeaderMenu

  def email_input
    ui(id: 'session_who')
  end

  def password_input
    ui(id: 'session_password')
  end
end
