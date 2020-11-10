# Python JSON Task 
## Task 
- Create a New Repo for this task
- .gitignore and README in a new pycharm project
- have the exchange_rates.json file available in your pycharm project/folder
- Display all the data from .json file
- iterate through the data and display exchange rate by country

## Pre-Requisites
__Necessary:__ You must have python installed.  
__Optional:__ It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

## Syntax:
1. Import the necessary modules:
```python
# importing json module
import json 
```
2. Load your  json file: 
```python
# loading the json file and printing all the information 
with open('exchange_rates.json') as jsonfile:
    all_information = json.load(jsonfile)
    print(all_information)
```
3. Loop through the nested dictionary to display rate information:
```python
#iterate through the data and print Rates by Country
    def print_rates(all_information):
        for key, value in all_information.items():
            # this is a way to loop through the nested dictionary 
            if isinstance(value, dict) and key == 'rates':
                print(key)
                print_rates(value)
            
            # this is really not clean, but it works
            elif key == 'base' or key == 'date':
                continue
            else:
                print(f'{key}: {value}')

    print_rates(all_information)
```