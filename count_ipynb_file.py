import os

ls = os.listdir()

count_ipynb_file = len(list(filter(lambda x : x.endswith("ipynb"),ls)))
count_r_file = len(list(filter(lambda x : x.endswith("r"),ls)))
print(f"Number of ipynb file is {count_ipynb_file} and number of R file is {count_r_file}")