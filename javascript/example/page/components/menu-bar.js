const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../contents-page')

class MenuBar{
  get npmHomepageIcon(){
    return ui(By.css('a[href="/"]'), new ContentsPage().homePage);
  }

  get proButton(){
    return ui(By.id('nav-pro-link'), new ContentsPage().proPage);
  }

  get teamsButton(){
    return ui(By.id('nav-teams-link'), new ContentsPage().teamsPage);
  }

  get pricingButton(){
    return ui(By.id('nav-pricing-link'), new ContentsPage().productsPage);
  }

  get signupButton(){
    return ui(By.id('signup'), new ContentsPage().signupPage);
  }

  get signinButton(){
    return ui(By.id('signin'), new ContentsPage().loginPage);
  }

  get searchPackagesInput(){
    return ui(By.name('q'), new ContentsPage().searchPage);
  }

  get searchButton(){
    return ui(By.css('button[type="submit"]'), new ContentsPage().searchPage);
  }
}

module.exports = MenuBar
