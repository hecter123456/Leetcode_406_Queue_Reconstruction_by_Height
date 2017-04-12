import unittest

class unitest(unittest.TestCase):
    def testNull(self):
        people = []
        self.assertEqual(Solution().reconstructQueue(people),people);

class Solution():
    def reconstructQueue(self, people):
        if(people == []):
            return people

if __name__ == '__main__':
    unittest.main()
