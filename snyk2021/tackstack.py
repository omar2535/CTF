import nclib
from sympy import sympify, solve

nc = nclib.Netcat(('35.211.72.63', 8000), verbose=True)

# Initial connection
response = nc.recv()
response = nc.recv()

while response != b'\nERROR: DOMAIN\n':
    equation_string = response.decode('utf-8').split('\n')[0]
    sympy_eq = sympify("Eq(" + equation_string.replace("=", ",") + ")")
    result = solve(sympy_eq)
    nc.send(f"{result[0]}\n")
    response = nc.recv()
    response = nc.recv()









