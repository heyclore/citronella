'use strict'

const { until } = require('selenium-webdriver');
const logWrapper = require('./log-wrapper')

class WebUi
{
  #driver;
  #locator;
  #page;
  #pageLists;
  #wait;
  #logger;

  constructor(driver, by, page, pageLists, wait, logger)
  {
    this.#driver = driver;
    this.#locator = by;
    this.#page = page;
    this.#pageLists = pageLists;
    this.#wait = wait;
    this.#logger = logger;
  }

  async click()
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),this.#wait);
    await el.click()
    this.#pageLists.unshift(this.#page)
    //console.log(this)
    if(this.#pageLists.length >= 5)
    {
      this.#pageLists.pop()
    }
  }

  async sendKeys(x)
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),this.#wait);
    await el.sendKeys(x)
  }

  async getElements()
  {
    return await this.#driver.wait(until.elementsLocated(this.#locator),this.#wait);
  }
}

class PageDecorator {
  constructor(args) {
    return new Proxy(this, {
      get(target, prop) {
        let currentPage = new args.pageLists.currentPage()
        if(prop in currentPage){
          let obj = currentPage[prop]
          let ui =  new WebUi(args.driver, obj.by, obj.page, args.pageLists, args.webdriverWait, args.logger)
          ui.click = logWrapper(currentPage.constructor.name, prop, ui.click);
          ui.sendKeys = logWrapper(currentPage.constructor.name, prop, ui.sendKeys);
          ui.getElements = logWrapper(currentPage.constructor.name, prop, ui.getElements);
          ui.propertyName = logWrapper(currentPage.constructor.name, prop, ui.getElements);
          return ui
        }
        throw new Error(`'${prop}' doesn't exist in '${currentPage.constructor.name}'`);
      }
    });
  }
}


module.exports = PageDecorator;
