const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../../contents-page')

class ProPage extends new ContentsPage().menuBar{
  get getStartedButton()
  {
    return ui(By.css('a[href="/signup"'));
  }
}

module.exports = ProPage
