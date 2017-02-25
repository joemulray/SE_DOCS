<center>
#CSV LIBRARY
###Software Requirements Document

Joseph Mulray<br/>
SE 211 <br/>
Dr. Filippos Vokolos, Ph. D. <br/>
Febuary 5 2017<br/>
</center>

<strong>
<br/>
<br/>

##Table of Contents:
<br/>
<br/>

1. Introduction <br/> 
1.1 Purpose <br/>
1.2 Scope of Document <br/>
1.3 Definitions, Acronyms, Abbreviations <br/>
1.4 References

2. Overall Description<br/>
2.1 Product Perspective<br/> 
2.2 Product Features<br/> 
2.3 Operating Environment<br/> 

3. Specific Requirements<br/> 
3.1 Functional Requirements<br/> 
3.2 Non-Functional Requirements<br/> 
3.3 Hardware Requirements<br/> 


</strong>

<br/>
<br/>

##Introduction:

###1.1 Purpose
The purpose of this document is to specify all the requirements for an CSVLibrary system. These requirements satisfy the performance, capabilities, constraints, system interface, and application structure for a given system.

<br/> 


###1.2 Project Scope
CSVLibrary is a csv editor that allows users to read, write, edit csv file documents. The benefits of this is fast efficient means of edditing csv files. This allows users to efficiently pull and push data to their comma seperated files. Its main objective is to reduce time and energy that a User would spend edditing a file and bring new features not offered in your traditional standard librarys.

<br/>

###1.3 Definitions, Acronyms, Abbreviations <br/>
CSV: comma seperated value <br/>
Python: programming language used for implementation <br/>
List: python list (array), not linked list <br/>

<br/>

###1.4 References

>"Software Requirements Specification." Wikipedia. Wikimedia Foundation, n.d. Web. 05 Feb. 2017.
<br/>

>"System Requirements Specification." Wikipedia. Wikimedia Foundation, n.d. Web. 05 Feb. 2017.

<br/>
<br/>


##2. Overall Description

###2.1 Product Overview
CSVLibrary software brings a friendly csv library to anyone using Python as their implimentation method. With a created file, a user can simply import the csvlibrary and use all of the defined functions simplifying and increasing performance of a system.

<br/>

###2.2 Product Features

refresh: Refresh is used to reassign data, used when changing delimeter or changes made to a file and want a refresh of that data <br/>

setDelimeter: The purpose is to set comma seperated value to what ever input user wants by default set towards comma. <br/>

search: Searches file for inputed value, return None if such value does not exist, if found returns coordinates in file. <br/>

read: Read returns data from file inputted <br/>

readAll: Reads all values from file, and returns a list of with no row segmentation <br/>

write: Takes a value(s) inputed by user, and writes to the CSV file <br/>

writeRow: Takes a list of values appends to a file<br/>

ignoreEmpty: Function ignoreEmpty ignores empty cells following values of csv, dont return empty cells with no values, does not return any value <br/>

rmNLC: Removes trailing new line character from end of csv file <br/>

next: Returns the next row from the csv file object, gets the current position and returns next value <br/>

<br/>

###2.3 Operating Environment

The CSVLibrary does not have a graphical user interface. The environment can only be imported to an existing Python application or file. From there the 2.2 application features will be accessible. CSVLibrary can improve on any application that does writing or parsing through files. 

<br/>


* The application will be tested and be fully functional and compatible with Python applications 2.7 and up. <br/>

* Any of the computers can function as web servers for integration testing.
* Source code control will be managed using "Git".
* Problem and issue tracking will be managed using Atlassian Jira.

<br/>
<br/>

##Specific Requirements
###3.1 Functional Requirements
* User can have any amount of csv objects
* CSVLibrary will run on any operating system
* Run on any application Python 2.7 and above

<br/>


###3.2 Non-Functional Requirements
* User ability to set a different delimeter other than comma seperated value
* System must reliably handle errors for a given circumstance.
*  Ability to reliably write to files, without altering data if error occurs.


<br/>
###3.3  Hardware Requirements
Any application running Python2.7 and above. Reguardless of operating system, csvlib will work on any operating system.


