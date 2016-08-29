import requests, httplib, time, datetime, unittest
from datetime import timedelta

myToken = 'd34c1c19c158b0ddd603f8637c3b32e2' # same token for all API calls

# step 1 is to just connect to the endpoint with my token
def step1():
    endpointURL = 'http://challenge.code2040.org/api/register'
    githubURL = 'https://github.com/bryanmclellan/Code2040APIChallenge2016/'
    r = requests.post(endpointURL, data = {'token': myToken, 'github': githubURL})
    print r.text
    return r.text

# step 2 is to reverse a given string
def step2():
    endpointURL = 'http://challenge.code2040.org/api/reverse'
    r = requests.post(endpointURL, data = {'token': myToken})
    reversed = r.text[::-1] # actual reversing of the string
    validateURL = 'http://challenge.code2040.org/api/reverse/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'string': reversed})
    print r.text
    return r.text

# step 3 is to return the index of a value in a given array
def step3():
    dict = getJsonResponse('http://challenge.code2040.org/api/haystack')
    needle = dict['needle']
    haystack = dict['haystack']
    index = haystack.index(needle) # gets the index to POST to API
    validateURL = 'http://challenge.code2040.org/api/haystack/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'needle': index})
    print r.text
    return r.text

# step 4 is to filter an array into values that do not begin with a certain prefix
def step4():
    dict = getJsonResponse('http://challenge.code2040.org/api/prefix')
    prefix = dict['prefix']
    array = dict['array']
    myArray =  [a for a in array if a.find(prefix) != 0] # list comprehension for elements that don't have the prefix
    validateURL = 'http://challenge.code2040.org/api/prefix/validate'
    r = requests.post(validateURL, json = {'token': myToken, 'array': myArray})
    print r.text
    return r.text

# step 5 is to add an interval of seconds to a given ISO time
def step5():
    dict = getJsonResponse('http://challenge.code2040.org/api/dating')
    datestamp = dict['datestamp']
    interval = dict['interval']
    tuple_time = time.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ") # get ISO time in tuple format
    myDate = datetime.datetime(tuple_time[0], tuple_time[1], tuple_time[2], tuple_time[3], tuple_time[4], tuple_time[5])
    finalDate = (myDate + timedelta(seconds=interval)).isoformat() + 'Z' # add interval to datetime and add 'Z' for formatting
    validateURL = 'http://challenge.code2040.org/api/dating/validate'
    r = requests.post(validateURL, data = {'token': myToken, 'datestamp': finalDate}) 
    print r.text
    return r.text

# helper function to get json response from a POST request to an endpoint url
def getJsonResponse(endpointURL):
    req = requests.post(endpointURL, data = {'token': myToken})
    return req.json()


# tests for each function
class TestAPIChallenge(unittest.TestCase):

    def test_step1(self):
        self.assertEqual("Step 1 complete", step1())

    def test_step2(self):
        self.assertEqual("Step 2 complete", step2())   

    def test_step3(self):
        self.assertEqual("Step 3 complete", step3()) 

    def test_step4(self):
        self.assertEqual("Step 4 complete", step4())

    def test_step5(self):
        self.assertEqual("Step 5 complete", step5())


if __name__ == "__main__":
    unittest.main()
