// MIT License
// 
// Copyright (c) 2023 Eko Purnomo
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

'use strict'

const { elementLocated, elementsLocated, elementIsVisible, elementIsNotVisible,
  elementIsEnabled, elementIsDisabled, elementIsSelected,
  elementIsNotSelected } = require('selenium-webdriver/lib/until');
const { Key } = require('selenium-webdriver');
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

  async click(redirect)
  {
    logger(this.#logger, this.click.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await this.webdriverWait(elementIsVisible(el));
    await el.click()
    if(redirect == false){
      return
    }
    this.#pageLists.unshift(this.#page)
  }

  async sendKeys(text, args)
  {
    logger(this.#logger, this.sendKeys.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await el.sendKeys(text)
    if(args){
      if(args.return == true || args.enter == true){
        await el.sendKeys(Key.ENTER)
        if(this.#page && (args.redirect == undefined || args.redirect != false)){
          this.#pageLists.unshift(this.#page)
        }
      }
    }
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
    logger(this.#logger, this.untilElementLocated.name)
    return await this.webdriverWait(elementLocated(this.#locator));
  }

  async untilElementsLocated(){
    logger(this.#logger, this.untilElementsLocated.name)
    return await this.webdriverWait(elementsLocated(this.#locator));
  }

  async untilElementIsVisible(){
    logger(this.#logger, this.untilElementIsVisible.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsVisible(el));
  }

  async untilElementIsNotVisible(){
    logger(this.#logger, this.untilElementIsNotVisible.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotVisible(el));
  }

  async untilElementIsEnabled(){
    logger(this.#logger, this.untilElementIsEnabled.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsEnabled(el));
  }

  async untilElementIsDisabled(){
    logger(this.#logger, this.untilElementIsDisabled.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsDisabled(el));
  }

  async untilElementIsSelected(){
    logger(this.#logger, this.untilElementIsSelected.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsSelected(el));
  }

  async untilElementIsNotSelected(){
    logger(this.#logger, this.untilElementIsNotSelected.name)
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotSelected(el));
  }
}

module.exports = WebUi;
