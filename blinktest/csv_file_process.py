import os, csv, sys,  math

class CSVFileReader:
    '''
       Initiliase the file using os path currently using the default folder which  can be improved here
    '''
    def __init__(self, file=None):
        self.file = file
        if file is None:
            sys.exit(-1)
    '''
       read the file, for the moment read everytime and using the data can be improved by caching
    '''
    def read_file(self):
        data = []
        with open(self.file, 'r') as f:
           try:
               data =[row for row in csv.DictReader(f, delimiter=',', quotechar='"')]   
           except csv.Error as e:
               sys.exit('file %s, line %d: %s' % (self.file, reader.line_num, e))
        return data
    '''
       Using this function to retrieve the row count as survey usage increases quite a lot we might 
       need to know what was the last input to calculate the probability
    '''
    def get_row_count(self):
        return len(self.read_file())
    '''
       incase of using the random sampling or various other sampling we might need to weight the column as well
       or may use it for future purposes
    '''
    def get_column_count(self):
        new_data = self.read_file()
        return len(new_data[0])
    '''
       Return the data by getting the number of rows required only this is quite basic
       TODO could be improved with various other options
    '''
    def get_data(self, rows=1):
        data = self.read_file()
        return data[:rows]
    '''
       Return the headerlist of the rows so that we can enhance for future use
    '''
    def get_headerlist(self,rows=1):
        header_list = self.get_data()
        return [item for item,value in header_list[0].items()]
    
    
