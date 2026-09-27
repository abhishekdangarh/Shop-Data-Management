### Shop Stock Management System

A simple, interactive command-line Python application designed to track and manage retail inventory. The system automates item classification by dynamically assigning a quality or pricing **Grade** based on the retail value, helping shop owners monitor stock values and levels seamlessly. 

### 🚀 Features

* **Add New Items:** Register items with an ID, name, price, and initial quantity.
* **Dynamic Grade Allocation:** Calculates grades automatically based on the price tier: 

  * Prices ≤ ₹1000 receive a grade of "0".
  * Prices above ₹1000 step up through grades A to Z for every ₹200 increment (items with exceptionally high prices receive a "Z+").
* **Inventory Tracking:** Update stock levels instantly using specific entry prompts for buying (adding stock) and selling items.
* **Grade-Based Search:** Filter available inventory instantly by its assigned grade.
* **Comprehensive Metrics:** View total available inventory units alongside the combined financial valuation of the current warehouse stock.

### 🛠️ Code Structure Overview

The application utilizes a procedural layout structured around global state (items) and standalone functions: 

FunctionPurpose
**calculate_grade(price)**
Evaluates a custom pricing tier calculation using a letter-mapping array.
**add_item()**
Prompts user for inputs and appends the new item dictionary to the list.
**display_items()**
Lists all items that currently have a stock quantity greater than zero.
**add_stock() / sell_item()**
Standard increments and decrements for active item inventory checking constraints.
**search_by_grade()**
Displays items matching a specific grade string query.
**stock_details()**
Evaluates and loops through total quantities and overall monetary valuations.

### 💻 How To Run

1. Make sure you have **Python 3.x** installed.
2. Save the script code locally as main.py.
3. Open your terminal or command prompt and navigate to the directory where the file is stored.
4. Run the script using: 

bash

python main.py

Use code with caution.
5. Follow the terminal menu prompt selections from 1 to 7 to operate the system.
