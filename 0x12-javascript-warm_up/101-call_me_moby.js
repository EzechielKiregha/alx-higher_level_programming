#!/usr/bin/node

module.exports = {
	callMeMoby: function(x, theFunction) {
		for (let i_ = 0; i_ < x; i_++) theFunction();
	}
}
