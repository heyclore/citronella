require 'citronella'
require_relative '../components/header_menu'

class SignUpPage
  include HeaderMenu

  def email_input
    ui(id: 'user_email')
  end

  def password_input
    ui(id: 'user_handle')
  end
end
