from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

class Grover_Circuit(QuantumCircuit):
    """The grover circuit class for the Grover's algorithm

    Inheritence:
        QuantumCircuit : The QuantumCircuit class from qiskit
    """
    def __init__(self, number_list: list, cycles:int = 1):
        """__init__ method for Grover's algorithm

        Args:
            number_list (list): The list of numbers the circuit should return with high probability
            cycles (int, optional): Number of Grover cycles (U_s*U_omega). Defaults to 1.
        """
        self.n_qubits = len(bin(max(number_list))[2:])
        oracle_circuit = self.oracle(number_list).to_gate()
        super().__init__(self.n_qubits,self.n_qubits)
        self.h(range(self.n_qubits))
        self.barrier()
        reflection_circuit = self.reflection(self).to_gate()

        # START OF CYCLE - Repeat to increase probability of measuring the correct answer
        for _ in range(cycles):
            self.append(oracle_circuit, range(self.n_qubits))
            self.append(reflection_circuit, range(self.n_qubits))
        #END OF CYCLE

        self.measure(range(self.n_qubits),range(self.n_qubits))


    def oracle(self, number_list:list, restriction = True) -> QuantumCircuit:
        """Creates the oracle for the Grover's algorithm

        Args:
            number_list (list): The list of numbers the oracle should mark as -1
            (analougous to a classical oracle giving True for the correct answer)

        Raises:
            ValueError: If the number of bits required to represent the list is greater than 7,
            this is because the free plan on IBM Quantum only allows a maximum of 7 qubits,
            feel free to remove this restriction if you have access to more qubits.

        Returns:
            QuantumCircuit: The oracle circuit
        """
        # determine number of bits to represent list
        if self.n_qubits > 7 and restriction:
            raise ValueError('We are restricted to 7 bits or fewer for this challenge.')
        oracle = QuantumCircuit(self.n_qubits, name='oracle')
        u_omega = np.identity(2**self.n_qubits)
        for number in number_list:
            u_omega[number,number] = -1
        oracle.unitary(u_omega, range(self.n_qubits),  label='oracle')
        return oracle


    def reflection(self, circuit:QuantumCircuit) -> QuantumCircuit:
        """Creates the reflection circuit for the Grover's algorithm

        Args:
            n_qubits (int): the number of qubits in the circuit
            circuit (QuantumCircuit): The circuit to be reflected
            (should have the oracle applied to it)

        Returns:
            QuantumCircuit: The reflection circuit (also known as the diffusion operator)
        """
        reflection = QuantumCircuit(self.n_qubits, name='reflection')
        u_s = 2*np.outer(Statevector(circuit),Statevector(circuit)) - np.identity(2**self.n_qubits)
        reflection.unitary(u_s, range(self.n_qubits), label='reflection')
        return reflection
