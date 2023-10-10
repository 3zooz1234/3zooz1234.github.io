def nicetrips(p):
	trips = []
	for i in range(int(p/2),p+1):
		if int((p**2)/2)%i == 0:
			triple = (p-int((p**2)/(2*i)),p-i,int((p**2)/(2*i))+i-p)

			trips.append(triple)
	return trips

from pyodide.ffi import create_proxy
from js import document
@create_proxy
def click(*args):
    perimeter = int(document.getElementById('text').value)
    document.getElementById('output').innerText = nicetrips(perimeter)
document.getElementById('click').addEventListener('click',click)

