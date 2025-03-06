import unittest
def trib(k):
    '''Calls helper function to find the K value of the Tribonacci sequence'''
    return _trib(k, cashe = {0:0, 1:0, 2:0, 3:1})

def _trib(k, cashe):
    '''Helper function that uses the three previous numbers of the sequence to sum to the newest number of the sequence'''
    if k not in cashe:
        cashe[k] = _trib(k-1, cashe) + _trib(k-2, cashe) + _trib(k-3, cashe) 
    return cashe[k]

class Testtrib(unittest.TestCase):
    '''Tests the first ten numbers of the Tribonacci sequence to check if true'''
    def test_firstten(self):
        solutions = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 4, 7: 7, 8: 13, 9: 24, 10: 44}

        for k in solutions:
            self.assertEqual(trib(k), solutions[k])

    def test_100(self):
        '''Checks to see if the function returns the correct value for the 100th number'''
        self.assertEqual(trib(100), 28992087708416717612934417)

if __name__ == '__main__':
    unittest.main()

