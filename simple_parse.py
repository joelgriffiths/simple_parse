import csv
from dateutil.parser import parse as date_parse
import numpy as np

class Ingest:
  
  def __init__(self, filename):

    # events[customer_id] = [event1_epoch, event2_epoch, ...]
    self.events = {}

    # Loading everything into memory since it's only 15M
    # Outside of the customer selection menu, this is the only loop
    # in the code. It's probably avoidable but I want to use epoch
    # timestamps, and no sub-seconds since it's easier to use those in a URL
    with open(filename, newline='', encoding='ascii') as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] not in self.events:
          self.events[row[0]] = [int(date_parse(row[3]).timestamp())]
        else:
          self.events[row[0]].append(int(date_parse(row[3]).timestamp()))

  #
  # Print a list of the customers found in the CSV file
  #
  # Returns: uid for chosen customer
  #
  def selectCustomers(self):
    customer_list = list(self.events.keys())
    for idx, customer in enumerate(customer_list):
      print(f"[{idx}] - {customer}")

    print('\nChoose Customer [exit]: ', end='')
    customer_idx = input()

    # Cheap way to exit on anything invalid
    try:
      return customer_list[int(customer_idx)]
    except (IndexError, ValueError):
        return ''

  #
  # Prompt for the minimum timestamp (defaults to lowest value)
  #
  # Returns: Epoch for first event
  #
  def getMin(self, customer_id):
    customer_events = self.events[customer_id]
    min_timestamp = min(customer_events)
    print(f"Choose minimum timestamp [{min_timestamp}]: ", end='')
    epoch_start = input()

    selected_timestamp = int(epoch_start) if epoch_start.isnumeric() else min_timestamp
    return selected_timestamp

  #
  # Same as above, but the maximum. Repeated for readability
  #
  # Returns: Epoch for last event
  #
  def getMax(self, customer_id):
    customer_events = self.events[customer_id]
    max_timestamp = max(customer_events)
    print(f"Choose maximum timestamp [{max_timestamp}]: ", end='')
    epoch_start = input()

    selected_timestamp = int(epoch_start) if epoch_start.isnumeric() else max_timestamp
    return selected_timestamp

  #
  # The point of the exercise. Let's do it without a loop
  #
  # Returns: Number of timestamps between the two timestamps
  #
  def getCount(self, customer, time1=0, time2=9999999999, inclusive=True):
    # Make timestamps absolute so order doesn't count
    start_time = time1 if time1 < time2 else time2
    end_time   = time2 if time2 > time1 else time1

    # Make a new array with the events between the two times
    customer_list = np.array(self.events[customer])
    if inclusive:
      matching_array = np.logical_and(customer_list >= start_time, customer_list <= end_time)
    else:
      matching_array = np.logical_and(customer_list > start_time, customer_list < end_time)

    final_array = np.where(matching_array)[0]

    # Return the length of the new sub-array
    return(len(final_array))

if __name__ == '__main__':
  ingest = Ingest('events.csv')
  
  customer = ingest.selectCustomers()
  while customer:
    print(f"Counting customer {customer}")
    min_ts = ingest.getMin(customer)
    max_ts = ingest.getMax(customer)

    customer_count = ingest.getCount(customer, min_ts, max_ts)
    print(f"\n-- Inclusively, there are {customer_count} records between {min_ts} and {max_ts} for {customer}")

    customer_count = ingest.getCount(customer, min_ts, max_ts, False)
    print(f"-- Exclusively, there are {customer_count} records between {min_ts} and {max_ts} for {customer}\n\n")
    
    # Prompt again. Exit on no selection or invalid selection
    customer = ingest.selectCustomers()
