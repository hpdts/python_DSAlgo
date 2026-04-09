from collections import defaultdict


class SilentTracker():
    def __init__(self):
        self.tracker = defaultdict(int)
        
    def allocate(self, hostType):
        if hostType in self.tracker:
            prev_val = self.tracker[hostType]
            prev_val += 1
            self.tracker[hostType] = prev_val
        else:
            self.tracker[hostType] = 1
            
        return hostType + str(self.tracker[hostType])
        
    def deallocate(self, hostname):
        hostType = "".join(letter for letter in hostname if letter.isalpha())
        if hostType in self.tracker:
            prev_val = self.tracker[hostType]
            prev_val -= 1
            if prev_val == 0:
                del self.tracker[hostType]
            else:
                self.tracker[hostType] = prev_val
        
        return None


"""

rest ad api 1 api 2 dellocate 
and get api 1 again
allocate
 api:1
 
 api: 2
 
to dellocate decrement and if is 0 you remove the key

"""

tracker = SilentTracker()

assert tracker.allocate("api") == "api1"
assert tracker.allocate("api") == "api2"

assert tracker.deallocate("api1") == None

assert tracker.allocate("api") == "api1"  # ❌ EXPECT: api1, ACTUAL: api2

assert tracker.allocate("db") ==  "db1"
assert tracker.allocate("db") == "db2"
assert tracker.allocate("db") == "db3"

tracker.deallocate("db2") == None

assert tracker.allocate("db") == "db2"  # ❌ EXPECT: db2, ACTUAL: db3