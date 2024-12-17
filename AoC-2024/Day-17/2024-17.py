'''Part 1
Literal Operand = Actual value
Combo Operand   = Actual for 0-3, A-C for 4-6, NA for 7

Opcode 0 - adv
    n = combo operand
    A //= 2**n
Opcode 1 - bxl
    n = literal operand
    B = B^n
Opcode 2 - bst
    n = combo operand
    B = n%8
Opcode 3 - jnz
    n = literal operand
    if A != 0:
        jump to instruction n
Opcode 4 - bxc
    B = B^C
Opcode 5 - out
    n = combo operand
    output n%8
Opcode 6 - bdv
    n = combo operand
    B = A // 2**n
Opcode 7 - cdv
    n = combo operand
    C = A // 2**n

Define a machine to be a 3 tuple of the form
    (
        program:list[int],
        (A,B,C),
        instruction pointer,
    )
'''

'''Part 2
Brute force + slightly smarter brute force take too long

Program
    2 4 
        B = A % 8
    1 1
        B = B ^ 1
    7 5
        C = A // 2**B
    1 5
        B = B ^ 5
    4 3
        B = B ^ C
    0 3
        A = A // 8
    5 5
        return B % 8
    3 0
        if A != 0:
            goto start

B = A%8
B = B^1

'''

def to_base_8(n:int) -> list[int]:
    ans = []
    while n != 0:
        ans.append(n%8)
        n //= 8
    return ans[::-1]

class Machine:
    def __init__(self, program:list[int], registers:list[int]):
        if len(registers) != 3:
            raise Exception(f'Wrong number of registers passed: {registers}')
        self.prog:list[int] = program
        self.reg:list[int] = registers
        self.ptr:int = 0   #Instruction Pointer

    def _lit_op(self) -> int:
        return self.prog[self.ptr+1]

    def _cmb_op(self) -> int:
        lit = self._lit_op()
        if 0 <= lit <= 3:
            return lit
        if lit <= 6:
            return self.reg[lit-4]
        raise Exception(f'Invalid combo operand: {lit}')
    
    def _step(self) -> int|None:
        if self.ptr >= len(self.prog):
            raise Exception('Pointer out of bounds')
        if self.ptr%2 != 0:
            raise Exception('Pointer at odd index')
        opcode = self.prog[self.ptr]
        
        if opcode == 0:
            n = self._cmb_op()
            self.reg[0] //= 2**n
        elif opcode == 1:
            n = self._lit_op()
            self.reg[1] ^= n
        elif opcode == 2:
            n = self._cmb_op()
            self.reg[1] = n%8
        elif opcode == 3:
            n = self._lit_op()
            if self.reg[0] != 0:
                self.ptr = n
                return
        elif opcode == 4:
            self.reg[1] ^= self.reg[2]
        elif opcode == 5:
            n = self._cmb_op()
            self.ptr += 2
            return n%8
        elif opcode == 6:
            n = self._cmb_op()
            self.reg[1] = self.reg[0] // 2**n
        elif opcode == 7:
            n = self._cmb_op()
            self.reg[2] = self.reg[0] // 2**n
        else:
            raise Exception(f'Invalid opcode received: {opcode}')
        
        self.ptr += 2
        return None
    
    def run(self) -> list[int]:
        ans = []
        while self.ptr < len(self.prog):
            out = self._step()
            if out != None:
                ans.append(out)
        return ans
    
    def is_self_gen(self) -> bool:
        out = []   #List of all outputs
        while self.ptr < len(self.prog):
            #Simulate next step
            n = self._step()
            if n == None:
                continue
            out.append(n)
            #Output is too long
            l = len(out)
            if l > len(self.prog):
                return False
            #Output is wrong
            if n != self.prog[l-1]:
                return False
        #Output is too short
        if len(out) != len(self.prog):
            return False
        #Output is correct
        return True

program = [2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0]

#Sample Input
machine_sample = Machine(
    [0,1,5,4,3,0],
    [729,0,0],
)
ans_sample = machine_sample.run()
ans_sample = [str(i) for i in ans_sample]
ans_sample = ','.join(ans_sample)
print(ans_sample)

#Part 1
machine_1 = Machine(
    program,
    [46323429,0,0],
)
ans_1 = machine_1.run()
ans_1 = ','.join([str(i) for i in ans_1])
print(ans_1)

print(to_base_8(46323429))

# #Part 2
# ans_2 = 0
# while True:
#     machine_2 = Machine(
#         program,
#         [ans_2,0,0],
#     )
#     if machine_2.is_self_gen():
#         break
#     ans_2 += 1
# print(ans_2)
