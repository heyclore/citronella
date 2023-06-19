const { By } = require("selenium-webdriver");
const { ui } = require("citronella");

class MenuBar {
  get npmHomepageIcon() {
    return ui(By.css('a[href="/"]'));
  }

  get proButton() {
    return ui(By.id("nav-pro-link"));
  }

  get teamsButton() {
    return ui(By.id("nav-teams-link"));
  }

  get pricingButton() {
    return ui(By.id("nav-pricing-link"));
  }

  get signupButton() {
    return ui(By.id("signup"));
  }

  get signinButton() {
    return ui(By.id("signin"));
  }

  get searchPackagesInput() {
    return ui(By.name("q"));
  }

  get searchButton() {
    return ui(By.css('button[type="submit"]'));
  }
}

module.exports = MenuBar;
