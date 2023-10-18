from math import log

def isfloat(st):
    try:
        float(st)
        return True
    except ValueError:
        return False

def euler_num(error):
    def seq(n):
        return (1+(0.5)**n)**(2**n)

    if isfloat(error) or error.isdigit():
        error = float(error)
        if error < 10**(-16):
            output = "Error must be positive and not less than 10^-16."
        elif error <= 1:
            num = int(2-log(error/abs(seq(1)-seq(2)),2))
            output = f"e ~ {str(seq(num))}"
        else:
            output = "Error is too large; it must be less than 1."
    else:
        output = "Invalid Entry."
    
    return output

from js import document
from pyodide.ffi import create_proxy

@create_proxy
def click(*args):
    _input = document.getElementById("err").value
    document.getElementById("output").innerText = euler_num(_input)
document.getElementById("click").addEventListener("click", click)


