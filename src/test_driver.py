import unittest
import pygame
import driver


class TestDriver(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.game = driver.game_loop()
        pygame.init()

    def tearDown(self):
        pygame.quit()
        unittest.TestCase.tearDown(self)

    def test_phrase(self):

        self.elftest = driver.elf_phrase("test input")
        self.assertEqual(self.elftest, driver.user_display("test diff"))


if __name__ == '__main__':
    unittest.main()