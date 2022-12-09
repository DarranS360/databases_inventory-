# Shoe Inventory

This is a Python programme that helps manage the inventory of shoes in a shop. It will read from an inventory.txt file where the shoe data will be stored.
It keps track of shoe data including country of origin, model name, code for re-ordering, and current stock count. It also has the ability to manually add
new stock and update stock count when new stock comes in. 

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)
- [Credits](#credits)

## Features

- View all shoes in stock with all data
- Add new shoes to the inventory
- Update stock count
- Search for shoe with highest stock and mark as on sale
- Search for a specific shoe in the inventory and return its data
- Calculate total value of all shoes in stock

## Requirements

- Python 3.6 or higher
- Suitable IDE (like PyCharm or VSC)
- Creation ofa local txt file called "inventory.txt"

## Installation

1. Download a copy of the file: "inventory.py"
2. Install any of the above requirements lacking on local system
3. Create the txt file mentioned above
4. Run the programme on chosen IDE

## Usage

```python
# Function to give menu options to user to carry out all functions above
def main():
    # Create a menu
    menu = ["", "1. View all shoes", "2. Re-stock shoes", "3. Search for a shoe",
            "4. Calculate the total value for each shoe", "5. Find the shoe with the highest quantity",
            "6. Enter new shoe into system", "7. Exit"]
 ```
![menu](https://user-images.githubusercontent.com/116950436/206730308-b7ed276b-8fe0-4d6b-948b-8d0a4b3d9da1.png)

To use any of the features in the programme simply enter a number from the menu above into the terminal.
The file autmatically calls the `main()` function when the programme starts to show the menu.

To view all shoes simply return `1` to the programme and a table of shoes with their relevant info will appear like this:

![view_all](https://user-images.githubusercontent.com/116950436/206730706-a701d444-5fdc-402e-b80c-a7312008d1b0.png)

`2` will show you the show with the lowest stock and give you the option to update its stock.

Searching for a shoe simply requires enter `3`and then the code for the shoe you are looking up. A table similar to the view all table will appear, 
but this time only containing the info for the shoe code your entered.

If you would like to know how much each model of shoe is worth in total (total amount for all stock of that model) simply return `4` to the programme.
The information will be printed as follows:

![view_total](https://user-images.githubusercontent.com/116950436/206730726-e7a9436d-b760-40b4-ba38-d0d011661c57.png)


`5` will return the item to you that has the highest stock count and list it for sale:

![highest_stock](https://user-images.githubusercontent.com/116950436/206732447-5b8298fb-3171-42e4-951a-7c7f96bdb6b7.png)

To add a new shoe to the system return `6` and fill in the info when asked for it (see image below for example). This will append the new shoe to 
the "inventory.txt" file and update the list.

![input_new](https://user-images.githubusercontent.com/116950436/206730754-47629a25-78eb-4676-8799-bfe7cf8aa20d.png)

 Entering `7` will simply end the programme, allowing you to exit.

## Contributions

We welcome contributions to this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Push your branch to your forked repository.
5. Create a pull request.

## Credits

- [Darran Smith](https://github.com/DarranS360)
- [HyperionDev](https://hyperiondev.com)
