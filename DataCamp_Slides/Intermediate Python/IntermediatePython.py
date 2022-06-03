'''
Line plot (1)
With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot. 
A general recipe is given here.

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

In the video, you already saw how much the world population has grown over the past years. Will it continue to do so? 
The world bank has estimates of the world population for the years 1950 up to 2100. The years are loaded in your workspace 
as a list called year, and the corresponding populations as a list called pop.

This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Python 
for data science Cheat Sheet and keep it handy!

Instructions
print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. 
Use two print() functions.
Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. 
Don't forget to finish off with the plt.show() function to actually display the plot.
'''

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
'''
Line plot (3)
Now that you've built your first line plot, let's start working on the data that professor Hans Rosling used to build his beautiful bubble chart. It was collected in 2007. Two lists are available for you:

life_exp which contains the life expectancy for each country and
gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.
GDP stands for Gross Domestic Product. It basically represents the size of the economy of a country. Divide this by the population and you get the GDP per capita.

matplotlib.pyplot is already imported as plt, so you can get started straight away.

Instructions
100 XP
Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
Don't forget to finish off with a plt.show() command, to actually display the plot.
'''

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Scatter Plot (1)
When you have a time scale along the horizontal axis, the line plot is your friend. But in many other cases, 
when you're trying to assess if there's a correlation between two variables, for example, the scatter plot is the better choice. 
Below is an example of how to build a scatter plot.

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()
Let's continue with the gdp_cap versus life_exp plot, the GDP and life expectancy data for different countries in 2007. 
Maybe a scatter plot will be a better alternative?

Again, the matplotlib.pyplot package is available as plt.

Instructions
Change the line plot that's coded in the script to a scatter plot.
A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
Finish off your script with plt.show() to display the plot. """

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Scatter plot (2)
In the previous exercise, you saw that the higher GDP usually corresponds to a higher life expectancy. 
In other words, there is a positive correlation.

Do you think there's a relationship between population and life expectancy of a country? The list life_exp from the 
previous exercise is already available. In addition, now also pop is available, listing the corresponding populations for 
the countries in 2007. The populations are in millions of people.

Instructions
Start from scratch: import matplotlib.pyplot as plt.
Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
Finish the script with plt.show() to actually display the plot. Do you see a correlation? """

# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Build a histogram (1)
life_exp, the list containing data on the life expectancy for different countries in 2007, is available in your Python shell.

To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.

matplotlib.pyplot is already available as plt.

Instructions
100 XP
Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; 
Python will set the number of bins to 10 by default for you.
Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations? """

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Build a histogram (2): bins
In the previous exercise, you didn't specify the number of bins. By default, Python sets the number of bins to 10 in that case. 
The number of bins is pretty important. Too few bins will oversimplify reality and won't show you the details. 
Too many bins will overcomplicate reality and won't show the bigger picture.

To control the number of bins to divide your data in, you can set the bins argument.

That's exactly what you'll do in this exercise. You'll be making two plots here. The code in the script already 
includes plt.show() and plt.clf() calls; plt.show() displays a plot; plt.clf() cleans it up again so you can start afresh.

As before, life_exp is available and matplotlib.pyplot is imported as plt.

Instructions
Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
Build another histogram of life_exp, this time with 20 bins. Is this better? """

# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()
---------------------------------------------------------------------------------------------------------------------------------
""" Build a histogram (3): compare
In the video, you saw population pyramids for the present day and for the future. Because we were using a histogram, 
it was very easy to make a comparison.

Let's do a similar comparison. life_exp contains life expectancy data for different countries in 2007. 
You also have access to a second list now, life_exp1950, containing similar data for 1950. 
Can you make a histogram for both datasets?

You'll again be making two plots. The plt.show() and plt.clf() commands to render everything nicely are already included. 
Also matplotlib.pyplot is imported for you, as plt.

Instructions
Build a histogram of life_exp with 15 bins.
Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data? """

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()
---------------------------------------------------------------------------------------------------------------------------------
""" Choose the right plot (2)
You're a professor in Data Analytics with Python, and you want to visually assess if longer answers on exam questions 
lead to higher grades. Which plot do you use?

Instructions
Possible Answers """

