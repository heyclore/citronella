const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../contents-page')

class SearchPage extends new ContentsPage().menuBar{
}

module.exports = SearchPage
