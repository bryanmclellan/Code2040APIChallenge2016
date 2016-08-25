import sys
import requests

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)


if __name__ == "__main__":
    connectToEndpoint();

def connectToEndpoint():
    endpointURL = 'http://challenge.code2040.org/api/register'
    myToken = 'd34c1c19c158b0ddd603f8637c3b32e2'
    r = requests.post(endpointURL, data = {token: myToken, })