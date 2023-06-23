# Citronella

[![npm version](https://badge.fury.io/js/citronella.svg)](https://badge.fury.io/js/citronella)

webdriver extension with a page object wrapper.

![alt terminal](https://github.com/heyclore/citronella/blob/main/javascript/screenshot/terminal.png?raw=true)
![alt terminal2](https://github.com/heyclore/citronella/blob/main/javascript/screenshot/terminal2.png?raw=true)

## Example Tests

```javascript
const { Builder } = require("selenium-webdriver");
const { WebPage } = require("citronella");
const ContentsPage = require("../page/contents-page");
const assert = require("assert");

describe("test navigation", function () {
  this.timeout(10000);
  before(async function () {
    driver = await new Builder().forBrowser("chrome").build();
    web = new WebPage(driver, 10000, true);
    web.page = ContentsPage;
    await web.driver.get("https://www.npmjs.com/");
  });

  after(async function () {
    driver.quit();
  });

  it("navigate to a pro page", async function () {
    await web.page.homePage.proButton.click();
    title = await web.driver.getTitle();
    await assert.match(title, /Pro/);
  });

  it("navigate to a teams page", async function () {
    await web.page.proPage.teamsButton.click();
    title = await web.driver.getTitle();
    await assert.match(title, /Teams/);
  });

  it("navigate to a products page", async function () {
    await web.page.teamsPage.pricingButton.click();
    title = await web.driver.getTitle();
    await assert.match(title, /Products/);
  });

  it("navigate to a home page", async function () {
    await web.page.productsPage.npmHomepageIcon.click();
    title = await web.driver.getTitle();
    await assert.match(title, /npm/);
  });
});
```

Even though this module is mainly designed for the page object model, it can also be used without it for quick prototyping or mockups, etc.
```javascript
const { By, Builder } = require("selenium-webdriver");
const { WebPage } = require("citronella");
const assert = require("assert");

describe("test search package with locate method", function () {
  this.timeout(10000);
  before(async function () {
    driver = await new Builder().forBrowser("chrome").build();
    web = new WebPage(driver, 10000, true);
    await web.driver.get("https://www.npmjs.com/");
  });

  after(async function () {
    driver.quit();
  });

  it("check if a package exists in the list of results", async function () {
    await web.locate(By.name("q")).sendKeys("citronella");
    await web.locate(By.css('button[type="submit"]')).click();
    await web.locate(By.name("foo")).getElements();
    let textList = [];
    for (let i in ElementsResult) {
      textList.push(await ElementsResult[i].getText());
    }
    assert.match(textList.join(), /citronella/);
  });
});
```

___
## Install Package

```bash
npm i citronella
```

___
## Documentation

There are only two modules import in this package:

* The first module is for the test script.

```javascript
const { Builder } = require("selenium-webdriver");
const { WebPage } = require("citronella");

describe("test navigation", function () {
  this.timeout(10000);
  before(async function () {
    driver = await new Builder().forBrowser("chrome").build();
    web = new WebPage(driver, 10000, true);
  });
});
```

* The second module are for the page object model.

```javascript
const { By } = require("selenium-webdriver");
const { ui } = require("citronella");
const MenuBar = require("../components/menu-bar");

class HomePage extends MenuBar {
  get signUpForFreeButton() {
    return ui(By.css('div.w-100 a[href="/signup"]'));
  }

  get signUpForFreeButton() {
    return ui(By.css('div.w-100 a[href="/products/pro"]'));
  }
}

module.exports = HomePage;
```

___
## Page Object Design / Strategy

see full [Page object](https://github.com/heyclore/citronella/tree/main/javascript/example/page) example

```javascript
const { By, Builder } = require("selenium-webdriver");
const { ui, WebPage } = require("citronella");

class HomePage {
  get signUpForFreeButton() {
    return ui(By.css('div.w-100 a[href="/signup"]'));
  }
}

class SignupPage {
  get usernameInput() {
    return ui(By.id("signup_name"));
  }  

  get passwordInput() {
    return ui(By.id("signup_password"));
  }

  get signUpButton() {
    return ui(By.id("signup_button"));
  }
}

class ContentsPage {
  get homePage() {
    return HomePage;
  }

  get signupPage() {
    return SignupPage;
  }
}

main(async function () {
  driver = await new Builder().forBrowser("chrome").build();
  web = new WebPage(driver, 10000, true);
  web.page = ContentsPage;
  await web.driver.get("https://www.npmjs.com/");

  await web.page.homePage.signUpForFreeButton.click();
  await web.page.signupPage.usernameInput.sendKeys("foo@bar.baz");
  await web.page.signupPage.passwordInput.sendKeys("FizzBuzz");
  await web.page.signupPage.signUpButton.click();
}

main();
```

___
## Usage

### citronella.WebPage

###### Args:
- driver / webdriver
- wait (ms)
- logger (bool)

###### Method Lists:
| Method Name        | Args*       | Kwargs**         | Note |
| ------------------ |:-----------:|:----------------:|:----:|
| driver             | -           | -                | return selenium `webdriver` object |
| locate             | by          | -                | similar as`driver.get_element` args |
| page               | page object | -                | setter |
| page               | -           | -                | getter |
| readyState         | timeout(ms) | -                | execute javascript `document.readyState` manually |
| sleep              | number(ms)  | -                |      |

### citronella.ui / citronella.WebUi

###### Args:
- by

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | text   | clear `bool`, return_key `bool` |     |
| click         | -      | -                  |      |
| get_element   | -      | -                  |      |
| get_elements  | -      | -                  |      |
| ec_element_to_be_clickable | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_all_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_all_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_any_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_invisibility_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_element_located_to_be_selected | -    | -    | wrapper of `EC` / `excpected_condition` |


## Testing powered by
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)
