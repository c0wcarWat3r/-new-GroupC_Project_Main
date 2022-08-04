# Create a function with a parameter "forex"
def profitloss_function(forex):
    """
    function accepts 1 parameter: forex
    computes the difference in net profit each day
    if net profit is not consecutively higher, 
    it highlights the day where net profit is lower than previous day 
    and value difference
    """
    # Import path method from Pathlib
    from pathlib import Path 
    # Import csv module 
    import csv

    # create 4 empty lists
    net_profit=[]
    dd=[]
    d=[]
    result = []

    # # Instantiate a file path to the profit and loss csv file 
    file_path = Path.cwd()/"project_group"/"csv_reports"/"profit-and-loss-usd-42.csv"
    
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
    # Use the total number of days minus 1 so that the for loop would repeat for index 0 to 5.
    day=(len(net_profit)-1)  
    # i represents index
    # for each index in the range of 0-5,
    for i in range(day):
        # Find the difference between net profits for each consecutive day 
        diff=(net_profit[i+1]-net_profit[i])
        # Append the list of number of days when there is a profit deficit with the list of the difference in the empty list 'dd' (stands for daily difference)
        dd.append([d[i+1]]+[diff])

    # Convert nested list into a dictionary where day number is the key and the difference is the value 
    dictionary=dict(dd)
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
            result.append(f"[PROFIT DEFICIT] DAY: {float(pd)}, AMOUNT: SGD{abs(round((dictionary[pd]*forex),1))}\n")
            # If this condition is true, is_positive would change to false 
            is_positive= False
    # After running through the loop above, if is_positive does not change to false and remains true, 
    if is_positive==True:
            # Append this final message into the empty list 'results' instead 
            result.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    # return the list of results 
    return result