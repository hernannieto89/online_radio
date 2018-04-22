#!/usr/bin/python

import subprocess
import datetime

# init
r = subprocess.check_output("clementine 2> /dev/null &", shell=True)
r = subprocess.check_output("clementine -p", shell=True)
r = subprocess.check_output("clementine --volume 50", shell=True)

# check time


def is_time_range(start, end):
    """
    Ask if actual hour is within start - end range.
    :param start:
    :param end:
    :return: Boolean
    """
    now = datetime.datetime.now()
    now_time = now.time()
    start_time = datetime.time(start)
    end_time = datetime.time(end)

    if start_time < end_time:
        return now_time >= start_time and now_time <= end_time
    # Over midnight
    return now_time >= start_time or now_time <= end_time


def got_to_sleep():
    return is_time_range(2, 7)


def be_quiet():
    return is_time_range(7, 9) or is_time_range(23, 2)


def be_loud():
    return is_time_range(9, 23)


while True:

    if got_to_sleep():
        r = subprocess.check_output("clementine --volume 0", shell=True)
    elif be_quiet():
        r = subprocess.check_output("clementine --volume 50", shell=True)
    elif be_loud():
        r = subprocess.check_output("clementine --volume 100", shell=True)
