import unittest
from view.button import Button
from view import config

class ButtonTest(unittest.TestCase):
    def testAction(self):
        self.assertTrue(Button.click[0] ==1)



