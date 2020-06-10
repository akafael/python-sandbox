"""
Challenge from first interview
"""

import re


def calc_bill_value(S):
    '''
    Calculate the Bill value for a fiction phone call register list
    Length call, phone Number in the format "HH:MM:SS,000-000-000\n"
    Conditions
        1. time less then 5 min : cost 3 cents/s
        2. time greater then 5 min : cost 150 cents/min
        3. all the calls from the number longest call time overall are free
    :param S:
    :return:
    '''

    bill_value = 0

    # Convert Data to (hour,minute,second,phone_number)
    SPLIT_BILL_PARAMETERS = r'([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9])'
    data = re.findall(SPLIT_BILL_PARAMETERS, S)

    ddata = {}
    # Store Phone with longest call time
    phone_longestcall = ""
    time_maxcalls = 0
    # Get Duration
    for item in data:
        # Convert Time to s
        time_seconds = int(item[0]) * 3600 + int(item[1]) * 60 + int(item[2])

        # Add Time to phone number register
        if item[3] not in ddata:
            ddata[item[3]] = time_seconds
        else:
            ddata[item[3]] += time_seconds

        # Get Longest Call time
        if ddata[item[3]] > time_maxcalls:
            phone_longestcall = item[3]
            time_maxcalls = ddata[item[3]]
        # elif ddata[item[3]] == time_maxcalls:
        #     # Check smallest Number in case of tier if the right number is needed to show up in the bill
        #     if item[3] < phone_longestcall:
        #         phone_longestcall = item[3]
        #         time_maxcalls = ddata[item[3]]

    # Remove Longest Call time (dont check smallest tier number since the value it dont change de value)
    del (ddata[phone_longestcall])

    # Generate Bill
    for phone_number, time in ddata.items():
        price_call = 0
        if time < 300:
            price_call = time * 3
        else:
            price_call = (time // 60 + 1) * 150

        bill_value += price_call

    # Return
    return bill_value
