<center>
#CSV LIBRARY
###Software Specification and Design II <br/> Design Document

Joseph Mulray<br/>
SE 211 <br/>
Dr. Filippos Vokolos, Ph. D. <br/>
Febuary 5 2017<br/>
</center>


<br/>
<br/>
<br/>

##Table of Contents:
<br/>
<br/>
<strong>

1. Introduction <br/> 
1.1 Purpose <br/>
1.2 Scope of Document <br/>
1.3 Definitions, Acronyms, Abbreviations <br/>

2. System Overview <br/>
2.1 Description of Software <br/>
2.2 Technologies Used <br/>

3. Component Design <br/>
3.1 Overview <br/>
3.2 CSV <br/>
3.3 Attributes <br/>
3.4 Methods <br/>


4. References

</strong>
<br/>
<br/>
<br/>

	
##Introduction:

###1.1 Purpose:
The pupose of this document is to describe the implementation of csvlibary as described in the CSVLibrary Requirements document. CSV Library is designed to be a library to parse, read, and write csv files. The implimentation of this code is written in Python.


<br/>

###1.2 Scope of Document:
This document describes the implementation details of the CSVLibrary Software. The software will consists of a library that can be imported into a file or installed on a system or server. This document will not specify the testing of the software.


<br/>

###1.3 Definitions, Acronyms, Abbreviations <br/>
CSV: comma seperated value <br/>
Python: programming language used for implementation <br/>
List: python list (array), not linked list <br/>

<br/>
<br/>

##System Overview <br/>

###2.1 Description of Software <br/>
CSVLibrary is designed to be a library for python that allows users, to read, write, parse, and search comma seperated files. The CSVLibrary is a class object, that can be imported into any file or system. There can be several csv file objects at one time, allowing for multi-file functionality. There is no GUI for this specific library, each function will have a description along with its return type below.


<br/>

###2.2 Technologies Used <br/>
CSVLibrary uses csv files as input, or any file with separated values. Development of this library will run on any version of Python 2.7 and above. Development environment is using Unix and version control is handled through Git.

<br/>





<br/>
<br/>

##Component Design <br/>

###3.1 Overview
In this section, more details on each component are given. For each component, UML and a brief description are given.


###3.2 CSV
The CSV class is respooncible for reading, parsing, and writing to a given file. The class initializes and retains the following information, the file, the data from the file, the delimeter used to parse the data, and the position of the row current row. A user imports the csv library to their Python program and creates a csv object. The user can then call several of the predifined functions below.

</br>

<center>
![](images/csv_uml.png)
</center>

</br>

###3.3 Attributes
</br>
<center>

|  Name | Type  |  Description |
|:-:|---|---|
|  file | String  | Used to read and write to the contents of a file  |      
| data  |  Array[] | Used to retain all data from file, stored into an array  |      
|  delimeter | String  | Used to hold the delimeter, in case there is another value user wants to seperate file with  |
| position | Integer | Used to keep position of current row, used for next() method to return next row in the array    

</center>


<br/>
<br/>
<br/>

###3.4 Methods <br/>




<br/>
####Function: refresh
Refresh is used to reassign data, used when changing delimeter or changes made to a file and want a refresh of that data
		
```python
	def refresh(self):

#Input: Void 
#Output: Void
	
```

<br/>
<br/>
<br/>

####Function: setDelimeter
The purpose is to set comma seperated value to what
		ever input user wants by default set towards comma.
		
```python
	def setDelimeter(self, delimeter =','):
	
#Input: Takes in a delimeter, will then assign new delimeter 
#and refresh the data using new assigned delimeter.

#Output: Void


```


<br/>

####Function: search
Searches file for inputed value, return None if such value does not exist, if found returns coordinates in file.
		


```python

	def search(self, value):

"""	
Input: A value inputted by the user
Output: Returns a boolean if value was found or not, was found
returns true: otherwise returns false
"""	
```

<br/>

####Function: read
Read returns data from file inputted

```python
def read(self):

"""
Input: Void
Output: Returns a list with each  of each rows data
"""

```
<br/>
####Function: readAll
Reads all values from file, and returns a list of with no row segmentation



```python
	def readAll(self):

"""
Input: Void
Output: Array[] of all values from file, no row segmentation
"""
```


<br/>
####Function: write
Takes a value(s) inputed by user, and writes to the CSV file


```python
	def write(self, *argv):

"""
Input: Arguments inputted by the user
Output: Void
"""

```
<br/>
####Function: writeRow
Takes a list of values appends to a file

```python
	def writeRow(self, row):

"""
Input: list of values
Output: Void
"""
```

<br/>
####Function: ignoreEmpty
Function ignoreEmpty ignores empty cells following values of csv, dont return empty cells with no values, does not return any value
		
```python
	def ignoreEmpty(self):

"""
Input: Void
Output: Void
"""

```

<br/>
####Function: rmNLC
Removes trailing new line character from end of csv file

```python
	def rmNLC(self):
	
"""
Input: Void
Output: Void
"""
```
<br/>

####Function: next
Returns the next row from the csv file object, gets the current position and returns next value


```python
	def next(self):
	
"""
Input: Void
Output: List of the next row, other wise if no more values in the data, return None
"""
```
<br/>
<br/>
## 4. References

>"Software Requirements Specification." Wikipedia. Wikimedia Foundation, n.d. Web. 05 Feb. 2017.

<br/>
>"System Requirements Specification." Wikipedia. Wikimedia Foundation, n.d. Web. 05 Feb. 2017.

