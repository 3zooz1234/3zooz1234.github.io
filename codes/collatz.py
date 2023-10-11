def collatz(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n+1

def program(_input):
    string = ""
    num = _input
    count = 1
    while num > 1:
        string += str(num) + " -> "
        num = collatz(num)
        count += 1
    string += "1"
    return (string, count)

from js import document
from pyodide.ffi import create_proxy

@create_proxy
def click(*args):
    _input = document.getElementById('initial_num').value
    if _input.isdigit():
        initial_num = int(_input)
        output = program(initial_num)[0]
        length = "Length = " + str(program(initial_num)[1])
    else:
        output = "Invalid Entry."
        length = ""
    document.getElementById('output').innerText = output
    document.getElementById('len').innerText = length

document.getElementById('click').addEventListener('click',click)

