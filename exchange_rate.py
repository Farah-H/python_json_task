# importing json module
import json 

# loading the json file and printing all the information 
with open('exchange_rates.json') as jsonfile:
    all_information = json.load(jsonfile)
    print(all_information)

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