
function out(val){
			outlet(0, val);
		}

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
}

function readlines(s)
{
	var f = new File(s);

	var i,a,c;

	if (f.isopen) {
		//var parsed = JSON.parse(f.readlne());
		var JSONString = "";
		while (a=f.readline()) { // returns a string
			//var parsed = JSON.parse(a);
			//outlet(0,parsed.name + " " + parsed.value);
			JSONString += a
			//outlet(0, a+"\n");
		}
		//outlet(0, JSONString);
		var parsed = JSON.parse(JSONString);
		sendDelays(parsed.singlesComplexity);
		f.close();
	} else {
		post("could not open file: " + s + "\n");
	}
}

function bang()
{
	//outlet(0,"myvalue","is",myval);
	readlines("features.json");
}
