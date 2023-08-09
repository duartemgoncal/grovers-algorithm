<h1 align="center">
  Grover's Algoithm
</h1>

<div align='center'>
<img src="https://static.wikia.nocookie.net/muppet/images/e/e9/Grover2.jpg/revision/latest?cb=20190610143055" alt="drawing" width="500"/>
</div>
<h4 align="center">Implementation of a general Grover's Algorithm for quamtum searching.</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

## About

This is a general implementation of Grover's Algorithm for quantum searching. It is based on the paper [Grover's Algorithm for Quantum Searching](https://arxiv.org/pdf/quant-ph/9605043.pdf) by Lov K. Grover.


## Installation

To install the algorithm, clone the repository and install the dependencies:
  
  ```bash
  $ git clone https://github.com/DuarteMGoncal/grovers-algorithm.git
  $ cd grovers-algorithm
  $ pip install -r requirements.txt
  ```
  **Note:** It is reccomended to use a virtual environment, like `venv` or `conda`. For more information see the [Python Docs](https://docs.python.org/3/library/venv.html) or the [Conda Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


## Usage

The algorithm is implemented in the file `grover.py`. The file `main.ipynb`(soon) contains an example of how to use the algorithm.

The algorithm is implemented as a class, which is initialized with the following parameters:

- `number_list`: A list of numbers to be searched
- `cycles`: The number of Grover cycles to be run
- `restrict`: A boolean value that indicates if the algorithm should restrict the search to 7 bits or less. If `restrict` is `False`, the algorithm will search for any number in the list, regardless of its size.


## License

MIT

---

> GitHub [@DuarteMGoncal](https://github.com/DuarteMGoncal) &nbsp;&middot;&nbsp;
> Twitter [@DuarteMGoncal](https://twitter.com/DuarteMGoncal)