Line plot

Scatter plot # Answer

Histogram
---------------------------------------------------------------------------------------------------------------------------------
""" Labels
It's time to customize your own plot. This is the fun part, you will see your plot come to life!

You're going to work on the scatter plot with world development data: GDP per capita on the x-axis 
(logarithmic scale), life expectancy on the y-axis. The code for this plot is available in the script.

As a first step, let's add axis labels and a title to the plot. You can do this with the xlabel(), ylabel() 
and title() functions, available in matplotlib.pyplot. This sub-package is already imported as plt.

Instructions
The strings xlab and ylab are already set for you. Use these variables to set the label of the x- and y-axis.
The string title is also coded for you. Use it to add a title to the plot.
After these customizations, finish the script with plt.show() to actually display the plot. """

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# After customizing, display the plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Sizes
Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. Let's change this. Wouldn't 
it be nice if the size of the dots corresponds to the population?

To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country 
expressed in millions. You can see that this list is added to the scatter method, as the argument s, for size.

Instructions
Run the script to see how the plot changes.
Looks good, but increasing the size of the bubbles will make things stand out more.
Import the numpy package as np.
Use np.array() to create a numpy array from the list pop. Call this NumPy array np_pop.
Double the values in np_pop setting the value of np_pop equal to np_pop * 2. 
Because np_pop is a NumPy array, each array element will be doubled.
Change the s argument inside plt.scatter() to be np_pop instead of pop. """

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Colors
The code you've written up to now is available in the script.

The next step is making the plot more colorful! To do this, a list col has been created for you. 
It's a list with a color for each corresponding country, depending on the continent the country is part of.

How did we make the list col you ask? The Gapminder data contains a list continent with the continent each 
country belongs to. A dictionary is constructed that maps continents onto colors:

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
Nothing to worry about now; you will learn about dictionaries in the next chapter.

Instructions
Add c = col to the arguments of the plt.scatter() function.
Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). 
Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent. """

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Additional Customizations
If you have another look at the script, under # Additional Customizations, you'll see that there are two plt.text() 
functions now. They add the words "India" and "China" in the plot.

Instructions
Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot. """

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Motivation for dictionaries
To see why dictionaries are useful, have a look at the two lists defined in the script. countries contains the names of 
some European countries. capitals lists the corresponding names of their capital.

Instructions
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out. """

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
---------------------------------------------------------------------------------------------------------------------------------
""" Create dictionary
The countries and capitals lists are again available in the script. It's your job to convert this data to a dictionary 
where the country names are the keys and the capitals are the corresponding values. As a refresher, 
here is a recipe for creating a dictionary:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}
In this recipe, both the keys and the values are strings. This will also be the case for this exercise.

Instructions
With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. 
Beware of capitalization! Make sure you use lowercase characters everywhere.
Print out europe to see if the result is what you expected. """

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 
'france': 'paris', 
'germany': 'berlin',
'norway': 'oslo'}

