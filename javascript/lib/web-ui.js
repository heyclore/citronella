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

"use strict";

const {
  elementLocated,
  elementsLocated,
  elementIsVisible,
  elementIsNotVisible,
  elementIsEnabled,
  elementIsDisabled,
  elementIsSelected,
  elementIsNotSelected,
} = require("selenium-webdriver/lib/until");
const { Key } = require("selenium-webdriver");
const logger = require("./logger");

/**
 * Represents a Web UI object.
 */
class WebUi {
  #driver;
  #wait;
  #locator;
  #logger;

  /**
   * Constructs a new instance of the WebUi class.
   * @param {object} driver - The web driver object.
   * @param {number} wait - The wait time in milliseconds.
   * @param {string} locator - The element locator string.
   * @param {Dictionary} logger - The logger object.
   */
  constructor(driver, wait, locator, logger) {
    this.#driver = driver;
    this.#wait = wait;
    this.#locator = locator;
    this.#logger = logger;
  }

  /**
   * Waits for an element in the web driver.
   * @param {object} element - The element to wait for.
   * @returns {Promise} - A promise that resolves when the element is found.
   */
  async webdriverWait(element) {
    return await this.#driver.wait(element, this.#wait);
  }

  /**
   * Clicks on an element.
   * @returns {Promise} - A promise that resolves after the click operation is complete.
   */
  async click() {
    logger(this.#logger, this.click.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await this.webdriverWait(elementIsVisible(el));
    await el.click();
  }

  async sendKeys(text, returnKey) {
    logger(this.#logger, this.sendKeys.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    await el.sendKeys(text);
    if (returnKey) {
      await el.sendKeys(Key.ENTER);
    }
  }

  /**
   * Gets a single element matching the locator.
   * @returns {Promise} - A promise that resolves with the located element.
   */
  async getElement() {
    logger(this.#logger, this.getElement.name);
    return await this.webdriverWait(elementLocated(this.#locator));
  }

  /**
   * Gets all elements matching the locator.
   * @returns {Promise} - A promise that resolves with an array of located elements.
   */
  async getElements() {
    logger(this.#logger, this.getElements.name);
    return await this.webdriverWait(elementsLocated(this.#locator));
  }

  /**
   * Waits until an element is located.
   * @returns {Promise} - A promise that resolves with the located element.
   */
  async untilElementLocated() {
    logger(this.#logger, this.untilElementLocated.name);
    return await this.webdriverWait(elementLocated(this.#locator));
  }

  /**
   * Waits until all elements are located.
   * @returns {Promise} - A promise that resolves with an array of located elements.
   */
  async untilElementsLocated() {
    logger(this.#logger, this.untilElementsLocated.name);
    return await this.webdriverWait(elementsLocated(this.#locator));
  }

  /**
   * Waits until an element is visible.
   * @returns {Promise} - A promise that resolves with the visible element.
   */
  async untilElementIsVisible() {
    logger(this.#logger, this.untilElementIsVisible.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsVisible(el));
  }

  /**
   * Waits until an element is not visible.
   * @returns {Promise} - A promise that resolves when the element is not visible.
   */
  async untilElementIsNotVisible() {
    logger(this.#logger, this.untilElementIsNotVisible.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotVisible(el));
  }

  /**
   * Waits until an element is enabled.
   * @returns {Promise} - A promise that resolves with the enabled element.
   */
  async untilElementIsEnabled() {
    logger(this.#logger, this.untilElementIsEnabled.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsEnabled(el));
  }

  /**
   * Waits until an element is disabled.
   * @returns {Promise} - A promise that resolves when the element is disabled.
   */
  async untilElementIsDisabled() {
    logger(this.#logger, this.untilElementIsDisabled.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsDisabled(el));
  }

  /**
   * Waits until an element is selected.
   * @returns {Promise} - A promise that resolves with the selected element.
   */
  async untilElementIsSelected() {
    logger(this.#logger, this.untilElementIsSelected.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsSelected(el));
  }

  /**
   * Waits until an element is not selected.
   * @returns {Promise} - A promise that resolves when the element is not selected.
   */
  async untilElementIsNotSelected() {
    logger(this.#logger, this.untilElementIsNotSelected.name);
    let el = await this.webdriverWait(elementLocated(this.#locator));
    return await this.webdriverWait(elementIsNotSelected(el));
  }
}

module.exports = WebUi;
