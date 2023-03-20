const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../contents-page')

class ProductsPage extends new ContentsPage().menuBar{
  get createFreeButton()
  {
    return ui(By.css('a.db[href="/signup"'));
  }

  get getStartedProButton()
  {
    return ui(By.css('a[href="/products/pro#get-started"'));
  }

  get getStartedTeamsButton()
  {
    return ui(By.css('a[href="/org/create"'));
  }
}

module.exports = ProductsPage
