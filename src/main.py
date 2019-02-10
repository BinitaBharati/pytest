import sys
import csv
from dbservice import create_connection, create_person, count_person

def main():
    csvPath = str(sys.argv[1])
    f = open(csvPath)
    csv_f = csv.reader(f)
    conn = create_connection("test.db")
    counter = 0
    for row in csv_f:
       if (counter != 0):
           person = (row[0], row[1], row[2]);
           create_person(conn, person)
       counter += 1
    conn.commit()  
    totalRows = count_person(conn)
    totalRecCreated = counter - 1
    print(totalRecCreated ," records inserted. Total rows in DB are : ",totalRows)
    
    
       
    
argLen = len(sys.argv)
print ("input arg length = ", argLen)
for eachArg in sys.argv:
        print(eachArg)
#sys.argv[0] will be the python file name itself
if (len(sys.argv) != 2):
        print("You must specify a input CSV file path")
        quit()
if __name__ == '__main__':
    main()
	

