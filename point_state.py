"""
if you have 2 candidates and the following state points 
can you tell if there is a chance of a tie on an eleccion 
that both have the same points
state = ["Sunbroach", "Mindhaven", "CrystalFoot", "Mistscape"]
PointCount = [1,7,2,4]
output = True   

state = ["Sunbroach", "Mindhaven", "CrystalFoot", "Mistscape", "Emberpeak", "everbloom"]
PointCount = [1,9,3,4,3,2]
output = False

"""


def can_tie(points, states):
    sum_points = sum(points)

    if sum_points % 2 != 0:
        return False, []  # A tie is not possible

    half_points = sum_points // 2

    # Helper function to find the subset
    def helper(index, sum_point, chosen_states):
        if sum_point == 0:
            return True, chosen_states
        if index == len(points) or sum_point < 0:
            return False, []

        # Include the current state
        include, include_states = helper(index + 1, sum_point - points[index], chosen_states + [states[index]])
        if include:
            return True, include_states

        # Skip the current state
        skip, skip_states = helper(index + 1, sum_point, chosen_states)
        return skip, skip_states

    # Start the recursion
    return helper(0, half_points, [])

#states = ["Sunbroach", "Mindhaven", "CrystalFoot"]
#assert can_tie([1,9,1], states) == False
states = ["Sunbroach", "Mindhaven", "CrystalFoot"]
points = [1,9,1]
can_tie_bool, required_states = can_tie(points, states)
print(f"Can tie: {can_tie_bool}, States to win: {required_states}")
assert can_tie_bool == False
states = ["Sunbroach", "Mindhaven", "CrystalFoot", "Mistscape"]
points = [1, 7, 2, 4]
can_tie_bool, required_states = can_tie(points, states)
print(f"Can tie: {can_tie_bool}, States to win: {required_states}")
assert can_tie_bool == True
states = ["Sunbroach", "Mindhaven", "CrystalFoot", "Mistscape", "Emberpeak", "Everbloom"]
points = [1, 9, 3, 4, 3, 2]
can_tie_bool, required_states = can_tie(points, states)
print(f"Can tie: {can_tie_bool}, States to win: {required_states}")
assert can_tie_bool == True
print("all assertions passed")