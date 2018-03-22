import os, sys, random, unittest
import blinktest.csv_file_process
from blinktest.csv_file_process import CSVFileReader
from blinktest.masts import MastsRecord
from blinktest.ra_input import RawInputCommand
from datetime import datetime

class TestCSVFileReader(unittest.TestCase):

    def setUp(self):
        self.file= 'Mobile Phone Masts.csv'
        
        
    '''
	check whether the file exist
    '''
    def test_readfile(self):
        # make sure the file exists in the folder
        self.assertTrue(os.path.isfile(self.file),"{} File exists".format(True))
    '''
	failure case
    '''
    # def test_readfilefailure(self):
    #     # make sure the file exists in the folder
	# with self.assertRaises(SystemExit):
    #        CSVFileReader(None)

    '''
	Check the header list is matching
    '''
    def test_checkheaderlistmatching(self):
        # make sure the file exists in the folder
        expected_field = ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]', 'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date', 'Lease Years', 'Current Rent']
        csvfile = CSVFileReader(self.file)
        self.assertEqual(csvfile.get_headerlist(),expected_field)


class TestMastRecord(unittest.TestCase):
    def setUp(self):
        def set_date(value):
            try:
                return datetime.strptime(value,'%d %b %Y')
            except:
                return datetime.strptime(value,'%d %B %Y')
        self.unit_name='Queenswood Hgt-Telecom App.'
        self.tenant_name='Vodafone Ltd'
        self.current_rent=9500.00
        self.lease_start_date = set_date('08/Nov/2004')
        self.lease_end_date =set_date('07/Nov/2029')
        self.property_name='Queenswood Heights'
        self.lease_years=25
        self.property_address_1 ='Queenswood Heights'
        self.property_address__2 ='Queenswood Gardens'
        self.property_address_3 ='Headingley'
        self.property_address_4 ='Leeds'
   
    #TODO check the value are in expected format correct module etc.
    # assert(type(current_rent) == int)
    # assert(type(lease_end_date) == datetime)
    #
    #
    #
    #

	
     

class TestRawInputCommand(unittest.TestCase):
   #TODO
   pass

if __name__ == '__main__':
    unittest.main()