# Print europe
print(europe)
---------------------------------------------------------------------------------------------------------------------------------
""" Dictionary Manipulation (1)
If you know how to access a dictionary, you can also assign a new value to it. To add a new key-value pair 
to europe you can use something like this:

europe['iceland'] = 'reykjavik'

Instructions
Add the key 'italy' with the value 'rome' to europe.
To assert that 'italy' is now a key in europe, print out 'italy' in europe.
Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value. """
Print out europe.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)
---------------------------------------------------------------------------------------------------------------------------------
""" Dictionary Manipulation (2)
Somebody thought it would be funny to mess with your accurately generated dictionary. 
An adapted version of the europe dictionary is available in the script.

Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands 
to the script to update and remove key:value pairs.

Instructions
The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
Print out europe to see if your cleaning work paid off. """

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
---------------------------------------------------------------------------------------------------------------------------------
""" Dictionary to DataFrame (1)
Pandas is an open source library, providing high-performance, easy-to-use data structures and 
data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where 
you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a 
country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

Three lists are defined in the script:

names, containing the country names for which data is available.
dr, a list with booleans that tells whether people drive left or right in the corresponding country.
cpc, the number of motor vehicles per 1000 people in the corresponding country.
Each dictionary key is a column label and each value is a list which contains the column elements.

Instructions
Import pandas as pd.
Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
key 'country' and value names.
key 'drives_right' and value dr.
key 'cars_per_cap' and value cpc.
Use pd.DataFrame() to turn your dict into a DataFrame called cars.
Print out cars and see how beautiful it is. """

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
---------------------------------------------------------------------------------------------------------------------------------
""" Dictionary to DataFrame (2)
The Python code that solves the previous exercise is included in the script. Have you noticed that the row labels 
(i.e. the labels for the different observations) were automatically set to integers from 0 up to 6?

To solve this a list row_labels has been created. You can use it to specify the row labels of the cars DataFrame. 
You do this by setting the index attribute of cars, that you can access as cars.index.

Instructions
Hit Run Code to see that, indeed, the row labels are not correctly set.
Specify the row labels by setting cars.index equal to row_labels.
Print out cars again and check if the row labels are correct this time. """

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
---------------------------------------------------------------------------------------------------------------------------------
""" CSV to DataFrame (2)
Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. 
The row labels were imported as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used 
as a row label? Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

Instructions
Run the code with Run Code and assert that the first column should actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
Has the printout of cars improved now? """

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)
---------------------------------------------------------------------------------------------------------------------------------
""" Square Brackets (1)
In the video, you saw that you can index and select Pandas DataFrames in many different ways. The simplest, 
but not the most powerful way, is to use square brackets.

In the sample code, the same cars data is imported from a CSV files as a Pandas DataFrame. To select only the 
cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']]
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.

Instructions
Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame.
Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])
---------------------------------------------------------------------------------------------------------------------------------
""" Square Brackets (2)
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. 
The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. 
Also, you're using the integer indexes of the rows here, not the row labels!

Instructions
Select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
---------------------------------------------------------------------------------------------------------------------------------
""" loc and iloc (2)
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following 
commands in the IPython Shell. Again, paired commands produce the same result.

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]
Instructions
Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.iloc[[4, 5], [1, 2]])
---------------------------------------------------------------------------------------------------------------------------------
""" loc and iloc (3)
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from 
beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]

Instructions
Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.iloc[:,[2]])

# Print out drives_right column as DataFrame
print(cars.loc[:, 'drives_right'])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0,2]])
---------------------------------------------------------------------------------------------------------------------------------
""" Equality
To check if two Python values, or variables, are equal you can use ==. To check for inequality, 
you need !=. As a refresher, have a look at the following examples that all result in True. 
Feel free to try them out in the IPython Shell.

2 == (1 + 1)
"intermediate" != "python"
True != False
"Python" != "python"
When you write these comparisons in a script, you will need to wrap a print() function around them to see the output.

Instructions
In the editor on the right, write code to see if True equals False.
Write Python code to check if -5 * 15 is not equal to 75.
Ask Python whether the strings "pyscript" and "PyScript" are equal.
What happens if you compare booleans and integers? Write code to see if True and 1 are equal. """

# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
'pyscript' == 'PyScript'

# Compare a boolean with an integer
True == 1
---------------------------------------------------------------------------------------------------------------------------------
""" Compare arrays
Out of the box, you can also use comparison operators with NumPy arrays.

Remember areas, the list of area measurements for different rooms in your house from Introduction to Python? 
This time there's two NumPy arrays: my_house and your_house. They both contain the areas for the kitchen, living room, 
bedroom and bathroom in the same order, so you can compare them.

Instructions
Using comparison operators, generate boolean arrays that answer the following questions:

Which areas in my_house are greater than or equal to 18?
You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
Make sure to wrap both commands in a print() statement so that you can inspect the output! """

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
---------------------------------------------------------------------------------------------------------------------------------
""" and, or, not (1)
A boolean is either 1 or 0, True or False. With boolean operators such as and, or and not, you can combine these 
booleans to perform more advanced queries on your data.

In the sample code, two variables are defined: my_kitchen and your_kitchen, representing areas.

Instructions
Write Python expressions, wrapped in a print() function, to check whether:
my_kitchen is bigger than 10 and smaller than 18.
my_kitchen is smaller than 14 or bigger than 17.
double the area of my_kitchen is smaller than triple the area of your_kitchen. """

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or  my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)
---------------------------------------------------------------------------------------------------------------------------------
""" and, or, not (2)
To see if you completely understood the boolean operators, have a look at the following piece of Python code:

x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))
What will the result be if you execute these three commands in the IPython Shell?

NB: Notice that not has a higher priority than and and or, it is executed first.

Instructions
Possible Answers """

