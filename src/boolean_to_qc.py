import numpy as np
import qiskit.transpiler
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library.standard_gates import RYGate, IGate
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer.primitives import Sampler
from bigtree import BinaryNode, preorder_iter

def get_projectionprobs(f, n, projection_bit):
    #f .... boolean function on n bits
    p_proj = 0
    p_full = 0
    for i in range(2**n):
        argument = []
        for k in range(n):
            argument+= [i//2**(n-1-k)] 
            i = i % 2**(n-1-k)
        if argument[projection_bit] == 0:
            p_proj += f(argument)
        p_full += f(argument)
    
    #Define restricted functions
    def f_one(tupel):
        t = tupel.copy()
        t.insert(projection_bit,1)
        return f(t)
    
    def f_zero(tupel):
        t = tupel.copy()
        t.insert(projection_bit,0)
        return f(t)
    
    if p_full > 0:
        p = round(p_proj/p_full,2)
    else:
        p = -1
    
    return p, f_zero, f_one 


def get_fulltree(f,n,prefix=""):
    p, f_left, f_right = get_projectionprobs(f, n, 0)
    if p>= 0:
        root = BinaryNode(prefix, p = p)
       # print(prefix,"\t n=",n,"p=",p)
    
    else:
        return
    
    if n > 1:
        root.children = [get_fulltree(f_left,n-1,prefix+"0"),get_fulltree(f_right,n-1,prefix+"1")]
    #if n == 1:
    #    print(f([0]), f([1]))   
    return root
