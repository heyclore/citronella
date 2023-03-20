const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../contents-page')

class SearchPage extends new ContentsPage().menuBar{
  get searchResultLists()
  {
    return ui(By.css('a[target="_self"]'));
  }
}

module.exports = SearchPage
