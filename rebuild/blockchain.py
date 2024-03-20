"""
"""
import datetime
import hashlib
import unittest

class Node:
    def __init__(self, data, previous_hash, next):
        self.data = data
        self.t = datetime.datetime.now()
        self.next = next
        self.previous_hash = previous_hash

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.data) + repr(self.previous_hash) + "\n"
        if self.next:
            ret += self.next.__repr__(level + 1)
        return ret
    
    def isValid(self):
        p = self
        while p.next is not None:
            if calculate_hash(p) != p.next.previous_hash:
                return False
            p = p.next
        return True



def calculate_hash(n: Node):
    x = str(n.t) + str(n.data) + str(n.previous_hash)
    return hashlib.sha256(x.encode()).hexdigest()

class Test(unittest.TestCase):
    def test(self):
        b = Node("data 1", 0, None)
        b.next = Node("data 2", calculate_hash(b), None )
        p = b.next
        p.next = Node("data 3", calculate_hash(p), None)
        p = p.next
        p.next = Node("data 4", calculate_hash(p), None)
        p = p.next

        # tamering the data should make it unvalid
        self.assertEqual(b.isValid(), True)
        b.data = "tampered data"        
        self.assertEqual(b.isValid(), False)
        # cleanup
        b.data = "data 1"        
        self.assertEqual(b.isValid(), True)

        # tampering the data of one block and the previous hash field of the other block
        # this should still be detected
        b.data = "tampered data"
        b.next.previous_hash = calculate_hash(b)
        self.assertEqual(b.isValid(), False)
        # cleanup
        b.data = "data 1"
        b.next.previous_hash = calculate_hash(b)
        self.assertEqual(b.isValid(), True)


        # tampering all data in all blocks is the only way to tamper data
        b.data = "tampered data"
        b.next.data = "tampered data 2"
        b.next.previous_hash = calculate_hash(b)
        b.next.next.data = "tampered data 3"
        b.next.next.previous_hash = calculate_hash(b.next)
        b.next.next.next.data = "tampered data 4"
        b.next.next.next.previous_hash = calculate_hash(b.next.next)
        self.assertEqual(b.isValid(), True)



if __name__ == "__main__":
    unittest.main()


