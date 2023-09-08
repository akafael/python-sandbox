"""
Peek-a-book game
 * count_time > 0 -> "Time Over!"
 * count_time == 0 -> "peek--BOO!"
 * count_time > 0 -> "peek" + N times "a" + "BOO!"

Script used as example for manual test coverage evaluation with BRANCH and LOOP
"""

import unittest

def peekaboo(count_time: int) -> str:

    if(count_time < 0):
        return("time over!")
    else:
        msg = "peek-"
        for i in range(0,count_time):
            msg += f"a"

        msg += "-BOO!"
        return msg


class TestPeekaboo(unittest.TestCase):
    
    def test_timeover(self):
        """
        Test it will return 'time over!' for a negative number input
        """
        self.assertEqual(peekaboo(-1),"time over!")
        
    def test_shorttime(self):
        """
        Test it will return 'peek--BOO!' for a input == 0
        """
        self.assertEqual(peekaboo(0),"peek--BOO!")

    def test_longtime(self):
        """
        Test it will return 'peek-a-BOO!' with N times 'a' for a positive input
        """
        count_time = 5
        msg = peekaboo(5)

        self.assertEqual(msg,"peek-aaaaa-BOO!")
        self.assertEqual(msg.count('a'), count_time)

    def test_generictime(self):
        """
        Test using generic expression considering a positive value for {count_time}
        """
        count_time = 7
        msg = peekaboo(5)

        expectedMsg = "peek-" + "a"*(count_time) + "-BOO!"
        self.assertEqual(msg,expectedMsg)
        self.assertEqual(msg.count('a'), count_time)
        
        
if __name__ == '__main__':
    unittest.main()