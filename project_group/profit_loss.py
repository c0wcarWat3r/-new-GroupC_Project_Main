# Create a function with a parameter "forex"
def profitloss_function(forex):
    # Import path method from Pathlib
    from pathlib import Path 
    # Import csv module 
    import csv

    # # Instantiate a file path to the profit and loss csv file 
    ## file path to test
    file_path = Path.cwd()/"project_group"/"csv_49"/"profit-and-loss-49.csv"
    ## another file path to test
    
    ## file path for submission 
    # file_path = Path.cwd()/"project_group"/"csv_reports"/"profit-and-loss-usd-42.csv"
    

    # create 4 empty lists
    net_profit=[]
    dd=[]
    d=[]
    result = []

    # Open file in read mode 
    with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
        # Create a reader object
        reader = csv.reader(file)
        # Skip the headers
        next(reader)
        for line in reader:
            # Append only the net profits for each day to the empty list 'net_profit' and convert them to floats (so difference can be calculated later)
            net_profit.append(float(line[4]))
            # Append the number of days to the empty list 'd' (stands for days)
            d.append(line[0])
    # If there are 6 days, range would repeat the for loop from index 0 to 6. 
    # In this case as indexing in python starts from 0, we would need to access the cash on hand values from index 0 to index 5 for all 6 days
    # Hence, we used the total number of days minus 1 so that the for loop would repeat for index 0 to 5.
    day=(len(net_profit)-1)  
    # i represents index and range would give 0 to the highest index (in this case 6 days will have indices 0-5 )
    # for each index in the range of 0-5,
    for i in range(day):
        # Find the difference between net profits for each consecutive day 
        diff=(net_profit[i+1]-net_profit[i])
        # Append the list of number of days when there is a profit deficit with the list of the difference in the empty list 'dd' (stands for daily difference)
        dd.append([d[i+1]]+[diff])

    # Convert nested list into a dictionary where day number is the key and the difference is the value 
    dictionary=dict(dd)
    # If the api function incurs a key error and prints the note because of the exception handling, 
    # we would be multiplying the difference by a string which would incur a type error
    # Hence, we used try to run the code as follows:
    try: 
        # set a condition to a new variable stating that it is true 
        is_positive= True
        # Use a for loop to access the values in the dictionary 
        for pd in dictionary:
            # dictionary[pd] accesses the values (profit difference) and pd is the key 
            # If the profit difference is less than 0,
            if dictionary[pd] < 0 : 
                # Append the final message into the empty list 'results'
                # Use dictionary[pd]*forex to convert the difference to SGD 
                # abs() to convert the negative values to a positive value 
                # round() to round the difference to 1 decimal place
                result.append(f"[PROFIT DEFICIT] DAY: {float(pd)}, AMOUNT: SGD{round(abs(dictionary[pd]*forex),1)}\n")
                # If this condition is true, is_positive would change to false 
                is_positive= False
        # After running through the loop above, if is_positive does not change to false and remains true, 
        if is_positive==True:
                # Append this final message into the empty list 'results' instead 
                result.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # return the list of results 
        return result
    # If a type error occurs, 
    except TypeError: 
        # return this final message instead
        return f"Limit reached"