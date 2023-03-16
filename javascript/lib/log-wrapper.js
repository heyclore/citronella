'use strict'

function logWrapper(className, functionName, func)
{
  return function()
  {
    console.log(className +' => '+ functionName +' => ' + func.name);
    let result = func.apply(this, arguments);
    return result;
  };
}

module.exports = logWrapper
