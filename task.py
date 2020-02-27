#!/usr/bin/env python
from datetime import datetime

def firstrun():
    return "success"


def circleArea(radius):
    return radius * radius * 3.14159


def firstLast(myList):
    return [myList[0], myList[-1]]


def dateDifference(firstDate, secondDate):
    return abs((datetime.strptime(firstDate, "%Y-%m-%d") - datetime.strptime(secondDate, "%Y-%m-%d")).days)
