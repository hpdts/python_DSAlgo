'''
Campaign tickets

Scenario: A social media company is running an “Engage to Win” campaign. 
Each qualifying action (new post, payment, comment) earns the member one campaign ticket. 
Each disqualifying action like fraud flags, or action retractions should remove a single ticket. 
At any point, the system should be able to randomly draw a winner, where each member’s chance 
of being selected is proportional to their number of tickets. For example, a member with 5 tickets 
should be five times more likely to win than a member with 1 ticket. 
All operations should run in O(1) average time.

Examples
Add A, A, B, B, B, C then draw many times: P(B) ≈ 3/6, P(A) ≈ 2/6, P(C) ≈ 1/6.

Remove from B once, probabilities update to 2/5, 2/5, 1/5.

Removing a non-existent member returns false and does nothing.

Drawing from an empty campaign returns null or throws as specified.


new post, payment, comment
+1 txt
-1

O(1)

A 

freq map a,2 b, 3 C




Random
probabilistics model

P(B) ≈ 3/6, P(A) ≈ 2/6, P(C) ≈ 1/6.
0.5.           0.3.           0.1

                       r 0.2. O(N)


heap max    P(B)


we dont care about on the space complexity

dsta strcuture to pick a random ticket

A=0
B=1
C=3

0 1 2
2,3,1

P(B) ≈ 3/6, P(A) ≈ 2/6, P(C) ≈ 1/6.


 0 1.  2. 3. 4. 5
[A, A, B, B, B, C] 

O(1)
append()

map
ticket, set()

b,  2,3,4



set
B2

stack 

remove O(1)

total_tickets
num=rand(len(arr))
0

1..6
0 or 1 problem

winner whoever is closer to random num
map to a number




'''
import random
from typing import Protocol, Optional
from collections import defaultdict
class CampaignTickets(Protocol):
    def __init__(self):
        """Initializes the data structure."""
        self.campaign_tickets = []
        self.member_set_indexes = defaultdict(set)
        

    def add_ticket(self, member_id: str) -> None:
        """Adds a ticket for member_id."""
        index_member = len(self.campaign_tickets)
        self.campaign_tickets.append(member_id)
        self.member_set_indexes[member_id].add(index_member)

        
    def remove_ticket(self, member_id: str) -> bool:
        """
        Removes a single ticket for member_id if present.
        Returns True if a ticket was removed, False if member_id had none.
        """
        if member_id not in self.member_set_indexes:
            return False

        remove_index = self.member_set_indexes[member_id].pop()
        last_index = len(self.campaign_tickets)-1
        last_member = self.campaign_tickets[last_index]

        if remove_index != last_index:
            self.campaign_tickets[remove_index] = last_member
            self.member_set_indexes[last_member].remove(last_index)
            self.member_set_indexes[last_member].add(remove_index)

        # member at the end
        self.campaign_tickets.pop()
        if not self.member_set_indexes[member_id]:
            del self.member_set_indexes[member_id]

        return True


        
    def draw_random(self) -> Optional[str]:
        """
        Returns a random member_id, weighted by ticket count.
        Returns None if empty.
        """
        if not self.campaign_tickets:
            return None
            
        return random.choice(self.campaign_tickets)


campaign_tickets = CampaignTickets()
campaign_tickets.add_ticket('A')

def basic_test():
    ct = CampaignTickets()

    # Add tickets
    ct.add_ticket('A')
    ct.add_ticket('A')
    ct.add_ticket('B')
    ct.add_ticket('B')
    ct.add_ticket('B')
    ct.add_ticket('C')

    assert len(ct.campaign_tickets) == 6

    # Remove one B
    assert ct.remove_ticket('B') is True
    assert len(ct.campaign_tickets) == 5

    # Remove non-existent
    assert ct.remove_ticket('D') is False

    # Draw should return valid member
    for _ in range(10):
        winner = ct.draw_random()
        assert winner in {'A', 'B', 'C'}

    print("✅ Basic test passed!")

def edge_cases_test():
    ct = CampaignTickets()

    # Empty draw
    assert ct.draw_random() is None

    # Remove from empty
    assert ct.remove_ticket('A') is False

    # Add and remove all
    ct.add_ticket('A')
    ct.remove_ticket('A')

    assert ct.draw_random() is None

    print("✅ Edge cases test passed!")

basic_test()
edge_cases_test()