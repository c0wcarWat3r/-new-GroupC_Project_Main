# Create a function with a parameter "forex"
def overhead_function(forex):
    # Import path method from Pathlib
    from pathlib import Path 
    # Import csv module 
    import csv

    # create an empty list to store the category and value of overheads
    list = []
    # create an empty list to store the value of overheads
    overheads = []

    # instantiate a file path to overheads csv file in current working directory 
    # file_path = Path.cwd()/"csv_reports_game"/"overheads-day-42.csv"
    file_path = Path.cwd()/"csv_reports2"/"overheads.csv"

    # open the csv file in read mode 
    with file_path.open(mode="r",encoding="UTF-8",newline="") as file: 
        # create a reader object 
        reader = csv.reader(file)
        # skip the headers
        next(reader)
        
        for line in reader:
            # append the value of overheads to the empty list
            overheads.append(float(line[1]))
            # shift the values in front of category
            line.sort()
            # append the sorted lists to an empty list
            list.append(line)

    # convert the list of sublists into a dictionary 
    dictionary = dict(list)

    # find the max value in the overheads list to see what is the value of the highest overhead 
    maximum = max(overheads)
    # convert the highest overhead value to a string 
    key = str(maximum)
    # use the key to find the value which the category of the highest overhead
    value = dictionary[key]
    # If the api function incurs a key error and prints the note because of the exception handling, 
    # we would be multiplying the overheads by a string which would incur a type error
    # Hence, we used try to run the code as follows:
    try: 
        # Return the final message, converting the overhead value to SGD and using round() to round the value up to 1 decimal place
        return f"[Highest Overheads] {value}: SGD{round(maximum*forex,1)}"
    # If a type error occurs,
    except TypeError: 
        # return this final message 
        return f"Limit reached"


    



