const { By } = require("selenium-webdriver");
const { ui } = require("citronella");
const MenuBar = require("../components/menu-bar");

class SearchPage extends MenuBar {
  get searchResultLists() {
    return ui(By.css('a[target="_self"]'));
  }
}

module.exports = SearchPage;
