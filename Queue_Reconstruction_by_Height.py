import unittest
from operator import itemgetter
from collections import defaultdict

class unitest(unittest.TestCase):
    def testNull(self):
        people = []
        self.assertEqual(Solution().reconstructQueue(people),people);
    def testSameHeight(self):
        people = [[5,1],[5,0],[5,2]]
        ans = [[5,0],[5,1],[5,2]]
        self.assertEqual(Solution().reconstructQueue(people),ans);
    def testRandomList(self):
        people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        ans = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        self.assertEqual(Solution().reconstructQueue(people),ans);
class Solution():
    def my_key(self,people):
        return -people[0],people[1]
    def reconstructQueue(self, people):
        if(people == []):
            return people
        people.sort(key=Solution().my_key)
        answer = []
        for person in people:
            answer.insert(person[1],person)
        return answer

if __name__ == '__main__':
    unittest.main()
