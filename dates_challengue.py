import pytest
from datetime import date, timedelta 
from dateutil.relativedelta import relativedelta
import random

'''
1. Define how you want to represent your inputs and 
   outputs (ProgramConfig, Transfer).
2. Write a function that given a ProgramConfig, outputs 
   an array of Transfer as defined by the PaymentConfig.
'''
class ProgramConfig():
  def __init__(self, cadence, start_date, num_transfers, amount):
    self.cadence = cadence
    self.start_date = start_date
    self.num_transfers = num_transfers
    self.amount = amount

class Transfer():
  def __init__(self, scheduled_date_time, amount):
    self.scheduled_date_time = scheduled_date_time
    self.amount = amount
  
  def __str__(self):
    return f"scheduled_date_time: {self.scheduled_date_time}, amount: {self.amount}"
  
  def __eq__(self,other):
    if not isinstance(other, Transfer):
      return False
    return (self.scheduled_date_time == other.scheduled_date_time and self.amount == other.amount)
  
  def __repr__(self):
    return f"Transfer:({self.scheduled_date_time!r}, {self.amount:.2f})"

def generate_transfers(program_config):
  if not program_config:
    return None
  ret = []
  curr_date = program_config.start_date
  original_day = curr_date.day
  for i in range(program_config.num_transfers):
    transfer = Transfer(curr_date, program_config.amount)
    ret.append(transfer)
    if program_config.cadence == 'weekly':
      curr_date = curr_date + timedelta(weeks=1) 
    elif program_config.cadence == 'monthly':
      next_month = curr_date + relativedelta(months=1)
      last_day =(next_month + relativedelta(day=31)).day
      corrected_day = min(original_day, last_day)
      curr_date = next_month.replace(day=corrected_day)
    elif program_config.cadence == 'monthly_with_jitter':
      jitter = random.randint(-3,3)
      jittered_date = curr_date + timedelta(days=jitter)
      curr_date = jittered_date
    else:
      raise ValueError(f"Unknown cadence: {program_config.cadence}")
    #print(f"transfer: {transfer}")
  #print(f"Transfers: {ret}")
  return ret

'''
3. Write tests for your function. Please include testing 
for edge cases outside of the basic examples we have 
provided!
'''
program_config = ProgramConfig(cadence = "weekly", start_date = date(2024, 5, 30), num_transfers = 3, amount = 50.00)
#print(generate_transfers(program_config))
assert generate_transfers(program_config) == [
    Transfer(date(2024,5,30), 50.00), 
    Transfer(date(2024,6,6), 50.00), 
    Transfer(date(2024,6,13), 50.00)
    ]

program_config = ProgramConfig(cadence = "monthly", start_date = date(2024, 1, 25), num_transfers = 4, amount = 50.00)
assert generate_transfers(program_config) == [
    Transfer(date(2024,1,25), 50.00), 
    Transfer(date(2024,2,25), 50.00), 
    Transfer(date(2024,3,25), 50.00),
    Transfer(date(2024,4,25), 50.00)
    ]
#print(generate_transfers(program_config))

program_config = ProgramConfig(cadence = "monthly", start_date = date(2023, 1, 31), num_transfers = 4, amount = 50.00)
#print(generate_transfers(program_config))
assert generate_transfers(program_config) == [
    Transfer(date(2023,1,31), 50.00), 
    Transfer(date(2023,2,28), 50.00), 
    Transfer(date(2023,3,31), 50.00),
    Transfer(date(2023,4,30), 50.00)
    ]
assert generate_transfers(None) == None

program_config = ProgramConfig(cadence = "daily", start_date = date(2023, 1, 31), num_transfers = 4, amount = 50.00)
try:
  assert generate_transfers(program_config) == None
except ValueError as e:
  print(f"Exception: {e}")

program_config = ProgramConfig(cadence = "monthly_with_jitter", start_date = date(2024, 1, 5), num_transfers = 4, amount = 50.00)
print(generate_transfers(program_config))


print("all test passing")
"""
def test_example_pass():
  print("pass")
  assert 2 == 2


def test_example_fail():
  print("fail")
  assert 3 == 2
"""

pytest.main(["main.py"])