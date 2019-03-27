
# taking various csv file with same headers and combining them into one with and additional column which indicates 
# from which file this row of data came

import sys
import csv


def add_header(argv,output_file): #function to add header to the new output file
    try: #exception handling
        with open(argv[1],'r') as f: #opening the first file to extract column names from it
            d_reader=csv.DictReader(f) #initializing the reader object
            headers=d_reader.fieldnames #extracting the fieldnames which is the column names
            headers.append("filename") #appending new column filename
            try: #exception handling
                with open(output_file,'w',newline='') as f1: #creating new file for storing all the data
                    writer=csv.DictWriter(f1,fieldnames=headers) #initializing writer object
                    writer.writeheader() #writing the headers into output csv file
            except:
                print("Error creating output file.") #printing error message
                exit(1) #exiting the program
    except:
        print("Error opeing file") #printing error message 
        exit(1) #exiting the program


def append_data(argv,output_file): #function to append all the data into one file
    it=0 #variable to ignore the program name from the argument list
    for File in argv: #iterating over each file from the argument
        if(it==0):
            it=1
            continue
        try: #exception handling
            f3=open(File,'r') #trying to open current file from the argument list
        except:
            print("Error opening file: "+File) #printing error message with file name trying to open
            exit(1) #exiting program
        header=0 #variable to ignore the header from each file
        for row in f3: #iterating over all the data in the current file
            if(header==0):
                header=1
                continue
            row=row.split(',')#spiling the data and taking it in a list
            row.append(str(File)) #appending the filename to the list
            try: #exception handling
                with open(output_file,'a',newline='') as f:  #opening the csv file to append the current row of data
                    writer=csv.writer(f) #initializing the writer object
                    writer.writerow(row) #appending current row to the file
            except:
                print("Can't open output file") #printing error message
                exit(1) #exiting the program


def main(argv): #main function with command argument list as parameter
    l=len(argv) #getting the length of argument lsit
    output_file="new_csv.csv"
    if(l>1): #length should be greater than 1 , the first argument is the name of the program
        print("\nOutput file name is "+output_file+" by default") #prompt
        inp=input("Do you want to change the file name?(yes/no): ") #asking the user if he wants to change the file name
        if(inp=="yes"): # user entered yes
            output_file=input("Enter output file name: ")#asking for output file name
        if(output_file.endswith(".csv")==False): #checking if the user entered the .csv extension or not
            output_file+=".csv" #adding .csv extension
        add_header(argv,output_file) #calling function to add the headers in new created file
    else:
        print("Enter the csv files name as command argument") #prompt for the user
        print("python scrapping.py [file1] [file2] .... [file10]") #promt for the user
        exit(1) #exiting program
    append_data(argv,output_file) #calling function to add all the data into one file
    
    print("The program executed successfully.")
    

if __name__ == '__main__': 
	main(sys.argv) #calling main function with command argument list
