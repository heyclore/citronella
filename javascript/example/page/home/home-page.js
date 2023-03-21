const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../contents-page')

class HomePage extends new ContentsPage().menuBar{
  static URL = 'https://www.npmjs.com/'

  get signUpForFreeButton(){
    return ui(By.css('div.w-100 a[href="/signup"]'), new ContentsPage().signupPage);
  }

  get signUpForFreeButton(){
    return ui(By.css('div.w-100 a[href="/products/pro"]'), new ContentsPage().proPage);
  }
}

module.exports = HomePage
