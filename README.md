# Number Classification API

This project is a Flask-based API that classifies a given number based on various properties such as whether it is prime, perfect, Armstrong, odd, or even. It also provides a fun fact about the number if it is an Armstrong number. Accepts GET requests with a number parameter, returns JSON in the specified format, handles edge cases gracefully (non-numeric inputs, negative numbers, numbers with multiple properties), and provides appropriate HTTP status codes.


## Features

- Classifies a number as prime, perfect, Armstrong, odd, or even.
- Provides the sum of the digits of the number.
- Returns a fun fact if the number is an Armstrong number.

## Endpoints

### GET `/api/classify-number`

#### Query Parameters

- `number` (required): The number to classify.

#### Responses

##### 200 OK

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "class_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
##### 400 Bad Response

```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup
### 1. Clone the repository
```markdown
git clone https://github.com/LNCH92/Number-classification-API.git
cd your-repository
```
### 2. Create a virtual environment and activate it:
```markdown
python -m venv .venv
source .venv\Scripts\activate
```

### 3. Install the required packages:
```markdown
pip install -r requirements.txt
```

### 4. Run the Flask application
```markdown
python classify-api.py
```

### 5. Open your browser and navigate to the link below to test the endpoint.
``` markdown
http://127.0.0.1:5000/api/classify-number?number=371
```

## Dependencies
<<<<<<< HEAD
1. Flask
2. Flask-Marshmallow

## MIT License 
=======
 1. Flask
 2. Flask-Marshmallow

## MIT License

>>>>>>> 996b1707fb2aaad222015143cca96239563f2f96
