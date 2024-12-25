from dataclasses import dataclass

@dataclass
class Equation:
    inp0:str
    op:str
    inp1:str
    out:str

def parse_eqn(eqn:str) -> Equation:
    eqn = eqn.split()
    return Equation(eqn[0], eqn[1], eqn[2], eqn[4])

def parse_input(fn:str) -> tuple[
            dict[str,int],list[Equation]
        ]:
    with open(fn, 'r') as f:
        txt = f.read()
    init,eqns = txt.split('\n\n')
    init = {
        line[:3]:int(line[-1])
        for line in init.split('\n')
    }
    eqns = [
        parse_eqn(line)
        for line in eqns.split('\n')
    ]
    return init, eqns

def eval_eqn(inp0:int, op:str, inp1:int) -> int:
    if op == 'AND':
        return inp0 & inp1
    elif op == 'OR':
        return inp0 | inp1
    elif op == 'XOR':
        return inp0 ^ inp1
    raise Exception(f'Invlid operator received: {op}')

def find_val(
    var:str, 
    values:dict[str,int], 
    eqns:list[Equation]
    ) -> int:
    '''
    Finds the value of the specified variable given the currently 
    available values and the full list of equations.
    Will recursively calculate all the required values to solve 
    for it and update values correspondingly.
    '''
    #Base case
    if var in values:
        return values[var]
    #Not ideal, but ok for part 1. Linearly scan eqns to find var
    for eqn in eqns:
        if eqn.out == var:
            break
    #Find the values, then evaluate the equation
    v0 = eqn.inp0
    v1 = eqn.inp1
    inp0 = find_val(v0, values, eqns)
    inp1 = find_val(v1, values, eqns)
    ans = eval_eqn(inp0, eqn.op, inp1)
    #Update values and return the answer
    values[var] = ans
    return ans

def binary_to_int(a:list[int]) -> int:
    ans = a[0]
    for i in range(1,len(a)):
        ans *= 2
        ans += a[i]
    return ans

def part_1(fn:str) -> int:
    #Parse the input
    values,eqns = parse_input(fn)
    #Find the value of all the variables
    for eqn in eqns:
        var = eqn.out
        find_val(var, values, eqns)
    #Get the relevant variables
    z_values = {}
    for var in values:
        if var[0] == 'z':
            z_values[var] = values[var]
    #Put them together in binary form
    ans = [0 for i in range(len(z_values))]
    for i in range(len(ans)):
        var = f'z{i:02d}'
        ans[-i-1] = z_values[var]
    #Convert to a normal integer
    ans = binary_to_int(ans)
    return ans

print(part_1('Input.txt'))
