from qiskit import *
import numpy as np
from qiskit.quantum_info import Statevector

def reflection(n_qubits:int, circuit:QuantumCircuit) -> QuantumCircuit:
    """Creates the reflection circuit for the Grover's algorithm

    Args:
        n_qubits (int): the number of qubits in the circuit
        circuit (QuantumCircuit): The circuit to be reflected (shoulf have the oracle applied to it)

    Returns:
        QuantumCircuit: The reflection circuit (also known as the diffusion operator)
    """
    reflection = QuantumCircuit(n_qubits, name='reflection')
    R = 2*np.outer(Statevector(circuit),Statevector(circuit)) - np.identity(2**n_qubits)
    reflection.unitary(R, range(n_qubits), label='reflection')
    return reflection