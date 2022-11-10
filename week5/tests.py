import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_other_player(self):
        player = 'X'
        self.assertEqual(logic.other_player(player), 'O')

    def test_check_line(self):
        player = None
        adj1 = 'O'
        adj2 = 'X'
        self.assertEqual(logic.check_line(player,adj1, adj2), 'D')

    # TODO: Test all the other functions from logic.py!


if __name__ == '__main__':
    unittest.main()
