from grover import GroverCircuit
from qiskit import *
from qiskit_ibm_provider import IBMProvider

number = [7, 3, 9]
grover_circ = GroverCircuit(number, 1)

# Run in a Simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(grover_circ, backend, shots=1000)
result = job.result()
print(result.get_counts())

# Run on a real quantum computer, be sure to set up your IBMQ account, learn more here: https://quantum-computing.ibm.com/
provider = IBMProvider()
backend = provider.get_backend('ibmq_belem')
job = execute(grover_circ, backend, shots=1000)
result = job.result()
print(result.get_counts())