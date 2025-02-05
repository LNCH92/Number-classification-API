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


#### 400 Bad Response

```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python classify-api.py
```

### 5. Open your browser and navigate to htttp://127.0.0.1:5000/api/classify-number?number=371 to test the endpoint


## Dependencies
### - Flask
### - Flask-marshmallow

## MIT License
#### Copyright (c) 2025 Louis Chinenye Njoku 

#### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

#### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
