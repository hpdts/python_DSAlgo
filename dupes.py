
def dedup(input: list[str])->list[str]:
    uniques = set()
    res = []

    for item in input:

        if item not in uniques:
            uniques.add(item)
            res.append(item)
        else:
            print(f"Duplicate: {item}")
    
    return res
    
def dedup_dicts(input: list[dict])->list[dict]:
    uniques = set()
    res = []

    for item in input:
        print(f"item.items(): {item.items()}")
        item_tuple = tuple(sorted(item.items()))  # Convert dictionary to a tuple of sorted items
        print(f"item_tuple: {item_tuple}")
        if item_tuple not in uniques:
            uniques.add(item_tuple)
            res.append(item)
        else:
            print(f"Duplicate: {item}")
    
    return res

def test_dedup():
    assert dedup(["one", "two", "two", "three"]) == ["one", "two", "three"]
    assert dedup(["ten", "two", "two", "three"]) == ["ten", "two", "three"]
    assert dedup(["one", "one", "one", "one"]) == ["one"]

def test_dedup_dicts():
    dict1 = {"name":"one", "age":1}
    dict2 = {"age":1, "name":"one"}
    print(dedup_dicts([dict1, dict2]))
    assert dedup_dicts([dict1, dict2]) == [dict1]

#print(dedup(["one", "two", "two", "three"]))
test_dedup()
test_dedup_dicts()