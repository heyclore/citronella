'use strict'

const { elementLocated, elementsLocated, elementIsVisible, elementIsNotVisible,
  elementIsEnabled, elementIsDisabled, elementIsSelected,
  elementIsNotSelected } = require('selenium-webdriver/lib/until');
const logger = require('./logger')

class WebUi
{
  #driver;
  #wait;
  #pageLists;
  #locator;
  #page;
  #logger;

  constructor(driver, wait, pageLists, locator, page, logger)
  {
    this.#driver = driver;
    this.#wait = wait;
    this.#pageLists = pageLists;
    this.#locator = locator;
    this.#page = page;
    this.#logger = logger;
  }

  async webdriverWait(element){
    return await this.#driver.wait(element, this.#wait);
  }

  async click()
  {
    logger(this.#logger, this.click.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await this.webdriverWait(elementIsVisible(el));
    await el.click()
    this.#pageLists.unshift(this.#page)
  }

  async sendKeys(x)
  {
    logger(this.#logger, this.sendKeys.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await el.sendKeys(x)
  }

  async getElement()
  {
    logger(this.#logger, this.getElement.name)
    return await this.webdriverWait(elementLocated(this.#locator));
  }

  async getElements()
  {
    logger(this.#logger, this.getElements.name)
    return await this.webdriverWait(elementsLocated(this.#locator));
  }

  async untilElementLocated(){
    return await this.webdriverWait(elementLocated(this.#locator));
  }

  async untilElementsLocated(){
    return await this.webdriverWait(elementsLocated(this.#locator));
  }

  async untilElementIsVisible(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsVisible(el));
  }

  async untilElementIsNotVisible(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotVisible(el));
  }

  async untilElementIsEnabled(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsEnabled(el));
  }

  async untilElementIsDisabled(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsDisabled(el));
  }

  async untilElementIsSelected(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsSelected(el));
  }

  async untilElementIsNotSelected(){
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotSelected(el));
  }
}


module.exports = WebUi;
