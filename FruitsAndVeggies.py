import csv
import re

def checkList(vegeta, month):
    with open('Database.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    # This should be user input
    shoppingList = ['Apples','Oranges','Pears','Lettuce','Corn']

    print(month)
    produce = produce_list(data, associated_column(month), vegeta)
    return produce





                
def produce_list(data, month, vegeta):

    produce = []
    
    for i in range(1,len(data)):
        if vegeta == data[i][0].lower().strip():
            print(month)
            return(data[i][month])

    return "FALSE"

def associated_column(currentDate):

    if currentDate == 'Jan':
        dateColumn = 1
    elif currentDate == 'Feb':
        dateColumn = 2
    elif currentDate == 'Mar':
        dateColumn = 3
    elif currentDate == 'Apr':
        dateColumn = 4
    elif currentDate == 'May':
        dateColumn = 5
    elif currentDate == 'Jun':
        dateColumn = 6
    elif currentDate == 'Jul':
        dateColumn = 7
    elif currentDate == 'Aug':
        dateColumn = 8
    elif currentDate == 'Sep':
        dateColumn = 9
    elif currentDate == 'Oct':
        dateColumn = 10
    elif currentDate == 'Nov':
        dateColumn = 11
    elif currentDate == 'Dec':
        dateColumn = 12
    else:
        dateColumn = 0

    return dateColumn
        
if __name__ == '__main__':
    print(checkList("apples","Oct"))
    print(checkList("celery",1))
    print(checkList("=lery",1))
