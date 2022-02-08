
"""Generates a list of historical event dates that may have had
significant impact on markets.  See extract_interesting_date_ranges."""

import pandas as pd

from collections import OrderedDict

PERIODS = OrderedDict()

PERIODS['2015 Bull-Crash'] = (pd.Timestamp('20150209'), pd.Timestamp('20151231'))

PERIODS['Circuit Break'] = (pd.Timestamp('20151101'), pd.Timestamp('20160222'))

PERIODS['50 Crash'] = (pd.Timestamp('20180101'), pd.Timestamp('20180401'))

PERIODS['Covid-19'] = (pd.Timestamp('20200101'), pd.Timestamp('20200501'))

PERIODS['2015'] = (pd.Timestamp('20150101'), pd.Timestamp('20151231'))
PERIODS['2016'] = (pd.Timestamp('20160101'), pd.Timestamp('20161231'))
PERIODS['2017'] = (pd.Timestamp('20170101'), pd.Timestamp('20171231'))
PERIODS['2018'] = (pd.Timestamp('20180101'), pd.Timestamp('20181231'))
PERIODS['2019'] = (pd.Timestamp('20190101'), pd.Timestamp('20191231'))
PERIODS['2020'] = (pd.Timestamp('20200101'), pd.Timestamp('20201231'))
PERIODS['2021'] = (pd.Timestamp('20210101'), pd.Timestamp('20211231'))
PERIODS['2022'] = (pd.Timestamp('20220101'), pd.Timestamp('20221231'))
