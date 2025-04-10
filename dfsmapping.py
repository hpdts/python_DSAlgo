from collections import defaultdict

# Question:
# You are given a list of dictionaries representing a mapping between models. Each dictionary contains the following keys:
#
# SEMModelMappingId: A unique identifier for the model mapping.
# parentModel: The parent model ID of the current model. If the value is 0, this model has no parent.
# subModel: The ID of the model that is being mapped to the parent.
#
# Your task is to implement a function model_mapping_search(data: List[Dict]) -> Dict[int, List[int]]
# that outputs a mapping of each SEMModelMappingId to a list of models starting from the root parent (where parentModel is 0) down to the given submodel.
# This should include all models in the hierarchy between the root and the submodel, capturing all intermediate parent models.

example_input_data = [
    {'SEMModelMappingId': 10015, 'parentModel': 0, 'subModel': 54609},
    {'SEMModelMappingId': 10016, 'parentModel': 54609, 'subModel': 54610},
    {'SEMModelMappingId': 10017, 'parentModel': 54610, 'subModel': 54611},
    {'SEMModelMappingId': 10018, 'parentModel': 54609, 'subModel': 54612},
    {'SEMModelMappingId': 10019, 'parentModel': 54611, 'subModel': 42250},
    {'SEMModelMappingId': 10020, 'parentModel': 54612, 'subModel': 36107}
]

                 #     {10015: [54609], 10016: [54609, 54610], 10017: [54609, 54610, 54611], 10018: [54609, 54612], 10019: [42250, 54609, 54610, 54611], 10020: [36107, 54609, 54612]})
                 # by level child fix that
           #      ret: [42250, 54611, 54610, 54609]
#ret: [54609, 54610, 54611, 42250]
example_output_data = {10015: [54609], 10016: [54609, 54610], 10017: [54609, 54610, 54611], 10018: [54609, 54612], 10019: [54609, 54610, 54611, 42250], 10020: [54609, 54612, 36107]}

#recursive DFS

#0
# 54609
# - 54610
# -- 54611
# --- 42250
# - 54612
# -- 36107


# 

# example_input_data_3 = [
#     {'SEMModelMappingId': 10015, 'parentModel': 0, 'subModel': 54609},
#     {'SEMModelMappingId': 10018, 'parentModel': 54609, 'subModel': 54612},
#     {'SEMModelMappingId': 10020, 'parentModel': 54612, 'subModel': 36107}
#10020: [54609, 54612, 36107]
# ]


# #0
# # 54609
# # - 54612
# # -- 36107

# go over the map by SEMModelMappingId call dfs(id)->list subModel. 
# 10020

#10020: [54609, 54612, 36107
def find_modelmapping_data(SEMModelMappingId)->dict:
    for data_dict in example_input_data:
        if data_dict['SEMModelMappingId'] == SEMModelMappingId:
            return data_dict

    #    # print(f"data_dict: {data_dict}")
    # #    for key, value in data_dict.items():
    #      #   print(f"key, value: {key}, {value}")
    #         if key == 'SEMModelMappingId' and value == SEMModelMappingId:
    #             return data_dict
    return None

def find_modelmapping_data_bysubmodel(subModel)->dict:
    for data_dict in example_input_data:
        if data_dict['subModel'] == subModel:
            return data_dict

    #    # print(f"data_dict: {data_dict}")
    # #    for key, value in data_dict.items():
    #      #   print(f"key, value: {key}, {value}")
    #         if key == 'SEMModelMappingId' and value == SEMModelMappingId:
    #             return data_dict
    return None


def dfs(curr_data):
    #print(f"curr_data: {curr_data}")
    if not curr_data:
        return
    if curr_data:
        ret.append(curr_data['subModel'])

    parent = curr_data['parentModel']
    if parent:
        parent_data = find_modelmapping_data_bysubmodel(parent)
        #print(f"parent_data: {parent_data}")
        dfs(parent_data)

#print(find_modelmapping_data(10020))
#assert find_modelmapping_data(10020) == "{'SEMModelMappingId': 10020, 'parentModel': 54612, 'subModel': 36107}"

retu = defaultdict(list)
for data in example_input_data:
    map_id = data['SEMModelMappingId']
    curr_data = find_modelmapping_data(map_id)
    ret = []
    dfs(curr_data)
    #print(f"ret: {ret}")
    ret.reverse()
    #print(f"ret: {ret}")

    #print(ret)
    retu[map_id] = ret

#print(retu)
assert retu == example_output_data, f"Test failed"
print("Test passed")
