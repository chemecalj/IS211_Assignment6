#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Assignment 6, Part 2 and 3 Conversion Functions."""


abso_diff = 273.15


def fahrenheit_to_celsius(degrees):
    return (degrees - 32) * 5 / 9

def celsius_to_fahrenheit(degrees):
    return (degrees * 1.8) + 32

def celsius_to_kelvin(degrees):
    return degrees + abso_diff

def kelvin_to_celsius(degrees):
    return degrees - abso_diff

def fahrenheit_to_kelvin(degrees):
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))

def kelvin_to_fahrenheit(degrees):
    return celsius_to_fahrenheit(kelvin_to_celsius(degrees))

def meters_to_yards(dist):
    return dist * 1.09361

def yards_to_meters(dist):
    return dist * 0.9144

def meters_to_miles(dist):
    return dist * 0.000621371

def miles_to_meters(dist):
    return dist * 1609.34

def yards_to_miles(dist):
    return dist * 0.000568182

def miles_to_yards(dist):
    return dist * 1760
