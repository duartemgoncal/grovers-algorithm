# Previous attempt

I tried another method before using the Unitary Matrix, this would only work in a 3bit number.

```python
    oracle.x(i)
    oracle.z(i)
    oracle.cz(<other_qubit>, <qubit_i>)
    oracle.cz(<other_other_qubit>, <qubit_i>)
    oracle.ccz(<other_qubit>, <other_other_qubit>, <qubit_i> )
```

This algoritm inverts the phase of the state |010> for example, not inverting any other phase.
Then for two 1's

```python
    oracle.cx(<qubit_i>,<qubit_j>)
```

For three 1's

```python
oracle.ccx(<qubit_i>,<qubit_j>, <qubit_k>)
```