True

False # Answer

Running these commands will result in an error.
---------------------------------------------------------------------------------------------------------------------------------
""" Boolean operators with NumPy
Before, the operational operators like < and >= worked with NumPy arrays out of the box. Unfortunately, this is not true 
for the boolean operators and, or, and not.

To use these operators with NumPy, you will need np.logical_and(), np.logical_or() and np.logical_not(). Here's an example 
on the my_house and your_house arrays from before to give you an idea:

np.logical_and(my_house > 13, 
               your_house < 15)
Instructions
Generate boolean arrays that answer the following questions:
Which areas in my_house are greater than 18.5 or smaller than 10?
Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, 
so that you can inspect the output. """

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
---------------------------------------------------------------------------------------------------------------------------------
""" Warmup
To experiment with if and else a bit, have a look at this code sample:

area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")
What will the output be if you run this piece of code in the IPython Shell?

Instructions
Possible Answers """

small

medium # Answer

large

The syntax is incorrect; this code will produce an error.
---------------------------------------------------------------------------------------------------------------------------------
""" if
It's time to take a closer look around in your house.

Two variables are defined in the sample code: room, a string that tells you which room of the house we're 
looking at, and area, the area of that room.

Instructions
Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
Write another if statement that prints out "big place!" if area is greater than 15. """

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")
---------------------------------------------------------------------------------------------------------------------------------
""" Customize further: elif
It's also possible to have a look around in the bedroom. The sample code contains an elif part that checks 
if room equals "bed". In that case, "looking around in the bedroom." is printed out.

It's up to you now! Make a similar addition to the second control structure to further customize 
the messages for different values of area.

Instructions
Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10. """

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")
---------------------------------------------------------------------------------------------------------------------------------
""" Driving right (1)
Remember that cars dataset, containing the cars per 1000 people (cars_per_cap) and whether people drive right 
(drives_right) for different countries (country)? The code that imports this data in CSV format into Python 
as a DataFrame is included in the script.

In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. 
Let's start simple and try to find all observations in cars where drives_right is True.

drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean 
Series to select observations from cars.

Instructions
Extract the drives_right column as a Pandas Series and store it as dr.
Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
Print sel, and assert that drives_right is True for all observations. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
---------------------------------------------------------------------------------------------------------------------------------
""" Cars per capita (1)
Let's stick to the cars data some more. This time you want to find out which countries have a high cars per capita figure. 
In other words, in which countries do many people have a car, or maybe multiple cars.

Similar to the previous example, you'll want to build up a boolean Series, that you can then use to subset the cars DataFrame 
to select certain observations. If you want to do this in a one-liner, that's perfectly fine!

Instructions
Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the 
corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
Print out car_maniac to see if you got it right. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
cars_maniac = cars[many_cars]

# Print car_maniac
print(cars_maniac)
---------------------------------------------------------------------------------------------------------------------------------
""" while: warming up
The while loop is like a repeated if statement. The code is executed over and over again, as long as the condition is True. 
Have another look at its recipe.

while condition :
    expression
Can you tell how many printouts the following while loop will do?

x = 1
while x < 4 :
    print(x)
    x = x + 1
Instructions
Possible Answers """

