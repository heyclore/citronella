const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const MenuBar = require('../../components/menu-bar')

class TeamsPage extends MenuBar{
  get getStartedButton()
  {
    return ui(By.css('a[href="/org/create"'));
  }
}

module.exports = TeamsPage
