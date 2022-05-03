
#from StringIO import StringIO
import csv
from datetime import datetime
from dateutil.parser import isoparse, parse as date_parse

class Ingest:
  
  def __init__(self, filename):
    cols = ["uid", "operation","uuid","date"]
    self.events = {}

    with open(filename, newline='', encoding='ascii') as file:
      reader = csv.DictReader(file, cols)
      for row in reader:
        print("UID: %s  DATE: %s" % (row['uid'],
                                     date_parse(row['date']).timestamp()
                                     ))
        exit

  def getCount(self, start, end):
      print("hello")
      exit


if __name__ == '__main__':
  ingest = Ingest('events.csv')
  ingest.getCount(1,100)
