const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const MenuBar = require('../../components/menu-bar')

class ProPage extends MenuBar{
  get getStartedButton()
  {
    return ui(By.css('a[href="/signup"'));
  }
}

module.exports = ProPage
