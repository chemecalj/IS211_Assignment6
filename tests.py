#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Assignment 6, Part 1 Unit Test."""

import conversions
import conversions_refactored
import unittest


class TestCases(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        expected = 500
        returned = conversions.fahrenheit_to_celsius(932)
        self.assertEqual(returned, expected)
        expected = 490
        returned = conversions.fahrenheit_to_celsius(914)
        self.assertEqual(returned, expected)
        expected = 480
        returned = conversions.fahrenheit_to_celsius(896)
        self.assertEqual(returned, expected)
        expected = 470
        returned = conversions.fahrenheit_to_celsius(878)
        self.assertEqual(returned, expected)
        expected = 460
        returned = conversions.fahrenheit_to_celsius(860)
        self.assertEqual(returned, expected)

    def test_celsius_to_fahrenheit(self):
        expected = 914
        returned = conversions.celsius_to_fahrenheit(490)
        self.assertEqual(returned, expected)
        expected = 896
        returned = conversions.celsius_to_fahrenheit(480)
        self.assertEqual(returned, expected)
        expected = 878
        returned = conversions.celsius_to_fahrenheit(470)
        self.assertEqual(returned, expected)
        expected = 860
        returned = conversions.celsius_to_fahrenheit(460)
        self.assertEqual(returned, expected)
        expected = 842
        returned = conversions.celsius_to_fahrenheit(450)
        self.assertEqual(returned, expected)

    def test_celsius_to_kelvin(self):
        expected = 663.15
        returned = conversions.celsius_to_kelvin(390)
        self.assertEqual(returned, expected)
        expected = 653.15
        returned = conversions.celsius_to_kelvin(380)
        self.assertEqual(returned, expected)
        expected = 643.15
        returned = conversions.celsius_to_kelvin(370)
        self.assertEqual(returned, expected)
        expected = 633.15
        returned = conversions.celsius_to_kelvin(360)
        self.assertEqual(returned, expected)
        expected = 623.15
        returned = conversions.celsius_to_kelvin(350)
        self.assertEqual(returned, expected)

    def test_kelvin_to_celsius(self):
        expected = 440
        returned = conversions.kelvin_to_celsius(713.15)
        self.assertEqual(returned, expected)
        expected = 430
        returned = conversions.kelvin_to_celsius(703.15)
        self.assertEqual(returned, expected)
        expected = 420
        returned = conversions.kelvin_to_celsius(693.15)
        self.assertEqual(returned, expected)
        expected = 410
        returned = conversions.kelvin_to_celsius(683.15)
        self.assertEqual(returned, expected)
        expected = 400
        returned = conversions.kelvin_to_celsius(673.15)
        self.assertEqual(returned, expected)

    def test_fahrenheit_to_kelvin(self):
        expected = 723.15
        returned = conversions.fahrenheit_to_kelvin(842)
        self.assertEqual(returned, expected)
        expected = 713.15
        returned = conversions.fahrenheit_to_kelvin(824)
        self.assertEqual(returned, expected)
        expected = 703.15
        returned = conversions.fahrenheit_to_kelvin(806)
        self.assertEqual(returned, expected)
        expected = 693.15
        returned = conversions.fahrenheit_to_kelvin(788)
        self.assertEqual(returned, expected)
        expected = 683.15
        returned = conversions.fahrenheit_to_kelvin(770)
        self.assertEqual(returned, expected)

    def test_kelvin_to_fahrenheit(self):
        expected = 806
        returned = conversions.kelvin_to_fahrenheit(703.15)
        self.assertEqual(returned, expected)
        expected = 788
        returned = conversions.kelvin_to_fahrenheit(693.15)
        self.assertEqual(returned, expected)
        expected = 770
        returned = conversions.kelvin_to_fahrenheit(683.15)
        self.assertEqual(returned, expected)
        expected = 752
        returned = conversions.kelvin_to_fahrenheit(673.15)
        self.assertEqual(returned, expected)
        expected = 734
        returned = conversions.kelvin_to_fahrenheit(663.15)
        self.assertEqual(returned, expected)

    def tests_convert(self):
        expected = 623.15
        returned = conversions_refactored.convert('celsius', 'kelvin', 350)
        self.assertEqual(returned, expected)
        expected = 662
        returned = conversions_refactored.convert('celsius', 'fahrenheit', 350)
        self.assertEqual(returned, expected)
        expected = 160
        returned = conversions_refactored.convert('fahrenheit', 'celsius', 320)
        self.assertEqual(returned, expected)
        expected = 433.15
        returned = conversions_refactored.convert('fahrenheit', 'kelvin', 320)
        self.assertEqual(returned, expected)
        expected = 330
        returned = conversions_refactored.convert('kelvin', 'celsius', 603.15)
        self.assertEqual(returned, expected)
        expected = 626
        returned = conversions_refactored.convert('kelvin', 'fahrenheit', 603.15)
        self.assertEqual(returned, expected)
        expected = None
        returned = conversions_refactored.convert('kelvin', 'miles', 100)
        self.assertEqual(returned, expected)
        expected = "Please enter valid conversion units."
        returned = conversions_refactored.convert('meters', 'fahrenheit', 100)
        self.assertEqual(returned, expected)
        expected = None
        returned = conversions_refactored.convert('celsius', 'yards', 100)
        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()
