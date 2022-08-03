def coh_function(forex): 
    # Import path method from Pathlib
    from pathlib import Path 
    # Import csv module 
    import csv
    
    # Create 4 empty lists 
    coh=[]
    dd=[]
    d=[]
    results = []

    ## file_path = Path.cwd()/"csv_reports_game"/"cash-on-hand-usd-42.csv"

    # Instantiate a file path to the cash on hand csv file 
    file_path = Path.cwd()/"csv_reports2"/"cash on hand.csv"
    # Open file in read mode 
    with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
        # Create a reader object
        reader = csv.reader(file)
        # Skip the headers
        next(reader)
        for line in reader:
            # Append the cash on hand for each day to the empty list 'coh' and convert them to floats (so difference can be calculated later)
            coh.append(float(line[1]))
            # Append the number of days to the empty list 'd' (stands for days)
            d.append(line[0])
    # If there are 6 days, range would repeat the for loop from index 0 to 6. 
    # In this case as indexing in python starts from 0, we would need to access the cash on hand values from index 0 to index 5 for all 6 days
    # Hence, we used the total number of days minus 1 so that the for loop would repeat for index 0 to 5.
    day=(len(coh)-1) 
    # i represents index and range would give 0 to the highest index (in this case 6 days will have indices 0-5 )
    # for each index in the range of 0-5,
    for i in range(day):
        # Find the difference between cash on hand for each consecutive day 
        diff=(coh[i+1]-coh[i])
        # Append the list of number of days when there is a cash deficit with the list of the difference in the empty list 'dd' (stands for daily difference)
        dd.append([d[i+1]]+[diff])

    # Convert nested list into a dictionary where the day number is the key and the difference is the value 
    dictionary =dict(dd)
    # If the api function incurs a key error and prints the note because of the exception handling, 
    # we would be multiplying the difference by a string which would incur a type error
    # Hence, we used try to run the code as follows:
    try: 
        # set a condition to a new variable stating that it is true 
        is_positive= True
        # Use a for loop to access the values in the dictionary 
        for cd in dictionary:
            # dictionary[cd] accesses the values (cash on hand difference) and cd is the key 
            # If the cash on hand difference is less than 0,
            if dictionary[cd] < 0: 
                # Append the final message into the empty list 'results'
                # Use dictionary[cd]*forex to convert the difference to SGD 
                # abs() to convert the negative values to a positive value 
                # round() to round the difference to 1 decimal place
                results.append(f"[CASH DEFICIT] DAY: {cd} AMOUNT: SGD{abs(round(((dictionary[cd])*forex),1))}")
                # If this condition is true, is_positive would change to false 
                is_positive= False 
        # After running through the loop above, if is_positive does not change to false and remains true, 
        if is_positive==True:
            # Append this final message into the empty list 'results' instead 
            results.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # return the list of results 
        return results
    # If a type error occurs, 
    except TypeError: 
        # return this final message instead
        return f"Limit reached"

    