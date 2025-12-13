"""
No recipient is paid more than they are owed??


Input: {a: 10, b: 10, c: 10, d: 10},  40

Input: {a: 10, b: 10, c: 10, d: 10},  30

evenly as possible 


2 12

13/2. whole dollars
6+7

5 people owe 30   110/2


{a: 1, b: 100} 90/2
a:1 b:89

{a: 1, b: 100, c:12} 90/2
a:1 b:77, c:12

like giving cards

divide by number of people

Input: {a: 50, b: 10, c: 10, d: 10},  40
give each 1 dollar: brute force

{a: 1, b: 3}. 5
a:0, b:2.  1

a:0, b:1.  1


"""
def distribute_answer(amount, recipients):
  # Your code here! MCD
  min_money_pay=1
  pay_off = {}
  pay_out = {}
  for key in recipients:
      pay_off[key] = 0
      pay_out[key] = False
  
  while any(not value for value in pay_out.values()) and amount:
    curr_paid = 0
    for person in recipients:
      person_debt = recipients[person] 
      #print(f"person: {person}, person_debt: {person_debt}, pay_off[person]: {pay_off[person]}")
      
      if person_debt != pay_off[person]:
        #print(f"curr_paid: {curr_paid}")
        pay_off[person]+= min_money_pay
        curr_paid+=min_money_pay
      else:
        pay_out[person] = True
    
    amount-= curr_paid 
    
  return pay_off

def distribute(amount, recipients):
  # Your code here! MCD
  min_money_pay=1
  pay_off = {}
  for key in recipients:
      pay_off[key] = 0

  
  while any(pay_off[key] < recipients[key] for key in recipients.keys()) and amount != 0:
    curr_paid = 0
    for person in recipients:
      person_debt = recipients[person]
      #print(f"person: {person}, person_debt: {person_debt}, pay_off[person]: {pay_off[person]}")
      
      if person_debt != pay_off[person]:
        #print(f"curr_paid: {curr_paid}")
        pay_off[person]+= min_money_pay
        amount-= min_money_pay
        curr_paid+=min_money_pay
    
    if curr_paid == 0:
      break
    #amount-= curr_paid
    
  return pay_off
#heap
#print
assert distribute(5,{"a": 1, "b": 3}) == {'a': 1, 'b': 3}
assert distribute(5,{"a": 1, "b": 8}) == {'a': 1, 'b': 4}
assert distribute(40,{"a": 10, "b": 10, "c": 10, "d": 10}) == {"a": 10, "b": 10, "c": 10, "d": 10}
#print(distribute(90,{"a": 1, "b": 100, "c": 12}))
assert distribute(90,{"a": 1, "b": 100, "c": 12}) == {"a": 1, "b": 77, "c": 12}
print("all assertions passed")