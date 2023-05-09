Communication Contract: 

In order to request data from this microservice, the application must make an HTTP GET request to the local server, by default running on http:///localhost:5000/stock/SPY.
The server will then respond the data requested in JSON format.

In order to receive data from this microservice, the application must convert the JSON response format to a python dictionary wich can be done in the response body. 
After the requested JSON data has been stored in the variable "response", the application can then convert the JSON into a python dictionary via the command response.json(), and then store as desired.

Here is an example call of how the application can both request and receive data from this microservice.

// Python code for example request for stock DIA. First add requests in python built in library. Then request as follows. 
 
import requests

url = 'http://localhost:5000/stock/DIA'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code, response.text)

//

