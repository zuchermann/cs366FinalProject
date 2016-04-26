function hash() {
	var a = clean(arrayfromargs(arguments));
	/*
	word length
	frequency of letters? distribution
	frequency letters relative to normal dist of word in english
	starting letter
	starts with vowel?
	starts with plosive
	//p but not ph
	part of speach
	
	*/
	var idxs = toLetterIndex(a);
	var freqs = letterFrequencies(idxs);
	post(a, idxs, "\n", freqs);
}

var clean = function(a) {
	// a is a word...
	a = a.join("").toLowerCase();
	a = a.replace(/[^a-z]/g, '');
	return a;
};

var toLetterIndex = function(a) {
	var i;
	v = [];
	for(i = 0; i < a.length; i++) {
		v.push(a.charCodeAt(i) -97);
	}
	return v;
};

var letterFrequencies = function(idxs) {
	var v = [];
	var i;
	for (i=0; i < 26; i++) {
		v[i] = 0;
	}
	for (i=0; 0<idxs.length; i++){
		v[idxs[i]] += 1;
	}
	return v;
};