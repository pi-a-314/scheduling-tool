# scheduling-tool
### Goal
scheduling_tool.py is a program for dealing with finding an optimal timeslot that fits the availability of a specified amount of people.
### Motivation
We wanted to create a tool that made it easier to find timeslots that fit the majority of a group, for example when planning a holiday, since it can be a bit tedious to check all contraints and limitations by hand.
Now, you could:
- ask every one to enter the dates that fit them in a .csv you make available (mind the structure!)
- and use our tool to plan trips considering several constraints
    - customizable starting date
    - customizable participants: not everone in the database is considered
    - "Necessary to be included in planning": if there is no timeframe, that fits everyone, our program will give the next best one. But some people are necessary for the trip to happen (i.e. because they are hosting or designated drivers), so specify them in this step.
### Structure
Contained in the repo are:
- Files containing functions used in scheduling_tool.py
    - tools.py
    - get_input.py
- Data folder: 
    - Containts premade .csv for trying the tool

### Functionality
- Input / Optional custom .csv to be loaded (must be in \data folder):
    - Columns: people or names to be used
    - Index: Dates to be considered for scheduling
    - Data: weighting integer (0-2), 0: person X is not available, 1: person X is avaiable, 2: day fits person X best

    Example csv:
    |          | Person 1 | Person 2|
    | -------- | ------- | ------- |
    | 01.01.1970 | 0 | 1 |
    | 02.01.1970 | 1 | 0 |
    | 03.01.1970 | 2 | 2 |

- User adjustments possible:
    - People (.csv columns) to be considered in planning
    - People that must necessarily be available in that timeframe (that are for example hosting an event)
    - Length of timeframe to be found
    - Optional custom earliest startdate

- Output: timeframe best fitting for given constraints, people participating as a tuple


## Getting started
### Prerequisites
A working python environment with:
- pandas 
- numpy
### Installation
Clone the repo

## Usage 
- add your own csv in data folder if wanted

Execute in working directory:
```bash
python scheduling_tool.py
```

## Usage examples
- '-' signifies user input
### 1: Load own csv
```bash
"Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.
Do you want to use a custom .csv (Enter to skip)? - yes
What file do you want to load? vacations_w.csv
My search is based on data/vacations_w.csv. Let us begin!
Do you want to specify persons and times? (choose from used csv or press Enter to use defaults) - yes

Travel buddies are:['Barbie', 'Ken', 'Jasmine', 'Merida', 'Cinderella', 'Charming', 'Belle', 'Ariel', 'Pocahontas', 'Elsa', 'Aurora', 'Mulan']

How many Travel Buddies do you want to add to go on vacation? - 3
How many people of those need be present? - 0

Please add names one after the other:
Who else should be added that doesn't necessarily need to be there? - Barbie
Who else should be added that doesn't necessarily need to be there? - Mulan
Who else should be added that doesn't necessarily need to be there? - Ariel

The total timeframe available is: 2023-07-20 00:00:00 to 2023-10-15 00:00:00
For how long should the people be available (Enter to use default (6 days))? - 4 days

What is the starting date I should start searching from (Enter to use default)?

From the 2023-09-16 00:00:00 on, there are 3 people free for 4 days.
These people are: ['Barbie', 'Mulan', 'Ariel']

Here's also up to 3 best fitting solutions:
         date  count                  people
32 2023-09-16      3  [Barbie, Mulan, Ariel]
39 2023-09-23      3  [Barbie, Mulan, Ariel]
25 2023-09-09      3  [Barbie, Mulan, Ariel]"
```

### 2: Default csv and default values
```bash
"Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.
Do you want to use a custom .csv (Enter to skip)? - [ Enter ]
My search is based on data/vacations.csv. Let us begin!
Do you want to specify persons and times? (choose from used csv or press Enter to use defaults) - [ Enter ]
From the 2023-09-22 00:00:00 on, there are 11 people free for 6 days.
These people are: ['Gudrun', 'Dankwart', 'Sigurd', 'Brynhild', 'Siegfried', 'Gernot', 'Gunther', 'Kriemhild', 'Hildebrand', 'Wolfhart', 'Giselher']

Here's also up to 3 best fitting solutions:
         date  count                                             people
27 2023-09-22     11  [Gudrun, Dankwart, Sigurd, Brynhild, Siegfried...
24 2023-09-19     10  [Gudrun, Dankwart, Sigurd, Brynhild, Siegfried...
25 2023-09-20     10  [Gudrun, Dankwart, Sigurd, Brynhild, Siegfried..."
```


### 3: Choose constraint: necessary people (default csv)
```bash
"Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.
Do you want to use a custom .csv (Enter to skip)? - [ Enter ]
My search is based on data/vacations.csv. Let us begin!
Do you want to specify persons and times? (choose from used csv or press Enter to use defaults) - yes

Travel buddies are:['Gudrun', 'Dankwart', 'Sigurd', 'Brynhild', 'Siegfried', 'Gernot', 'Gunther', 'Kriemhild', 'Hildebrand', 'Wolfhart', 'Alberich', 'Giselher']

How many Travel Buddies do you want to add to go on vacation? - 3
How many people of those need be present? - 1

Please add names one after the other:
Who is necessary in the planning ? - Sigurd
Who else should be added that doesn't necessarily need to be there? - Gunther
Who else should be added that doesn't necessarily need to be there? - Kriemhild

The total timeframe available is: 2023-07-20 00:00:00 to 2023-10-15 00:00:00
For how long should the people be available (Enter to use default (6 days))? - 1 week

What is the starting date I should start searching from (Enter to use default)? - 2023-08-03

From the 2023-09-10 00:00:00 on, there are 3 people free for 1 week.
These people are: ['Sigurd', 'Gunther', 'Kriemhild']

Here's also up to 3 best fitting solutions:
         date  count                        people
17 2023-09-10      3  [Sigurd, Gunther, Kriemhild]
18 2023-09-11      3  [Sigurd, Gunther, Kriemhild]
19 2023-09-12      3  [Sigurd, Gunther, Kriemhild]"
```

### 4: Constraint violation found (default csv)
```bash
"Hello! I am a scheduling tool made to find a timeframe that fits all people specified in the following.
Do you want to use a custom .csv (Enter to skip)? - [ Enter ]
My search is based on data/vacations.csv. Let us begin!
Do you want to specify persons and times? (choose from used csv or press Enter to use defaults) - yes

Travel buddies are:['Gudrun', 'Dankwart', 'Sigurd', 'Brynhild', 'Siegfried', 'Gernot', 'Gunther', 'Kriemhild', 'Hildebrand', 'Wolfhart', 'Alberich', 'Giselher']

How many Travel Buddies do you want to add to go on vacation? - 5
How many people of those need be present? - 2

Please add names one after the other:
Who is necessary in the planning ? - Alberich
Who is necessary in the planning ? - Sigurd 
Who else should be added that doesn't necessarily need to be there? - Kriemhild
Who else should be added that doesn't necessarily need to be there? - Gunther
Who else should be added that doesn't necessarily need to be there? - Wolfhard
The specified Person(s) do not exist in the database!
Who else should be added that doesn't necessarily need to be there? - Wolfhart

The total timeframe available is: 2023-07-20 00:00:00 to 2023-10-15 00:00:00
For how long should the people be available (Enter to use default (6 days))? - 4 Days

What is the starting date I should start searching from (Enter to use default)? - 2023-08-15

There is no solution with your constraints.

Should I re-run the search with a smaller time window (Enter to skip)? - [ Enter ]"
```

## Authors and Contact
pi-a-314, MeinChef, Mini11e

