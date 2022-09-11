
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

## 🧪 Testing

The flask api is tested in both unit tests and functional tests using the [pytest](https://docs.pytest.org/en/7.1.x/contents.html) framework.

### Overview of the testing criteria

**Functional Tests:**

Tests the functionality of the api endpoint `/get-vehicle-info` which takes in an image as a parameter and return the vehicle model and price as a JSON object.

*Functional test modules:*

* `test_get_vehicle` -> Given a flask application, when the '/get-vehicle-info' is requested (POST), check that a '200' response code is returned with valid response data.

* `test_get_vehicle_without_image` -> Given a flask application, when the '/get-vehicle-info' is requested (POST) without an image attached in the body, then check that a '400' status code is returned.

* `test_get_vehicle_invalid_image_type` -> Given a flask application, when the '/get-vehicle-info' is requested (POST) with an invalid image type, then check that a '415' status code is returned. 

**Unit Tests:**

Tests the each individual functions used by the api, such as price retrieval, image recognition and image reshaping for the cnn model.

*Unit test modules:*

* `test_get_price` -> Given a name of vehicle, when trying to find the current market price, then check the return value is a string (*cannot check for an exact value since market value is not constant,therefore checking the return type is the only option available*).

* `test_predict` -> Given a path to an image of a vehicle, when trying to identify the vehicle, then check the identified vehicle is correct according to the given image.

* `test_reshape_image` -> Given a path to an image, when trying to predict the image, then check the returned image tensor is in correct shape.

**A code test coverage of 89% is achieved with the implementation of above test cases.**


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
## ⚗ Running Tests

*Prerequisites:*

* [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)
* [Coverage](https://coverage.readthedocs.io/en/6.4.4/#)

* Navigate to the root folder of the project and activate the python virtual environment created during the setup process.

**Step 01:**

* Install pytest and coverage.

```bash
    pip install pytest, coverage
```

**Step 02:**

* Run the test modules.

```bash
    coverage run --source=app -m pytest
```

**output:**

```
===================================================================== test session starts =====================================================================
platform win32 -- Python 3.9.5, pytest-7.1.2, pluggy-1.0.0
collected 6 items                                                                                                                                               

tests\functional\test_get_vehicle_info.py ...                                                                                                            [ 50%] 
tests\unit\test_get_price.py .                                                                                                                           [ 66%] 
tests\unit\test_predict.py .                                                                                                                             [ 83%] 
tests\unit\test_reshape_image.py .                                                                                                                       [100%] 

====================================================================== 6 passed in 7.74s ======================================================================
```

**Step 03:**

* Checking the test coverage report.

```bash
    coverage report
```

**output:**

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
## 🚀 Deployment (Google Cloud Platform)

The API developed in this project is deployed in Google Cloud Platform (GCP) to be accessed by the price finder mobile application. Furthermore, the deployment process is fully automated with the use of github actions CI/CD pipleline.


*Prerequisites:*

* [Google Cloud Platform (GCP)](https://cloud.google.com/) account.

📌 *Note: You have to activate the billing feauture of the account by providing your credit / debit card details and it will charge you 1-2 USD to verify your account, but that amount will be refunded and you will not have to turn on billing for the project itself and therefore, **you will not be charged** for the usage during this project and everything will be under the [free usage limits.](https://cloud.google.com/free/docs/free-cloud-features) Moreover, you will recieve **300 USD free credits** valid for 3 months.*

### Create new GCP project

**Step 01:**

* Go to the GCP console and create a new project (Make sure to give a unique relatable name for your service).

*Example:* `vehicle-price-finder-001`

📌 *Note: You will not be able to use the example above since every project has to have a unique name therefore, provide a unique name and keep it noted since it will be required in the steps below.*

**Step 02:**

Activate `Cloud Run` and `Cloud Build` API

* In the Google Cloud console, go to APIs & services for your project. 
* Click on the **Library page** and Search `Cloud Run` on the search box.
* Select the API and select **Enable**.
* Activate `Cloud Build` api with the same steps.


### Install Google Cloud CLI

**Step 01:**

Download and install Google Cloud CLI using this [guide](https://cloud.google.com/sdk/docs/install) by Google and complete the installing and initializing sections.

### Manual deployment to GCP

**Step 01:**

Build the docker filer in Cloud Build

`PROJECT-ID` -> Can be found in the project dashboard in Google Cloud console. Edit this value before executing the command below.

* Run the command below in a terminal in project root directory

```bash
    gcloud builds submit --tag gcr.io/{PROJECT-ID}/get-prediction
```

**Step 02:**

Deploying to Cloud Run

```bash
    gcloud run deploy --image gcr.io/{PROJECT-ID}/get-prediction --platform managed
```

* `Service name` -> Provide a service name for the api, use **get-prediction** for the current project.
* `region` -> Select a region based on your location with the help of this [documentation](https://cloud.google.com/run/docs/locations) for the current project i have used `asia-south1` [6].
*  `allow unauthenticated invocations` -> select 'y'

After successful deployment, the **Service URL** will be displayed at the bottom of the terminal. Copy that for future use since that will be the api access point.

### Deployment to GCP through Github Actions CI/CD pipleine

Before following the steps fork this repository to your own github account.

*Make sure to complete the sections mentioned below*

* [Create new GCP project](#create-new-gcp-project)
* [Install Google Cloud CLI](#install-google-cloud-cli)


**Step 01:**

Create a Google Cloud Service Account.

* Go to google cloud console
* Click navigation menu on top left corner.
* `IAM & Admin` -> `Service Accounts` -> `Create Service Account`
* Service Account Name: `api-service-account`

**Step 02:**

Grant the Google Cloud Service Account permissions mentioned below to access Google Cloud resources.


* `Cloud Run Admin`
* `Cloud Run Service Agent`
* `Cloud Build Service Agent`
* `Viewer`

**Step 03:**

Enable the IAM Credentials API.

```bash
    gcloud services enable iamcredentials.googleapis.com --project "{PROJECT-ID}"
```

**Step 04:**

Create a Workload Identity Pool.

Format:

```bash
gcloud iam workload-identity-pools create `"WORKLOAD-ID-POOL-NAME"` \
  --project=`"PROJECT_ID"` \
  --location="global" \
  --display-name=`"DISPLAY_NAME_FOR_POOL"`
```

Example:

```bash
    gcloud iam workload-identity-pools create "price-finder-pool" --project "{PROJECT-ID}" --location="global" --display-name="price finder pool"
```

**Step 05:**

Get the full ID of the Workload Identity Pool.

Format:

```bash
gcloud iam workload-identity-pools describe `"WORKLOAD-ID-POOL-NAME"` \
  --project=`"PROJECT_ID"` \
  --location="global" \
  --format="default"
```

Example:

```bash
    gcloud iam workload-identity-pools describe "price-finder-pool" --project "{PROJECT-ID}" --location="global" --format="default"
```

Return format:

```bash
    `WORKLOAD_IDENTITY_POOL_ID` = projects/`YOUR-PROJECT-NUMBER`/locations/global/workloadIdentityPools/`"WORKLOAD-ID-POOL-NAME"`
```

**Step 06:**

Create a Workload Identity Provider in that pool.

Format:

```bash
gcloud iam workload-identity-pools providers create-oidc `"WORKLOAD-ID-POOL-PROVIDER-NAME"` \
  --project=`"PROJECT_ID"` \
  --location="global" \
  --workload-identity-pool=`"WORKLOAD-ID-POOL-NAME"` \
  --display-name=`"DISPLAY_NAME_FOR_PROVIDER"` \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"
```

Example:

```bash
    gcloud iam workload-identity-pools providers create-oidc “price-finder-provider”  --project "{PROJECT-ID}" --location="global" --workload-identity-pool="price-finder-pool" --display-name="price finder provider" --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" --issuer-uri="https://token.actions.githubusercontent.com"
```

**Step 07:**

Allow authentications from the Workload Identity Provider originating from your repository to impersonate the Service Account created above.

Format:

```bash
gcloud iam service-accounts add-iam-policy-binding "my-service-account@${PROJECT_ID}.iam.gserviceaccount.com" \
  --project=`"PROJECT_ID"` \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/`WORKLOAD_IDENTITY_POOL_ID( RETURN VALUE FROM STEP 5)`/attribute.repository/`yourgithubname/reponame`"
```

Example:

```bash
    gcloud iam service-accounts add-iam-policy-binding "test-service-account@{PROJECT-ID}.iam.gserviceaccount.com" --project "{PROJECT-ID}" --role="roles/iam.workloadIdentityUser" --member="principalSet://iam.googleapis.com/`WORKLOAD_IDENTITY_POOL_ID( RETURN VALUE FROM STEP 5)`/attribute.repository/`yourgithubname/reponame`"
```

**Step 08:**

Extract the Workload Identity Provider resource name.

Format:

```bash 
gcloud iam workload-identity-pools providers describe "my-provider" \
  --project=`"PROJECT_ID"` \
  --location="global" \
  --workload-identity-pool=`"WORKLOAD-ID-POOL-NAME"` \
  --format="default"
```

Example:

```bash
    gcloud iam workload-identity-pools providers describe "price-finder-provider" --project="{PROJECT-ID}" --location="global" --workload-identity-pool=“price-finder-pool” --format="default"
```

Return format:

```bash 
    projects/`YOUR-PROJECT-NUMBER`/locations/global/workloadIdentityPools/`WORKLOAD-ID-POOL-NAME`/providers/`WORKLOAD-ID-POOL-PROVIDER-NAME`
```

⭕ **Important**

**YOU NEED TO USE THIS VALUE AS** "workload_identity_provider" in `main.yml` file, located in `.github\workflows` directory under **"Authenticate to Google Cloud"** section.

📌 *Note: When replacing the workload_identity_provider, remove the `$` and curly brackets. Just include the value within single quotes.*


**Step 09:**

Making the service public (Allow unauthenticated).

Format:

```bash
  gcloud run services add-iam-policy-binding [SERVICE_NAME] \
    --member="allUsers" \
    --role="roles/run.invoker" \
    --project=`"PROJECT_ID"`
```

`SERVICE_NAME` = Name of the cloud run service

Example:

```bash
    gcloud run services add-iam-policy-binding get-prediction --member="allUsers" --role="roles/run.invoker" --project="{PROJECT-ID}"
```

**Step 10:**

Update the `cloudbuild.yaml` file with current project details.

* Update the `PROJECT-ID` in the section below and replace the content in `cloudbuild.yaml` file in the project root directory.

```bash
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/{PROJECT-ID}/get-prediction', '.']
images: ['gcr.io/{PROJECT-ID}/get-prediction']
```

**Step 11:**

Update the `main.yml` file in `.github\workflows` 'directory.

* `PROJECT_ID` -> Replace with your own project id
* `REGION` -> If necessary, replace it with a region suitable for you or keep as it is.
* `service_account` -> Can be found under **IAM & Admin** > **Service accounts** (Example: my-service-account@my-project.iam.gserviceaccount.com)

📌 *Note: When replacing the service account, remove the `$` and curly brackets. Just include the value within single quotes.*


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