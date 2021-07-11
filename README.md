Objective:-
A friend's grandma regularly knits socks. But she spends way too much money on the wool at the craft shop next door. You want to program her a comparison portal for wool. The portal is intended to display wool ball information from various websites. To do this, you want to start with a first website, the Wool place1, Read out information
automatically. You are interested in the price, the delivery time, the needle size and the composition. You first selected the following balls for which you have the information want:
----------------------------------
brand      | description          |
----------------------------------|
DMC	       | Natura XL            |
----------------------------------|
Drops	     | saffron              |
----------------------------------|
Drops	     | Baby merino mix      |
----------------------------------|
Rooster	   | Alpacca Speciale     |
----------------------------------|
Stylecraft | Special double knit  |
----------------------------------|

You are planning big things for your wool comparison portal. Correspondingly, with this first website you already think about how you can encapsulate code so that you can
add more websites and functionalities later. At first, you only want the data in a simple, practical format save as a file.

Execution:-
In the main file(Markt.py), two functions are written. One to search for the brand in the given website and collect data from it and another function to save that data into a file and also to a dataframe.
The website URL and the brand name are given as input parameters into the function so that the same function code works for all the websites and brands.
By creating objects for every website and brand name to be searched for, both the functions and all the variables are made accessible throughout the program.

In the test program(Test_Markt.py), two test functions are written to test both the functionalities written in the main file.
Here, first test function is testing the price of a brand named "DMC Natura XL", against some random price. It gives false result as the correct price value is not provided for comparison.
Second function tests for the brand name saved in csv file when main program is run.
