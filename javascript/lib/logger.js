'use strict'

function logger(log, name)
{
  if(log.logger){
    console.info(log.cls +' => '+ log.method +' => ' + name);
  }
}

module.exports = logger
