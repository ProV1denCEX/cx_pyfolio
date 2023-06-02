
"""Generates a list of historical event dates that may have had
significant impact on markets.  See extract_interesting_date_ranges."""

import pandas as pd

from collections import OrderedDict

PERIODS = OrderedDict()

PERIODS['2015 Bull-Crash'] = (pd.Timestamp('20150209'), pd.Timestamp('20151231'))

PERIODS['Covid-19'] = (pd.Timestamp('20200101'), pd.Timestamp('20200501'))

for i in range(pd.Timestamp.now().year - 7, pd.Timestamp.now().year + 1):
    PERIODS[str(i)] = (pd.Timestamp(f'{i}0101'), pd.Timestamp(f'{i}1231'))
