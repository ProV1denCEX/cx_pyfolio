import pandas as pd


APPROX_BDAYS_PER_MONTH = 21
APPROX_BDAYS_PER_YEAR = 252
MIN_5_PER_YEAR = APPROX_BDAYS_PER_YEAR * 48
MIN_1_PER_YEAR = APPROX_BDAYS_PER_YEAR * 240
MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52
QTRS_PER_YEAR = 4

MIN_1 = '1min'
MIN_5 = '5min'
DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'
YEARLY = 'yearly'

ANNUALIZATION_FACTORS = {
    MIN_5: MIN_5_PER_YEAR,
    DAILY: APPROX_BDAYS_PER_YEAR,
    WEEKLY: WEEKS_PER_YEAR,
    MONTHLY: MONTHS_PER_YEAR,
    QUARTERLY: QTRS_PER_YEAR,
    YEARLY: 1
}


def infer_freq(freq):
    if freq == pd.Timedelta(5, unit='min'):
        return MIN_5_PER_YEAR

    elif freq == pd.Timedelta(1, unit='min'):
        return MIN_1_PER_YEAR

    elif freq == pd.Timedelta(1, unit='day'):
        return APPROX_BDAYS_PER_YEAR
