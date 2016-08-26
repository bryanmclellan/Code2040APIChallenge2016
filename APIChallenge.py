import requests, httplib

myToken = 'd34c1c19c158b0ddd603f8637c3b32e2'

def connectToEndpoint():
    endpointURL = 'http://challenge.code2040.org/api/register'
    
    githubURL = 'https://github.com/bryanmclellan/Code2040APIChallenge2016/'
    r = requests.post(endpointURL, data = {'token': myToken, 'github': githubURL})

def step2():
    endpointURL = 'http://challenge.code2040.org/api/reverse'
    r = requests.post(endpointURL, data = {'token': myToken})
    reversed = r.text[::-1]
    validateURL = 'http://challenge.code2040.org/api/reverse/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'string': reversed})

def step3():
    endpointURL = 'http://challenge.code2040.org/api/haystack'
    r = requests.post(endpointURL, data = {'token': myToken})
    dict = r.json()
    needle = dict['needle']
    haystack = dict['haystack']
    index = haystack.index(needle)
    validateURL = 'http://challenge.code2040.org/api/haystack/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'needle': index})

def step4():
    endpointURL = 'http://challenge.code2040.org/api/prefix'
    req = requests.post(endpointURL, data = {'token': myToken})
    dict = req.json()
    prefix = dict['prefix']
    array = dict['array']
    myArray =  [a for a in array if a.find(prefix) != 0]
    validateURL = 'http://challenge.code2040.org/api/prefix/validate'
    r = requests.post(validateURL, json = {'token': myToken, 'array': myArray})





if __name__ == "__main__":
    step4()

