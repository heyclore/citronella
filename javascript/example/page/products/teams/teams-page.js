const { By } = require('selenium-webdriver');
const { ui } = require('citronella')
const ContentsPage = require('../../contents-page')

class TeamsPage extends new ContentsPage().menuBar{
}

module.exports = TeamsPage
