from collections import defaultdict
LiveRampDataStoreBase = """data_store_segment_id,name,description,provider,price
1004765519,123Push > Consumer > Demographic > Senior Citizens > Age 65+,Individuals living in a household with 3 or more people.,123Push,0.75
1000846336,Alliant > Automotive > Auto - In Market New Vehicle,In-Market model for new vehicle,Alliant,2.75
1000846346,Alliant > Automotive > Auto - In Market for Insurance,In-Market model for auto insurance,Alliant,2.75
1000847476,Alliant > Automotive > Auto - In Market for Used Vehicle,In-Market model for used vehicle,Alliant,2.75
1000846216,Alliant > Demographic > Homeowner,Active multi-channel households who own their home,Alliant,2.0
1000845656,Alliant > Demographic > Age 25-29 years,Active multi-channel households with a person age 25-29 years old present in the HH.,Alliant,1.75
1000848136,Alliant > Demographic > Age 30-34 years,Active multi-channel households with a person age 30-34 years old present in the HH.,Alliant,1.75
1000845646,Alliant > Demographic > Age 35-39 years,Active multi-channel households with a person age 35-39 years old present in the HH.,Alliant,1.75
1000845646,Alliant > Demographic > Age 35-39 years,Active multi-channel households with a person age 35-39 years old present in the HH.,Alliant,1.75
1000848146,Alliant > Demographic > Age 40-44 years,Active multi-channel households with a person age 40-44 years old present in the HH.,Alliant,1.75"""


# data_store_segment_id,
# name,
# description,
# provider,
# price

# Alliant > 
#   Automotive > 
#     Auto - In Market New Vehicle
#     Auto - In Market for Insurance


"""

123Push > Consumer > Demographic > Senior Citizens > Age 65+,Individuals living in a household with 3 or more people

3 levels??
1000846336,Alliant > Automotive > Auto - In Market New Vehicle,In-Market model for new vehicle,Alliant,2.75
1000846346,Alliant > Automotive > Auto - In Market for Insurance,In-Market model for auto insurance,Alliant,2.75
1000847476,Alliant > Automotive > Auto - In Market for Used Vehicle,In-Market model for used vehicle,Alliant,2.75
1000846216,Alliant > Demographic > Homeowner,Active multi-channel households who own their home,Alliant,2.0

Alliant > Automotive > Auto - In Market New Vehicle

dict(dict)

Alliant
       Automotive. 
               Auto - In Market New Vehicle
               
            DFS
recursive


dict = 

Alliant = [Automotive, ]
DFS
"""

# 1. create a layered structure that would be easy for our UI engineer to present on the frontend. 
#print("Francisco")
#print(LiveRampDataStoreBase)

#hello

line = "Alliant > Automotive > Auto - In Market for Used Vehicle"

ui_levels = defaultdict(dict)

def add_levels_bad(s, ui_levels):
  items_stream = s.split(">")
  curr = ui_levels
  for item in items_stream:
   # curr = curr[item]
    if len(curr) == 0:
      ui_levels[item] = {}
      curr = curr[item]
      #print(ui_levels)
      #print(curr)
    else:
      #curr empty
      if not curr:
       # print(f"item: {item}, curr: {curr}")
        curr[item] = {}
        curr = curr[item] 
      else: 
        print(f"item: {item}, curr: {curr}")
        curr = curr[item]
        if item is not curr:
          curr[item] = {}
        else:
            curr = curr[item]
     # print(ui_levels)
  return ui_levels
  
def add_levels(s, ui_levels):
  line_items = s.split('>')
  curr = ui_levels

  for line_item in line_items:
    line_item = line_item.strip()
    #this also checks when is empty
    if line_item not in curr:
      curr[line_item] = {}
    curr = curr[line_item]

  return ui_levels
  


#print(add_levels(line, ui_levels))
#line = 'Alliant > Automotive > Auto - In Market for Insurance'
#print(add_levels(line, ui_levels))
    
        
def process(lines):
  single_lines = lines.split('\n')
  for single_line in single_lines[1:]:
    #print(single_line)
    single_line = single_line.split(',')
    #for elem in single_line:
    name = single_line[1].strip()
    #print(f"name: {name}")
    add_levels(name, ui_levels)

    

process(LiveRampDataStoreBase)
print(ui_levels)







