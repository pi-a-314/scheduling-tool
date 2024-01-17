import pandas as pd
import numpy as np
import get_input as gi
import tools

def solve(data, necessary, persons, startdate = np.datetime64('2023-08-01'), length = 6, interval = 'D'):
    """
Searches a solution for a timeframe considering the given constraints.

Constraint options: 
- necessary people
- ideally included people
- start date
- timeframe length 

Parameters:
data (pandas DataFrame): contains processed data from .csv
necessary (list): list of names (people who NEED be available)
persons (list): list of names (people who SHOULD be available)
startdate (np.datetime64): custom or preset earliest startdate for the timeframe
length (int) = custom or preset length of timeframe
daterange (str) = custom ('D'/'W') or preset ('D') quantifier for length (Day/ Week)

Returns:
3 top rows of a pandas DataFrame df_results

"""

    # the -1 because e.g. 07-01 + 6 days = 07-07, which would return 7 days, but 6 were expected
    delta = np.timedelta64(length - 1, interval)
    

    # take only the columns of people that were specified by user input
    data = data[persons]

    # create a new data frame with columns: 
    #  - start date
    #  - amount of people
    #  - sum of availability weights of all by user named people
    #  - names of named people
    df_results = pd.DataFrame(columns = ['date', 'count', 'weight', 'people'])
    df_results['count'] = pd.to_numeric(df_results['count'])
    df_results['weight'] = pd.to_numeric(df_results['weight'])
    
    # loop over all possible dates - ranging from the stardate to the last date - timedelta
    for i in np.arange(np.datetime64(startdate), np.datetime64(data.index[-1] - delta, 'D'), dtype = 'datetime64[D]'):
        
        counter = 0
        weight = 0
        people = []

        # loop over person list:
        for person in persons:

            # if the product of the column window from i to i+delta is not 0, we found a date, where the person is avaliable for the timedelta
            if data[person][i :i + delta].product() != 0:

                # increase counter, weight, add to "people" list, to save them in the df_result
                counter += 1
                people.append(person)
                weight += data[person][i :i + delta].product()
            
        
        # if all neccessary ppl are in the people list, and there is at least one person avaliable:
        if all(item in people for item in necessary) and counter > 0:
            
                # saving all possibilities
                df_results = df_results._append({'date': i, 'count': counter, 'weight': weight, 'people': people}, ignore_index = True)

    return df_results.nlargest(3, ['count', 'weight'])
            

        



if __name__ == "__main__":

    print("Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.")

    data, file = gi.transform_and_load()
    
    print(f"My search is based on {file}. Let us begin!")
    
    persons, necessary, time, startdate = gi.get_constraints(data)

    solution = solve(data,  necessary, persons = persons, length = time[0], interval = time[1])


    # to ensure a reasonable output is created, distinguish between:
    #  - up to three solutions perfectly fitting all constraints
    #  - up to three solutions that fits all constraints except the optional people
    #  - no solution possible under given constraints
    while time[0] >= 0:
        if not solution.empty:
            if len(solution['people'].iloc[0]) < len(persons):
                print("I wasn't able to find a solution that includes everyone. Here is the best timeframe I was able to find: ")
            if len(solution['people'].iloc[0]) > 1:
                print(f"From the {solution['date'].iloc[0]} on, there are {solution['count'].iloc[0]} people free for {tools.reformat_date(time)}.\n\rThese people are: {solution['people'].iloc[0]}\n\r")
                print(f"Here\'s also up to 3 best fitting solutions:")
                print(solution[['date', 'count', 'people']])
            else:
                print(f"From the {solution['date'].iloc[0]} on, there is {solution['count'].iloc[0]} person free for {tools.reformat_date(time)}.\n\rThis person is: {solution['people'].iloc[0]}\n\r")
                print(f"Here\'s also up to 3 best fitting solutions:")
                print(solution[['date', 'count', 'people']])
            break       
        
        # and if there is no solution:
        else:
            print("There is no solution with your constraints.\n\r")
            # ask for rerun with decreased timeframe
            re_run = input("Should I re-run the search with a smaller time window (Enter to skip)? ")
            
            # if one wants to rerun
            if re_run:
                
                # reduce timeframe
                time[0] = time[0]-1
                print(f"Trying with {tools.reformat_date(time)}")
                solution = solve(data, necessary, persons, length = time[0], interval = time[1])
            
            # otherwise: end program
            else: break

