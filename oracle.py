from qiskit import QuantumCircuit
import numpy as np
# define oracle circuit
def oracle(lucky_number):
    # determine number of bits to represent lucky_number
    lucky_bin = bin(lucky_number)[2:]
    bits = len(lucky_bin)
    if bits > 7:
        raise ValueError('We are restricted to 7 bits or fewer for this challenge.')
    oracle = QuantumCircuit(bits, name='Oracle')
    O = np.identity(2**bits)
    O[lucky_number,lucky_number] = -1
    oracle.unitary(O, range(bits),  label='Oracle')
    return oracle.to_gate()