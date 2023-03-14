'use strict'

class PageTab{
  #pageList = [];

  get currentPage(){
    return this.#pageList[0]

  }

  unshift(newPage){
    this.#pageList.unshift(newPage)
    console.log(this.#pageList.length, this.#pageList);
  }

  get shift(){
    this.#pageList.shift()
    console.log(this.#pageList.length, this.#pageList);
  }

}

module.exports = PageTab
