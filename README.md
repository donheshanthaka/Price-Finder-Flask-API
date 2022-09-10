
# Price Finder API

This project contains the Price Finder API developed and deployed to Google Cloud Platform (GCP) which facilitates the image recognition capabilities through a [vehicle image classification (CNN) model](https://github.com/donheshanthaka/Price-Finder-Deep-Learning-Model) and market price retrieval of the [Price Finder](https://github.com/donheshanthaka/Price-Finder-Flutter-APP) mobile application.
## 🧱 Tech Stack

| Framework / Library   | Functionality                                       |
|-----------------------|-----------------------------------------------------|
| Flask - 2.1           | Develop the API functionality                       |
| Tensorflow - 2.9      | Run the image recognition model                     |
| Requests - 4.11       | Retrieve current listings of the identified vehicle |
| Beautiful Soup - 4.11 | Retrieve the current market price                   |

## ⚙ Setup Instructions

**Clone the repository**

* Navigate to a folder in which you would like to setup the project.
* Open up a terminal in that folder and enter the command below to clone the repository.

```bash
  git clone https://github.com/donheshanthaka/Price-Finder-Flask-API.git
```

### 🐍 Setup the python virtual environment

**Step 01:**

* Navigate to the `Price-Finder-Flask-API` folder in terminal using the command below.

```bash
  cd Price-Finder-Flask-API
```

**Step 02:**

* Create the python virtual environment

```bash
    python -m venv env
```

**Step 03:**

* Navigate to the activation path

```bash
 cd env/Scripts
```

* Activate the virtual environment. *(Run either one, not both)*

```bash
  activate.bat //In CMD
  Activate.ps1 //In Powershell
```

**Step 04:**

* Move back to the project folder

```bash
  cd ../../
```

* Install the required dependencies



```bash
  pip install -r requirements.txt
```
## 🖥 Run Locally

**Setup environment variables**

* Setup flask app

```bash
  set FLASK_APP=main.py 
```

* Setup flask environment *(development is used since the app would be running locally)*

```bash
  set FLASK_ENV=development 
```

📌 To change the environment type : `set FLASK_ENV=development/production` use either `development` or `production`.

**Start the local server**

```bash
  flask run --host=192.168.1.100 --port=8000 
```

* `--host=192.168.1.100` > The server listens to requests on the given IP address
* `--port=8000` > The server will listen on port 8000
## 📡 Usage / Examples

*Prerequisites:*
* [cURL](https://curl.se/)

📌 *Note: If you have Windows 10 version 1803 or later, cURL is installed by default*


The current version of the api supports indentifying vehicle models and retrieving their current market price which can be accessed through a single end point. An example of that is given below.

**Getting vehicle information**

* Making a post request uisng `cURL` to the api endpoint `/get-vehicle-info` with an image attached to the body of the request.
* Use the command below in a terminal on the project root directory.

📍 **Make sure the local server is running before running the command below**

```cURL
  curl -L -X POST "http://192.168.1.100:8000/get-vehicle-info" -F imageFile=@tests/images/4.jpeg
```

* A JSON response will be returned with the identified model of the vehicle and it's current market value.


**Response:**

```bash
  {"model":"Toyota Aqua 2014", "price":"RS. 6,754,400"}
```

📌 *Note: The "Price" value returned in the response will vary since it is retrieved everytime from the web when the api is being called.*

**The same endpoint as above accessed using a python script:**

* Run this script on the project root folder.

```python
import requests

url = "http://192.168.1.100:8000/get-vehicle-info"

payload={}
files=[
  ('imageFile',('4.jpeg',open('tests/images/4.jpeg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

## 🧪 Running Tests

The flask api is tested in both unit tests and functional tests using the [pytest](https://docs.pytest.org/en/7.1.x/contents.html) framework.

### Overview of the testing criteria

**Functional Tests:**

Tests the functionality of the api endpoint `/get-vehicle-info` which takes in an image as a parameter and return the vehicle model and price as a JSON object.

*Functional test modules:*

`test_get_vehicle`: Given a flask application, when the '/get-vehicle-info' is requested (POST), check that a '200' response code is returned with valid response data.

`test_get_vehicle_without_image`: Given a flask application, when the '/get-vehicle-info' is requested (POST) without an image attached in the body, then check that a '400' status code is returned.

`test_get_vehicle_invalid_image_type` Given a flask application, when the '/get-vehicle-info' is requested (POST) with an invalid image type, then check that a '415' status code is returned. 

```
Name                    Stmts   Miss  Cover
-------------------------------------------
app\__init__.py            13      3    77%
app\error_handlers.py      22      2    91%
app\utils.py               40      6    85%
app\views.py               26      0   100%
-------------------------------------------
TOTAL                     101     11    89%

```
## Deployment (Google Cloud Platform)
## Response Codes
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Changelog