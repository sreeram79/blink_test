#Introduction:-
This is a short project and has done with minimal prototype for the given requirement. 
	a) #CSVFileReader class in csv_file_process.py:
			CSVFileReader class helps in reading the given sample file and extract the data into the dictionary.
	b) #MastRecord Class
			MastRecord class helps in holding and computing the values for the given requirements.
	c) #RawInputCommand Class
			RawInputCommand class helps to loop on the requiremnts and gather the inputs from the users and displays the expected results. 

#What can you expect:
	Hooray !!! Quite happy to say that the very simple things work ;-)
	a) Reads the sampling file and convert into a objects.
	b) Selection of choices are given to be selected for each requirements to be displayed 
	c) OOPS, DRY principle are used whereever possible in a pythonic way.
	
#What could have been better:
       Well !!!! lot of things but within the expected time frame I couldnt do much.;-(
	a) Improve exception handling.
	d) Unable to do boundary testings. 
	e) Common definitions are missing.
	f) No filter are set to take new input and provide the expected as required.


Improvements:
	a) Computing on Sampling values algorithm must be improved for stastical purpose.
	b) Cardinality of the objects on sampling data would improve the robustness and scalability for the mast record if given object is stored better according to the real functionality requirement.
	c) Stated with BDD or TDD implementation for the given problem but discontinued.
	

Test Cases:
	a) CSVFilereader class
	b) MastRecord Class
	c) missing TODO RawInputCommand


Instructions to install, configure, and to run the programs


Install python 3,6

Configure using github clone command:
		----> main.py
		----> testsuite.py
		----> Readme.txt
		----> Mobile Phone Masts.csv
		----> blinktest
			  ------> __init__.py
			  ------> masts.py
			  ------> csv_file_process.py
			  ------> ra_input.py
			 -------> commondef.py
			 -------> metric_stats.py

Run:
	python main.py  ---> to run the simple flow
	python testsuite.py  --> to run the simple test


