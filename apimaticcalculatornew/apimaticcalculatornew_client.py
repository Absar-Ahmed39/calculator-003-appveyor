# -*- coding: utf-8 -*-

"""
    apimaticcalculatornew

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from apimaticcalculatornew.decorators import lazy_property
from apimaticcalculatornew.configuration import Configuration
from apimaticcalculatornew.controllers.simple_calculator_controller import SimpleCalculatorController


class ApimaticcalculatornewClient(object):

    config = Configuration

    @lazy_property
    def simple_calculator(self):
        return SimpleCalculatorController()


