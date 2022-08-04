import api,cash_on_hand,overheads,profit_loss
from pathlib import Path

# As Alpha Vantage standard API call frequency is only 5 calls per minute, a message would be printed when user runs the code too many times 
# With a different message, the dictionary would change and the system would not be able to find the exact key for rate, incurring a key error
# Hence, we used try run the code as follows:
try: 
    # assign the rate_function (that extracts the exchange rate) to a variable 
    forex = api.rate_function()
    # assign the api_function to a variable 
    a = api.api_function()
    # assign the overhead_function to a variable 
    b = overheads.overhead_function(forex)
    # assign the coh_function to a variable 
    c = cash_on_hand.coh_function(forex)
    # assign the profitloss_function to a variable 
    d = profit_loss.profitloss_function(forex)

    # create a text file in the current working directory 
    file_path=Path.cwd()/"project_group"/"Summary_report.txt"
    file_path.touch()
    # Open the text file in write mode 
    with file_path.open(mode="w", encoding = "UTF-8") as file: 
        # Use .write() to write the final message returned in api_function into the file 
        file.write(a)
        # Use .write() to write the final message returned in overhead_function into the file 
        file.write(b)
        # Use .writelines() to write the final message returned in coh_function ('results' returned is a list)
        file.writelines(c)
        # Use .writelines() to write the final message returned in profitloss_function ('results' returned is a list)
        file.writelines(d)
# when a key error occurs, stop the programme from proceeding using pass 
except KeyError: 
    pass
