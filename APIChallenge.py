import requests, httplib, time, datetime
from datetime import timedelta

myToken = 'd34c1c19c158b0ddd603f8637c3b32e2' # same token for all API calls

def connectToEndpoint():
    endpointURL = 'http://challenge.code2040.org/api/register'
    githubURL = 'https://github.com/bryanmclellan/Code2040APIChallenge2016/'
    r = requests.post(endpointURL, data = {'token': myToken, 'github': githubURL})

def step2():
    endpointURL = 'http://challenge.code2040.org/api/reverse'
    r = requests.post(endpointURL, data = {'token': myToken})
    reversed = r.text[::-1] # actual reversing of the string
    validateURL = 'http://challenge.code2040.org/api/reverse/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'string': reversed})

def step3():
    endpointURL = 'http://challenge.code2040.org/api/haystack'
    r = requests.post(endpointURL, data = {'token': myToken})
    dict = r.json()
    needle = dict['needle']
    haystack = dict['haystack']
    index = haystack.index(needle) # gets the index to POST to API
    validateURL = 'http://challenge.code2040.org/api/haystack/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'needle': index})

def step4():
    endpointURL = 'http://challenge.code2040.org/api/prefix'
    req = requests.post(endpointURL, data = {'token': myToken})
    dict = req.json()
    prefix = dict['prefix']
    array = dict['array']
    myArray =  [a for a in array if a.find(prefix) != 0] # list comprehension for elements that don't have the prefix
    validateURL = 'http://challenge.code2040.org/api/prefix/validate'
    r = requests.post(validateURL, json = {'token': myToken, 'array': myArray})


def step5():
    endpointURL = 'http://challenge.code2040.org/api/dating'
    req = requests.post(endpointURL, data = {'token': myToken})
    dict = req.json()
    datestamp = dict['datestamp']
    interval = dict['interval']
    tuple_time = time.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ") # get ISO time in tuple format
    myDate = datetime.datetime(tuple_time[0], tuple_time[1], tuple_time[2], tuple_time[3], tuple_time[4], tuple_time[5])
    finalDate = (myDate + timedelta(seconds=interval)).isoformat() + 'Z' # add interval to datetime and add 'Z' for formatting
    validateURL = 'http://challenge.code2040.org/api/dating/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'datestamp': finalDate})


if __name__ == "__main__":
    step5()