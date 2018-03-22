import os,sys
import operator
import copy
from datetime import datetime

class RawInputCommand:
    '''
       Initiliase still_true as false because this will be instantiated every time when a new question is asked
    '''
    def __init__(self):
        self.still_true =False
        
    '''
       Rum command function below gets the output in console based on the choice
    '''
    def process_data(self,masts_list,input_command):
        def checkyear(current_year):
            # try:
            #     current_yr = datetime.strptime(current_year,'%d %b %Y')
            # except:
            #     current_yr =datetime.strptime(current_year,'%d %B %Y')
            if (current_year < datetime.strptime('31 Aug 2007','%d %b %Y') and 
                current_year > datetime.strptime('1 June 1999','%d %B %Y')):
                return True
            return False
        if input_command == 1:
            print('\n'.join([str(x) for x in sorted(masts_list,key=operator.attrgetter('current_rent'))[:5]]))
        elif input_command == 2:
            new_mast_list = []
            for mast in masts_list:
                if mast.lease_years == 25:
                    new_mast_list.append(copy.deepcopy(mast))
            print('\n'.join([str(x) for x in new_mast_list]))
        elif input_command == 3:
            tenant_count = dict()
            for mast in masts_list:
                if mast.tenant_name in tenant_count.keys():
                    tenant_count[mast.tenant_name] = tenant_count[mast.tenant_name] + 1
                else:
                    tenant_count[mast.tenant_name] = 1
            for x,y in tenant_count.items():
                print('Tenant Name {} : Count:{} '.format(x,y))
        elif input_command == 4:
            year_list =  [mastrecord for mastrecord in masts_list if checkyear(mastrecord.lease_start_date)]
            print('\n'.join([str(mastrecord) for mastrecord in year_list]))
        
        
    def run_command(self,masts_list):
       while not self.still_true:
           print ('+'*100)
           print ('+'*100)
           print ("Given Requirements: Select the option from below")
           print ('1. List first 5 items sorted by Current Rent in ascending order.')
           print ('2. List of all mast data with Lease Years = 25 years')
           print ('3. Dictionary containing tenant name and a count of masts for each tenant')
           print ('4.List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007')
           number = int(input("select your choice by entering 1 or 2 or 3 or 4 or 5 only: "))
           print ('+'*100)
           print ('+'*100)
           if type(number)==int and number != 5:
               self.still_true = False
               self.process_data(masts_list,number)
           else:
               self.still_true = True
           
       
