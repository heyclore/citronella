const { By } = require("selenium-webdriver");
const { ui } = require("citronella");

class LoginPage {
  get usernameInput() {
    return ui(By.id("login_username"));
  }

  get passwordInput() {
    return ui(By.id("login_password"));
  }

  get signinButton() {
    return ui(By.css('button[type="submit"]'));
  }

  get createAccountLink() {
    return ui(By.css('a[href="/signup"'));
  }
}

module.exports = LoginPage;
