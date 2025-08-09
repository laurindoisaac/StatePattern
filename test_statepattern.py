# test_statepattern.py
"""
Tests for StatePattern module.
"""

import unittest
from statepattern import StatePattern

class TestStatePattern(unittest.TestCase):
    """Test cases for StatePattern class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StatePattern()
        self.assertIsInstance(instance, StatePattern)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StatePattern()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
