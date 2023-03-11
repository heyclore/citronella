require 'citronella'
require_relative '../contents_page'

class SignUpPage < ContentsPage.new.header_menu
  def email_input
    ui(id: 'user_email')
  end

  def password_input
    ui(id: 'user_handle')
  end
end
