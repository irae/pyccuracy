import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class DivIsVisibleAction(ElementIsVisibleBase):
    def __init__(self, browser_driver, language):
        super(DivIsVisibleAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["div_is_visible_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        div_name = values[0]
        error_message = self.language["div_is_visible_failure"]
        self.execute_is_visible(context, Page.Div, div_name, error_message)