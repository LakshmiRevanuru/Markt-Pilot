# Markt-Pilot
This repository contains code for Markt-Pilot Software Challenge

In the main file(Markt.py), two functions are written. One to search for the brand in the given website and collect data from it and another function to save that data into a file and also to a dataframe.
The website URL and the brand name are given as input parameters into the function so that the same function code works for all the websites and brands.
By creating objects for every website and brand name to be searched for, both the functions and all the variables are made accessible throughout the program.

In the test program(Test_Markt.py), two test functions are written to test both the functionalities written in the main file.
Here, first test function is testing the price of a brand named "DMC Natura XL", against some random price. It gives false result as the correct price value is not provided for comparison.
Second function tests for the brand name saved in csv file when main program is run.
