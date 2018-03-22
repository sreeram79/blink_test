import os, sys, traceback
from blinktest.csv_file_process import CSVFileReader
from blinktest.masts import MastsRecord
from blinktest.ra_input import RawInputCommand

def main():
    
    try:
        filename = 'Mobile Phone Masts.csv'
        csvfile = CSVFileReader(filename)
        header_list=csvfile.get_headerlist()
        print(header_list)
        MastsRecordlist = []
        for iter in csvfile.get_data(csvfile.get_row_count()):
            mastrecord = MastsRecord()
            for item,value in iter.items():
               if item in 'Current Rent':
                   setattr(mastrecord,item.lower().replace(' ','_'),float(value))
               elif (item in 'Lease Start Date' or item in 'Lease End Date'):
                    mastrecord.set_date(item,value)
               elif (item in 'Lease Years'):
                   setattr(mastrecord,item.lower().replace(' ','_'),int(value))
               else:
                   if value is None:
                       value = ''
                   setattr(mastrecord,item.lower().replace(' ','_').replace('[','').replace(']',''),value)
                   

            MastsRecordlist.append(mastrecord)
        ra = RawInputCommand()
        ra.run_command(MastsRecordlist)
        
    except KeyboardInterrupt:
        print ("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    finally:
	#TODO how to handle the exception cases which is not currently handled. I should have recalculated the probability as well
	#the logic incase of failure case should be completely different as well.
        sys.exit(0)

if __name__ == "__main__":
    main()

