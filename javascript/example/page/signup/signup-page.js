const { By } = require("selenium-webdriver");
const { ui } = require("citronella");

class SignupPage {
  get usernameInput() {
    return ui(By.id("signup_name"));
  }

  get emailAddressInput() {
    return ui(By.id("signup_email"));
  }

  get passwordInput() {
    return ui(By.id("signup_password"));
  }

  get eulaCheckbox() {
    return ui(By.id("signup_eula-agreement"));
  }

  get eulaCheckbox() {
    return ui(By.css('button[type="submit"]'));
  }
}

module.exports = SignupPage;
