'use strict'

const { until } = require('selenium-webdriver');

class WebUi
{
  #driver;
  #locator;
  #page;
  #pageLists;
  #wait;

  constructor(driver, wait, pageLists, locator, page)
  {
    this.#driver = driver;
    this.#locator = locator;
    this.#page = page;
    this.#pageLists = pageLists;
    this.#wait = wait;
  }

  async click()
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),this.#wait);
    await el.click()
    this.#pageLists.unshift(this.#page)
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


module.exports = WebUi;
