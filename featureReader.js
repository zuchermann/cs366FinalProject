outlets = 2;
var buf = new Buffer("resultBuffer");
var x = new Dict("features");


function out(val){
	outlet(0, val);
};

// make an array of zeroes, set the buffer content to that
// only clears the first channel
function clear()
{
	var samples = [];
	var frames = buf.framecount();

	for (var i=0; i<frames; i++)
		samples.push(0.0);

	buf.poke(1, 0, samples);
};

function sendDelays(comp){
	
	var i = 0;
	var len = comp.length;
	while (i < len){
		var delay = comp[i][0]; //1 second
		prevLocation = comp[i][0];
		
		//setTimeout(out, delay);
		var tsk = new Task(out, this, comp[i][1]);
		tsk.schedule(delay/10) 
		i++;
	}
};

function readlines(s)
{
	var f = new File(getPath(s));

	var i,a,c;

	if (f.isopen) {
		//var parsed = JSON.parse(f.readlne());
		var JSONString = "";
		while (a=f.readline()) { // returns a string
			JSONString += a
		}
		//outlet(0, JSONString);
		var parsed = JSON.parse(JSONString);
		writeBuffer(parsed.singlesComplexity);
		f.close();
	} else {
		post("could not open file: " + s + "\n");
	}
};

function writeBuffer(){
	// provide a path to the json file or, if the file is in Max's searchpath, just the file name.
	// if you provide no argument then a file dialog will appear to allow you to choose a file.
	// alternatively, you may also use the import_yaml() to import yaml files rather than json files.
	// 
	// the import_json() and import_yaml() do enforce naming conventions and will only work if the
	// files to be imported end with the standard .json or .yml file suffixes.
	// to read any file, interpreting it as json regardless of suffix, use the readany() method
	
	x.import_json("features.json");
	var xjson = JSON.parse(x.stringify());
	var v = xjson.singlesComplexity;
	//post("length:", v.length, v[0], "\n");
	var samplesCh1 = [];
	var samplesCh2 = [];
	//buf.framecount();
	var maxVal1 = 0;
	var maxVal2 = 0;
	for (var i = 0; i < v.length; i++){
		samplesCh1.push(v[i][0]);
		samplesCh2.push(v[i][1]);
		//post(v[i],"\n");
		maxVal1 = Math.max(v[i][0], maxVal1);
		maxVal2 = Math.max(v[i][1], maxVal2);
	}
	//resixe the buffer
	buf.send("sizeinsamps", samplesCh1.length);
	buf.poke(1, 0, samplesCh1);
	buf.poke(2, 0, samplesCh2);
	outlet(0, "vzoom", maxVal1);
	outlet(1, "vzoom", maxVal2);
};

function bang()
{
	//outlet(0,"myvalue","is",myval);
	readlines("features.json");
};

var _root_directory = new File('featureReader.js').foldername;
var _separator = '/';

function getPath(name) {
	if (name.indexOf(':' ) == -1 && name[0] != _separator){
    	name = _root_directory + _separator + name;
	}
	return name;
};

