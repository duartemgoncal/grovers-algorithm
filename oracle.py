from qiskit import QuantumCircuit
import numpy as np
import qiskit.quantum_info as qi
# define oracle circuit
def oracle(lucky_number):
    # determine number of bits to represent lucky_number
    lucky_bin = bin(lucky_number)[2:]
    bits = len(lucky_bin)
    if bits > 7:
        raise ValueError('We are restricted to 7 bits or fewer for this challenge.')
    oracle = QuantumCircuit(bits, name='oracle')
    U = np.identity(2**bits)
    U[lucky_number,lucky_number] = -1
    oracle.unitary(U, range(bits),  label='oracle')
    return oracle.to_gate()