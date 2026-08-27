# test_fluxgaze.py
"""
Tests for FluxGaze module.
"""

import unittest
from fluxgaze import FluxGaze

class TestFluxGaze(unittest.TestCase):
    """Test cases for FluxGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxGaze()
        self.assertIsInstance(instance, FluxGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
