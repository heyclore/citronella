const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const MenuBar = require('../components/menu-bar')

class HomePage extends MenuBar{

  get signUpForFreeButton(){
    return ui(By.css('div.w-100 a[href="/signup"]'));
  }

  get signUpForFreeButton(){
    return ui(By.css('div.w-100 a[href="/products/pro"]'));
  }
}

module.exports = HomePage
