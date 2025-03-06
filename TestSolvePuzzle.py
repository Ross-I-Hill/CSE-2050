import unittest

def solve_puzzle(L, index = 0, mem = None):
    if index == len(L) - 1:
        return True
    if mem is None:
        mem = []
    if index in mem:
        return False
    else:
        mem.append(index)
    idx_cw = (index+L[index]) % len(L)
    idx_ccw =(index-L[index]) % len(L)
    return solve_puzzle(L, idx_cw, mem) or solve_puzzle(L, idx_ccw, mem)
    

class Testsolve_puzzle(unittest.TestCase):
    def test_cw(self):
        L = [3, 6, 4, 1, 3, 4, 2, 0]
        self.assertEqual(solve_puzzle(L), True)

    def test_ccw(self):
        L = [2, 4, 3, 9, 1, 3, 1]
        self.assertEqual(solve_puzzle(L), True)

    def test_both(self):
        L = [3, 2, 4, 6, 4, 1, 2, 1]
        self.assertEqual(solve_puzzle(L), True)

    def test_unsolvable(self):
        L = [2, 5, 4, 2, 1]
        self.assertEqual(solve_puzzle(L), False)

    


if __name__ == "__main__":
    unittest.main()