# vtu_results
----------------------------------------------------------------------------------------------------------------------------------------

Scrapes vtu results from the website - http://results.vtu.ac.in based on the usn number.
This can come handy when there is too much traffic on the server and a browser is unable to open the website.
This situation occurs very often specially on the day when the results are announced. At this time the crowd rushes to the server and so it somewhat stops responding.

-----------------------------------------------------------------------------------------------------------------------------------------

There are two files i.e, 1. vtu-result-recursive and 2. vtu-result-iterative.
The output is same in both the files.
The only difference is there while parsing the webpage.
vtu-res-recursive uses a recursive approach to grab the webpage contents.
vtu-res-iterative uses a iterative approach to grab the webpage contents.

-----------------------------------------------------------------------------------------------------------------------------------------

REQUIREMENTS:

The code is written in python. So you will need python.
This code uses the following python modules.
  1. Pandas
  2. BeautifulSoup
  3. re
  
In case if you do not have them, please install them first before executing the script.
