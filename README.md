
Copy code
# Store Pricing Calculator

This Python script calculates the total price of a list of products based on their individual prices and available offers.

## Description

The `Store` class contains the pricing details of various products and their corresponding offer prices. It provides a method to calculate the total price of products entered by the user, considering any applicable offers.

## Features

- Calculate total price based on actual prices and special offer prices.
- Handles non-existent products gracefully by informing the user.

## Class Details

### Store

#### Attributes

- `actual_prices` (dict): A dictionary containing the actual prices of products.
- `offer_prices` (dict): A dictionary containing the offer details of products in the form `(quantity, offer_price)`.

#### Methods

- `total_price(user_input)`: Takes a string of product codes as input and returns the total price after applying relevant offers.

## Usage

1. Clone the repository.
2. Run the `store.py` script.
3. Enter the product codes as a single string when prompted.
