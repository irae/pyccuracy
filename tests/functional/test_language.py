# -*- coding: utf-8 -*-
import os
from nose.tools import raises, set_trace
from pyccuracy.languages import LanguageGetter

def test_pt_br_exists():
    lg = LanguageGetter('pt-br')
    assert os.path.exists(lg.language_path), "There is no language file for pt-br culture: %s" % lg.language_path

def test_en_us_exists():
    lg = LanguageGetter('en-us')
    assert os.path.exists(lg.language_path), "There is no language file for en-us culture: %s" % lg.language_path