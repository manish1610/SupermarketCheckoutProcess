# Supermarket Checkout process

This project implements a supermarket checkout system that calculates the total price of items added to the cart.

## Setup

### Prerequisites

- Docker installed on your machine.

### Project Structure

- `run.py`: Contains the main logic to process inputs and calculate totals.
- `tests.py`: Contains unit tests for the checkout process.
- `cart.py`, `checkout.py`, `store.py`, `pricing.py`: Modules defining the core functionality.
- `setup.py`: Initializes the store, discounts, and pricing rules.

### Building the Docker Image

To build the Docker image for this project, run:

```bash
docker build -t supermarket-checkout-process .
```

### Running Tests

By default, the Docker container is set to run the unit tests. After building the image, run:

```bash
docker run supermarket-checkout-process
```

### Running the Main Script

To run the Run script with the input cases mentioned in problem description:

```bash
docker run supermarket-checkout-process python run.py
```
