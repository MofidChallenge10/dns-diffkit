import unittest
from tool import normalize, compare
class DnsTests(unittest.TestCase):
    def test_normalize_deduplicates(self): self.assertEqual(normalize(["::1","127.0.0.1","::1"]),["127.0.0.1","::1"])
    def test_diff(self):
        result=compare(["1.1.1.1","2.2.2.2"],["1.1.1.1","3.3.3.3"])
        self.assertEqual(result,{"added":["3.3.3.3"],"removed":["2.2.2.2"],"unchanged":["1.1.1.1"]})
if __name__=="__main__": unittest.main()
