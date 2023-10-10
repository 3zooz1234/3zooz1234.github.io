def nicetrips(p):
	trips = []
	for i in range(int(p/2),p+1):
		if int((p**2)/2)%i == 0:
			triple = (p-int((p**2)/(2*i)),p-i,int((p**2)/(2*i))+i-p)

			trips.append(triple)
	return trips

from pyodide.ffi import create_proxy
from js import document
def process(inp):
    if inp.isdigit():
        perimeter = int(inp)
        if perimeter%2 == 0:
            output = nicetrips(perimeter)
        else:
            output = "No such triangle exists."
    else:
        output = "Invalid Entry."
    return output

@create_proxy
def click(*args):
    _input = document.getElementById('text').value
    document.getElementById('output').innerText = process(_input)
document.getElementById('click').addEventListener('click',click)

