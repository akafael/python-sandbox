'''
Challenge from past interview
'''
import re

def calc_bill_value(S):
    '''
    Calculate the Bill value for a fictions phone call register list
    Length call, phone Number in the format "HH:MM:SS,000-000-000\n"
    Conditions
        1. time less then 5 min : cost 3 cents/s
        2. time greater then 5 min : cost 150 cents/min
        3. all the calls from the number longest call time overall are free
    :param S:
    :return:
    '''

    value = 0

    # Convert Data to (hour,minute,second,phonenumber)
    regexpdata = r'([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9])'
    data = re.findall(regexpdata, S)

    ddata = {}
    # Store Phone with longest call time
    phonemaxcalls = ""
    timemaxcalls = 0
    # Get Duration
    for item in data:
        # Convert Time to s
        timeSeconds = int(item[0]) * 3600 + int(item[1]) * 60 + int(item[2])

        # Add Time to phonenumber register
        if item[3] not in ddata:
            ddata[item[3]] = timeSeconds
        else:
            ddata[item[3]] += timeSeconds

        # Get Longest Call time
        if ddata[item[3]] > timemaxcalls:
            phonemaxcalls = item[3]
            timemaxcalls = ddata[item[3]]
        # elif ddata[item[3]] == timemaxcalls:
        #     # Check smallest Number in case of tier if the right number is needed to show up in the bill
        #     if item[3] < phonemaxcalls:
        #         phonemaxcalls = item[3]
        #         timemaxcalls = ddata[item[3]]

    # Remove Longest Call time (dont check smallest tier number since the value it dont change de value)
    del (ddata[phonemaxcalls])

    # Generate Bill
    for phonenumber, time in ddata.items():
        pricecall = 0
        if time < 300:
            pricecall = time * 3
        else:
            pricecall = (time // 60 + 1) * 150

        value += pricecall

    # Return
    return value