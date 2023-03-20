const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../../contents-page')

class TeamsPage extends new ContentsPage().menuBar{
  get getStartedButton()
  {
    return ui(By.css('a[href="/org/create"'));
  }
}

module.exports = TeamsPage
