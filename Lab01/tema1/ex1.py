import random
import csv
import numpy as np

def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        csv_data = csv.reader(file)
        list_data = list(csv_data)
    return [name.strip() for row in list_data for name in row if name.strip()]

def random_list(filename, n):   
    students = read_file(filename)
    random_list = random.sample(students, n)
    #random_list = np.random.choice(students, size=n, replace=False)
    return random_list

def main():
    result = random_list("Lab01/tema1/lista.csv", 5)
    print(result)   
if __name__ == "__main__":
    main()
