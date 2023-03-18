'use strict'

const WebUi = require('./web-ui')

class PageDecorator {
  constructor(args) {
    return new Proxy(this, {
      get(target, prop) {
        let currentPage = new args.pageLists.currentPage()
        if(prop in currentPage){
          let obj = currentPage[prop]
          let ui =  new WebUi(args.driver, args.webdriverWait, args.pageLists, obj.by, obj.page, {logger: args.logger, cls: currentPage.constructor.name, method: prop})
          return ui
        }
        throw new Error(`'${prop}' doesn't exist in '${currentPage.constructor.name}'`);
      }
    });
  }
}

module.exports = PageDecorator;
