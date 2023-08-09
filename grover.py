"""Grover's algorithm module

Author:
     Duarte Goncalves

Date:
    2023-08-09
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

class GroverCircuit(QuantumCircuit):
    """The grover circuit class for the Grover's algorithm

    Inheritence:
        QuantumCircuit : The QuantumCircuit class from qiskit
    """
    def __init__(self, number_list: list, cycles:int = 1, restrict = True):
        """__init__ method for Grover's algorithm

        Args:
            number_list (list): The list of numbers the circuit should return with high probability
            cycles (int, optional): Number of Grover cycles (U_s*U_omega). Defaults to 1.
            restriction (bool, optional): Whether to restrict the number of qubits to 7 or fewer.
        """
        self.number_list = number_list
        self.restriction = restrict
        self.n_qubits = len(bin(max(number_list))[2:])
        oracle_circuit = self.oracle().to_gate()
        super().__init__(self.n_qubits,self.n_qubits)
        self.h(range(self.n_qubits))
        self.barrier()
        reflection_circuit = self.reflection().to_gate()

        # START OF CYCLE - Repeat to increase probability of measuring the correct answer
        for _ in range(cycles):
            self.append(oracle_circuit, range(self.n_qubits))
            self.append(reflection_circuit, range(self.n_qubits))
        #END OF CYCLE

        self.measure(range(self.n_qubits),range(self.n_qubits))

    def __repr__(self):
        return f'Grover Circuit with {self.n_qubits} qubits'

    def __str__(self):
        return f'Grover Circuit with {self.n_qubits} qubits'

    def __len__(self):
        return self.n_qubits

    def oracle(self) -> QuantumCircuit:
        """Creates the oracle for the Grover's algorithm
        
        Raises:
            ValueError: If the number of bits required to represent the list is greater than 7,
            this is because the free plan on IBM Quantum only allows a maximum of 7 qubits,
            feel free to remove this restriction if you have access to more qubits.

        Returns:
            QuantumCircuit: The oracle circuit
        """
        # determine number of bits to represent list
        if self.n_qubits > 7 and self.restriction:
            raise ValueError('We are restricted to 7 bits or fewer for this challenge.\
                If you have access to more qubits, \
                feel free to remove this restriction with retriction=False.')
        oracle = QuantumCircuit(self.n_qubits, name='oracle')
        u_omega = np.identity(2**self.n_qubits)
        for number in self.number_list:
            u_omega[number,number] = -1
        oracle.unitary(u_omega, range(self.n_qubits),  label='oracle')
        return oracle


    def reflection(self) -> QuantumCircuit:
        """Creates the reflection circuit for the Grover's algorithm

        Returns:
            QuantumCircuit: The reflection circuit (also known as the diffusion operator)
        """
        reflection = QuantumCircuit(self.n_qubits, name='reflection')
        u_s = 2*np.outer(Statevector(self),Statevector(self)) - np.identity(2**self.n_qubits)
        reflection.unitary(u_s, range(self.n_qubits), label='reflection')
        return reflection
