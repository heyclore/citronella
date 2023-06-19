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

const { until } = require("selenium-webdriver");
const PageDecorator = require("./page-decorator");
const WebUi = require("./web-ui");

/**
 * Represents a WebPage with driver, wait, page, logger, and utility methods.
 */
class WebPage {
  #driver;
  #wait;
  #page;
  #logger;

  /**
   * Creates an instance of WebPage.
   * @param {object} driver - The driver object for interacting with the web page.
   * @param {number} wait - The wait time in milliseconds for handling element wait operations.
   * @param {boolean} logger - The logger object for logging page interactions.
   */
  constructor(driver, wait, logger) {
    this.#driver = driver;
    this.#wait = wait;
    this.#logger = logger;
  }

  /**
   * Returns the driver object.
   * @returns {object} - The driver object.
   */
  get driver() {
    return this.#driver;
  }

  /**
   * Sets the page object.
   * @param {Class} page - The unitialized page object class to be decorated.
   */
  set page(page) {
    this.#page = page;
  }

  /**
   * Returns a decorated page object using PageDecorator.
   * @returns {object} - The decorated page object.
   */
  get page() {
    return new PageDecorator(
      this.#driver,
      this.#wait,
      this.#page,
      this.#logger
    );
  }

  /**
   * Locates a UI element using the provided selector or identifier.
   * @param {object} by - The selector or identifier for locating the UI element.
   * @returns {object} - The WebUi object representing the located UI element.
   */
  locate(by) {
    return new WebUi(this.#driver, this.#wait, by, {
      logger: this.#logger,
      cls: this.locate.name,
      method: by,
    });
  }

  /**
   * Waits for the page's ready state to be complete.
   * @param {number} timeout - The timeout value in milliseconds.
   */
  readyState(timeout) {
    this.driver.wait(
      this.driver.executeScript('return document.readyState === "complete";'),
      timeout
    );
  }

  /**
   * Delays the execution for the specified amount of time.
   * @param {number} ms - The delay time in milliseconds.
   * @returns {Promise} - A promise that resolves after the specified delay.
   */
  sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

module.exports = WebPage;
