#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let execution = 0; execution < x; execution++)
  {
    theFunction();
  }
};
