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
    def reconstructQueue(self, people):
        if(people == []):
            return people
        people = sorted(people, key=itemgetter(1,0))
        dictionary = defaultdict(int);
        for person in people:
            checksum = 0
            for key,value in dictionary.items():
                if key >= person[0]:
                    checksum += value
            dictionary[person[0]] += 1
            if checksum != person[1]:
                people.remove(person)
                people.insert(person[1],person)
        return people

if __name__ == '__main__':
    unittest.main()
