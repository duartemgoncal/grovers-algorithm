from qiskit import QuantumCircuit
import numpy as np

def oracle(number_list:list, restriction = True) -> QuantumCircuit:
    """Creates the oracle for the Grover's algorithm

    Args:
        number_list (list): The list of numbers the oracle should mark as -1 (analougous to a classical oracle giving True for the correct answer)

    Raises:
        ValueError: If the number of bits required to represent the list is greater than 7, this is because the free plan on IBM Quantum only allows a maximum of 7 qubits, feel free to remove this restriction if you have access to more qubits.

    Returns:
        QuantumCircuit: The oracle circuit
    """
    # determine number of bits to represent list
    n_qubits = len(bin(max(number_list))[2:])
    if n_qubits > 7 and restriction:
        raise ValueError('We are restricted to 7 bits or fewer for this challenge.')
    oracle = QuantumCircuit(n_qubits, name='oracle')
    O = np.identity(2**n_qubits)
    for number in number_list:
        O[number,number] = -1
    oracle.unitary(O, range(n_qubits),  label='oracle')
    return oracle