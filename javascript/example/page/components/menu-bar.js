const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const { ContentsPage } = require('../contents-page')

class MenuBar{
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
    return ui(By.id('signin'), new ContentsPage().signinPage);
  }
}