0
1
2
3 # Answer
4
---------------------------------------------------------------------------------------------------------------------------------
""" Add conditionals
The while loop that corrects the offset is a good start, but what if offset is negative? You can try to run the 
following code where offset is initialized to -6:

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)
but your session will be disconnected. The while loop will never stop running, because offset will be further decreased 
on every run. offset != 0 will never become False and the while loop continues forever.

Fix things by putting an if-else statement inside the while loop. If your code is still taking too long to run, 
you probably made a mistake!

Instructions
Inside the while loop, complete the if-else statement:
If offset is greater than zero, you should decrease offset by 1.
Else, you should increase offset by 1.
If you've coded things correctly, hitting Submit Answer should work this time.
If your code is still taking too long to run (or your session is expiring), you probably made a mistake. Check your code and make 
sure that the statement offset != 0 will eventually evaluate to FALSE! """

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1  
    print(offset)
---------------------------------------------------------------------------------------------------------------------------------
""" Loop over a list
Have another look at the for loop that Hugo showed in the video:

fam = [1.73, 1.68, 1.71, 1.89]
for height in fam : 
    print(height)
As usual, you simply have to indent the code with 4 spaces to tell Python which code should be executed in the for loop.

The areas variable, containing the area of different rooms in your house, is already defined.

Instructions
Write a for loop that iterates over all elements of the areas list and prints out every element separately. """

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for rooms in areas :
    print(rooms)
---------------------------------------------------------------------------------------------------------------------------------
""" Indexes and values (1)
Using a for loop to iterate over a list only gives you access to every list element in each run, one after the other. 
If you also want to access the index information, so where the list element you're iterating over is located, 
you can use enumerate().

As an example, have a look at how the for loop from the video was converted:

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("person " + str(index) + ": " + str(height))

Instructions
Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
Update the print() statement so that on each run, a line of the form "room x: y" should be printed, 
where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out 
this exact string, with the correct spacing. """

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))
---------------------------------------------------------------------------------------------------------------------------------
""" Loop over list of lists
Remember the house variable from the Intro to Python course? Have a look at its definition in the script. It's basically a 
list of lists, where each sublist contains the name and area of a room in your house.

It's up to you to build a for loop from scratch this time!

Instructions
Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of 
the room and y is the area of the room. """

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house :
    print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")
---------------------------------------------------------------------------------------------------------------------------------
""" Loop over dictionary
In Python 3, you need the items() method to loop over a dictionary:

world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))
Remember the europe dictionary that contained the names of some European countries as key and their capitals as 
corresponding value? Go ahead and write a loop to iterate over it!

Instructions
Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be 
printed out, where x is the key and y is the value of the pair. """

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() :
    print("the capital of " + key + " is " + str(value))
---------------------------------------------------------------------------------------------------------------------------------
""" Loop over DataFrame (1)
Iterating over a Pandas DataFrame is typically done with the iterrows() method. Used in a for loop, every observation is 
iterated over and on every iteration the row label and actual row contents are available:

for lab, row in brics.iterrows() :
    ...
In this and the following exercises you will be working on the cars DataFrame. It contains information on the cars per capita 
and whether people drive right or left for seven countries in the world.

Instructions
Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row 
label and one to print out all of the rows contents. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
---------------------------------------------------------------------------------------------------------------------------------
""" Loop over DataFrame (2)
The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. 
Luckily, you can easily select variables from the Pandas Series using square brackets:

for lab, row in brics.iterrows() :
    print(row['country'])
