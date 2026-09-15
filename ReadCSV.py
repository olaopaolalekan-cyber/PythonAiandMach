#Python command to 
import csv

#Name of the csv file
filepath = "Books.csv"

# To open the csv file in read only mode
with open(filepath, mode="r") as file:
    #create a csv reader object
    csv_reader = csv.reader(file)
    #counter for the number of rows
    row_count = 0

    #read each row in the file
    for row in csv_reader:
        print(row)
        row_count += 1

#display the totl number of rows
print(f"\nTotal rows: {row_count}")
