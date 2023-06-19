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

/**
 * Logs the provided information to the console if logging is enabled.
 * @param {Dictionary} log - The log configuration in dictionary.
 * @param {boolean} log.logger - Specifies whether logging is enabled or not.
 * @param {string} log.cls - The class or module name associated with the log entry.
 * @param {string} log.method - The method or function name associated with the log entry.
 * @param {string} name - The name of the log entry.
 */
function logger(log, name) {
  if (log.logger) {
    console.info(log.cls + " => " + log.method + " => " + name);
  }
}

module.exports = logger;
