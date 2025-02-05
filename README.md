# Number Classification API

This project is a Flask-based API that classifies a given number based on various properties such as whether it is prime, perfect, Armstrong, odd, or even. It also provides a fun fact about the number if it is an Armstrong number.

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
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
### 2. Create a virtual environment and activate it:
```markdown
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the required packages:
```markdown
pip install -r requirements.txt
```

### 4. Run the Flask application
```markdown
python classify-api.py
```

### 5. Open your browser and navigate to http://127.0.0.1:5000/api/classify-number?number=371 to test the endpoint.


## Dependencies
### 1. Flask
### 2. Flask-Marshmallow

## MIT License

# Number Classification API

This project is a Flask-based API that classifies a given number based on various properties such as whether it is prime, perfect, Armstrong, odd, or even. It also provides a fun fact about the number if it is an Armstrong number.

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
#### 400 Bad Response

```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup
### 1. Clone the repository
```markdown
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
### 2. Create a virtual environment and activate it:
```markdown
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the required packages:
```markdown
pip install -r requirements.txt
```

### 4. Run the Flask application
```markdown
python classify-api.py
```

### 5. Open your browser and navigate to http://127.0.0.1:5000/api/classify-number?number=371 to test the endpoint.


## Dependencies
### 1. Flask
### 2. Flask-Marshmallow

## MIT License