Instructions
Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", 
the second iteration "AUS: 731", and so on.
The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
---------------------------------------------------------------------------------------------------------------------------------
""" Add column (1)
In the video, Hugo showed you how to add the length of the country names of the brics DataFrame in a new column:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])
You can do similar things on the cars DataFrame.

Instructions
Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. 
You can use the string method upper() for this.
To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop. """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)
---------------------------------------------------------------------------------------------------------------------------------
""" Add column (2)
Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. 
On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination 
with a for loop is not the preferred way to go. Instead, you'll want to use apply().

Compare the iterrows() version with the apply() version to get the same result in the brics DataFrame:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)
We can do a similar thing to call the upper() method on every name in the country column. However, upper() is a method, 
so we'll need a slightly different approach:

Instructions
Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY 
should be added to cars, containing an uppercase version of the country names.
As usual, print out cars to see the fruits of your hard labor """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print
print(cars)
---------------------------------------------------------------------------------------------------------------------------------
""" Random float
Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. 
You're going to use randomness to simulate a game.

All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, 
you'll be using two functions from this package:

seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, 
it takes an integer of your choosing. If you call the function, no output will be generated.
rand(): if you don't specify any arguments, it generates a random float between zero and one.

Instructions
Import numpy as np.
Use seed() to set the seed; as an argument, pass 123.
Generate your first random float with rand() and print it out. """

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
---------------------------------------------------------------------------------------------------------------------------------
""" Determine your next move
In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice. 
We can perfectly code this with an if-elif-else construct!

The sample code assumes that you're currently at step 50. Can you fill in the missing pieces to finish the script? 
numpy is already imported as np and the seed has been set to 123, so you don't have to worry about that anymore.

Instructions
Roll the dice. Use randint() to create the variable dice.
Finish the if-elif-else construct by replacing ___:
If dice is 1 or 2, you go one step down.
if dice is 3, 4 or 5, you go one step up.
Else, you throw the dice again. The number of eyes is the number of steps you go up.
Print out dice and step. Given the value of dice, was step updated correctly? """

# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
---------------------------------------------------------------------------------------------------------------------------------
""" The next step
Before, you have already written Python code that determines the next step based on the previous step. 
Now it's time to put this code inside a for loop so that we can simulate a random walk.

numpy has been imported as np.

Instructions
Make a list random_walk that contains the first step, which is the integer 0.
Finish the for loop:
The loop should run 100 times.
On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
Next, let the if-elif-else construct update step for you.
The code that appends step to random_walk is already coded.
Print out random_walk. """

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
---------------------------------------------------------------------------------------------------------------------------------
""" How low can you go?
Things are shaping up nicely! You already have code that calculates your location in the Empire State Building 
after 100 dice throws. However, there's something we haven't thought about - you can't go below 0!

A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. 
For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:

x = max(10, x - 1)

Instructions
Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
Hit Submit Answer and check the contents of random_walk. """

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
---------------------------------------------------------------------------------------------------------------------------------
""" Simulate multiple walks
A single random walk is one thing, but that doesn't tell you if you have a good chance at winning the bet.

To get an idea about how big your chances are of reaching 60 steps, you can repeatedly simulate the random walk 
and collect the results. That's exactly what you'll do in this exercise.

The sample code already sets you off in the right direction. Another for loop is wrapped around the code you already wrote. 
It's up to you to add some bits and pieces to make sure all of the results are recorded correctly.

Note: Don't change anything about the initialization of all_walks that is given. Setting any number inside the 
list will cause the exercise to crash!

Instructions
Fill in the specification of the for loop so that the random walk is simulated 10 times.
After the random_walk array is entirely populated, append the array to the all_walks list.
Finally, after the top-level for loop, print out all_walks. """

# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range (10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
---------------------------------------------------------------------------------------------------------------------------------
""" Visualize all walks
all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a NumPy 
array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.

The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.

Instructions
Use np.array() to convert all_walks to a NumPy array, np_aw.
Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the 
position after 1 throw for the 10 random walks.
Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time? """

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Plot the distribution
All these fancy visualizations have put us on a sidetrack. We still have to solve the million-dollar problem: What are the 
odds that you'll reach 60 steps high on the Empire State Building?

Basically, you want to know about the end points of all the random walks you've simulated. These end points have a certain 
distribution that you can visualize with a histogram.

Note that if your code is taking too long to run, you might be plotting a histogram of the wrong data!

Instructions
To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. 
Store this NumPy array as ends.
Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot. """

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
---------------------------------------------------------------------------------------------------------------------------------
""" Calculate the odds
The histogram of the previous exercise was created from a NumPy array ends, that contains 500 integers. 
Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than 
or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number 
by 500, the total number of simulations.

Well then, what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game? 
The ends array is everything you need; it's available in your Python session so you can make calculations in the IPython Shell.

Instructions
Possible Answers """

48.8%

76.6%

78.4% # Answer

95.9%
---------------------------------------------------------------------------------------------------------------------------------