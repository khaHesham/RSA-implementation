# RSA-implementation

This is a Python implementation of the RSA algorithm, which is a public-key cryptosystem that can be used for encryption and digital signatures. The RSA algorithm is based on the mathematical problem of factoring large numbers, which is believed to be hard to solve.

## Features

- Generate public and private keys using the RSA algorithm
- Encrypt and decrypt messages using the public and private keys
- Sign and verify messages using the private and public keys
- Break the RSA encryption by finding the factors of the modulus using a brute-force approach

## Requirements

- Python 3.6 or higher
- sympy library for mathematical operations

## Usage

- To run the RSA algorithm, execute the RSA.py file as follows:

```bash
python RSA.py
```

- To run the client-server communication using RSA encryption and signatures, execute the client.py and server.py files as follows:

```bash
python server.py
python client.py
```

- To run the analysis of the RSA algorithm, open the eff.ipynb file in a Jupyter notebook and run the cells.

- To run the breakRSA.py file, which attempts to break the RSA encryption by finding the factors of the modulus, execute it as follows:

```bash
python breakRSA.py
```

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.
