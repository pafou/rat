"""
Basic tests for RAT application.
"""

from django.test import TestCase

from rat.views import last_line


class BasicTests(TestCase):
    def test_last_line(self):
        """
        Check last line has no \n, is not None, and is a string.
        """

        blabla = ""
        self.assertIsNotNone(last_line(blabla)) 
        self.assertIsInstance(last_line(blabla),str)
        
        blabla = "Une ligne simple"
        self.assertEqual(last_line(blabla), "Une ligne simple")
        
        blabla = """allez les bleus
        et les verts"""
        self.assertEqual(last_line(blabla), "        et les verts")
        
        blabla = """
        derniere ligne non vide
        
        
"""
        self.assertEqual(last_line(blabla), "        derniere ligne non vide")
