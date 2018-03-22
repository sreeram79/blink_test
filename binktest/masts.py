import os,sys
from datetime import datetime

'''
masts_record class keep details for each item
'''
class MastsRecord:
  
    '''
       Initiliase Masts with given details
    '''
    def __init__(self):
        self.property_name = None
        self.property_address_1 = None
        self.property__address_2 = None
        self.property_address_3 = None
        self.property_address_4 = None
        self.unit_name = None
        self.tenant_name = None
        self.lease_start_date = None
        self.lease_end_date = None
        self.lease_years = None
        self.current_rent = None
    
    def set_date(self,item,value):
        try:
            date = datetime.strptime(value,'%d %b %Y')
        except:
            date =datetime.strptime(value,'%d %B %Y')
        
        setattr(self,item.lower().replace(' ','_'),date)

    def checkyear(current_year):
        try:
            current_yr = datetime.strptime(current_year,'%d %b %Y')
        except:
            current_yr =datetime.strptime(current_year,'%d %B %Y')
        ##TODO currently hardcoded but should be modifiable as a filter
        if (current_yr < datetime.strptime('31 Aug 2007','%d %b %Y') and 
            current_yr > datetime.strptime('1 June 1999','%d %B %Y')):
            return True
        return False

    ## TODO property settting not done

    ## TODO set the value as expected automatically here
        
    def __repr__(self):
        return ('\n Unit Name:{},\t  Tenant Name:{}, \t Current Rent:{}, \t Lease Start Date: {}, \tLease End Date: {}, \tLease Years {}, Property Name {},  Property Address[1]: {},  Property Address[2]: {}, Property Address[3]: {}, Property Address[4]: {}'\
         .format(self.unit_name,self.tenant_name,self.current_rent,
         self.lease_start_date.strftime('%d/%b/%Y'),
         self.lease_end_date.strftime('%d/%b/%Y'),self.lease_years,
         self.property_name,self.property_address_1,self.property__address_2,self.property_address_3,self.property_address_4))

  