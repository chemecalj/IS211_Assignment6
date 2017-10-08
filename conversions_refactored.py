#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Assignment 6, Part 4 Refactoring"""

import conversions

def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temp = ['celsius', 'fahrenheit', 'kelvin']
    dist = ['meters', 'miles', 'yards']
    tempfuncs = [conversions.celsius_to_fahrenheit(value), conversions.celsius_to_kelvin(value),
                 conversions.fahrenheit_to_celsius(value), conversions.fahrenheit_to_kelvin(value),
                 conversions.kelvin_to_celsius(value), conversions.kelvin_to_fahrenheit(value)]
    distfuncs = [conversions.meters_to_miles(value), conversions.meters_to_yards(value),
                 conversions.miles_to_meters(value), conversions.miles_to_yards(value),
                 conversions.yards_to_meters(value), conversions.yards_to_miles(value)]

    if fromUnit == toUnit:
        return value

    if fromUnit and toUnit in temp:
        if fromUnit == temp[0]:
            if toUnit == temp[1]:
                return tempfuncs[0]
            if toUnit == temp[2]:
                return tempfuncs[1]
        if fromUnit == temp[1]:
            if toUnit == temp[0]:
                return tempfuncs[2]
            if toUnit == temp[2]:
                return tempfuncs[3]
        if fromUnit == temp[2]:
            if toUnit == temp[0]:
                return tempfuncs[4]
            if toUnit == temp[1]:
                return tempfuncs[5]

    if fromUnit and toUnit in dist:
        if fromUnit == dist[0]:
            if toUnit == dist[1]:
                return distfuncs[0]
            if toUnit == dist[2]:
                return distfuncs[1]
        if fromUnit == dist[1]:
            if toUnit == dist[0]:
                return distfuncs[2]
            if toUnit == dist[2]:
                return distfuncs[3]
        if fromUnit == dist[2]:
            if toUnit == dist[0]:
                return distfuncs[4]
            if toUnit == dist[1]:
                return distfuncs[5]

    else:
        return "Please enter valid conversion units."
