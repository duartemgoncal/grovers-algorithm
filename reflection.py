from qiskit import *
import numpy as np
from qiskit.quantum_info import Statevector

def reflection_gate(lucky_number, circuit):
    lucky_bin = bin(lucky_number)[2:]
    bits = len(lucky_bin)
    reflection = QuantumCircuit(bits, name='reflection')
    R = 2*np.outer(Statevector(circuit),Statevector(circuit)) - np.identity(2**bits)
    reflection.unitary(R, range(bits), label='reflection')
    return reflection.to_gate()