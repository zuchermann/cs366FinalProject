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
		outlet(0, parsed.semanticRichness);
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
