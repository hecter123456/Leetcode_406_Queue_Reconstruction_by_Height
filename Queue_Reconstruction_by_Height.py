import unittest
from operator import itemgetter

class unitest(unittest.TestCase):
    def testNull(self):
        people = []
        self.assertEqual(Solution().reconstructQueue(people),people);
    def testSameHeight(self):
        people = [[5,1],[5,0],[5,2]]
        ans = [[5,0],[5,1],[5,2]]
        self.assertEqual(Solution().reconstructQueue(people),ans);
class Solution():
    def reconstructQueue(self, people):
        if(people == []):
            return people
        return sorted(people, key=itemgetter(1))

if __name__ == '__main__':
    unittest.main()
