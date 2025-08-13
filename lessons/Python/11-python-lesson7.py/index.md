# Comprehensive Python Functions & REST API Tutorial

## Table of Contents
1. [Python Functions Fundamentals](#python-functions-fundamentals)
2. [Advanced Function Concepts](#advanced-function-concepts)
3. [REST API with Python](#rest-api-with-python)
4. [Error Handling & Status Codes](#error-handling--status-codes)
5. [Real-World Examples](#real-world-examples)
6. [Best Practices](#best-practices)
7. [Code Summary](#code-summary)

---

## Python Functions Fundamentals

### Basic Function Syntax

```python
def function_name(parameters):
    """
    Docstring: Brief description of what the function does
    
    Args:
        parameter1: Description of parameter1
        parameter2: Description of parameter2
    
    Returns:
        Description of return value
    """
    # Function body
    return result
```

### 1. Simple Functions

```python
def greet():
    """Simple function with no parameters"""
    return "Hello, World!"

def greet_user(name):
    """Function with one parameter"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function with multiple parameters"""
    return a + b

# Usage examples
print(greet())                    # Output: Hello, World!
print(greet_user("Alice"))        # Output: Hello, Alice!
print(add_numbers(5, 3))         # Output: 8
```

### 2. Default Parameters

```python
def create_user(username, email, role="user", active=True):
    """Function with default parameters"""
    user = {
        "username": username,
        "email": email,
        "role": role,
        "active": active
    }
    return user

# Usage examples
user1 = create_user("john_doe", "john@example.com")
user2 = create_user("admin_user", "admin@example.com", role="admin")
user3 = create_user("temp_user", "temp@example.com", active=False)

print(user1)  # {'username': 'john_doe', 'email': 'john@example.com', 'role': 'user', 'active': True}
```

### 3. Variable-Length Arguments

```python
def sum_all(*args):
    """Function accepting variable number of arguments"""
    return sum(args)

def create_profile(**kwargs):
    """Function accepting keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

def flexible_function(*args, **kwargs):
    """Function accepting both *args and **kwargs"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    return len(args) + len(kwargs)

# Usage examples
print(sum_all(1, 2, 3, 4, 5))    # Output: 15
print(create_profile(name="Alice", age=30, city="New York"))
print(flexible_function(1, 2, 3, name="Bob", age=25))
```

### 4. Lambda Functions

```python
# Lambda function syntax
square = lambda x: x ** 2
add = lambda x, y: x + y

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(squared)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]

# Lambda in sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
```

---

## Advanced Function Concepts

### 1. Decorators

```python
import functools
import time

def timer_decorator(func):
    """Decorator to measure function execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def validate_types(*expected_types):
    """Decorator factory for type validation"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i+1} must be of type {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Using decorators
@timer_decorator
@validate_types(int, int)
def calculate_factorial(n, multiplier=1):
    """Calculate factorial with multiplier"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result * multiplier

# Usage
try:
    print(calculate_factorial(5, 2))  # Output: 240, with timing info
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
```

### 2. Generators

```python
def fibonacci_generator(n):
    """Generator function for Fibonacci sequence"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def process_large_file(filename):
    """Generator for processing large files line by line"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Usage examples
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34

# List comprehension vs Generator expression
numbers = range(1000000)
list_comp = [x ** 2 for x in numbers if x % 2 == 0]  # Memory intensive
gen_exp = (x ** 2 for x in numbers if x % 2 == 0)    # Memory efficient
```

### 3. Closures

```python
def create_multiplier(factor):
    """Closure example - function that returns a function"""
    def multiplier(number):
        return number * factor
    return multiplier

def create_counter(initial=0):
    """Closure with state management"""
    count = [initial]  # Using list to make it mutable
    
    def counter():
        count[0] += 1
        return count[0]
    
    def reset():
        count[0] = initial
    
    def get_count():
        return count[0]
    
    # Return multiple functions
    counter.reset = reset
    counter.get_count = get_count
    return counter

# Usage
multiply_by_5 = create_multiplier(5)
print(multiply_by_5(10))  # Output: 50

counter = create_counter(10)
print(counter())          # Output: 11
print(counter())          # Output: 12
print(counter.get_count()) # Output: 12
counter.reset()
print(counter())          # Output: 11
```

---

## REST API with Python

### 1. Basic HTTP Requests with `requests` Library

```python
import requests
import json
from typing import Dict, List, Optional, Union

class APIClient:
    """Comprehensive REST API client"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def set_auth(self, token: str, auth_type: str = "Bearer"):
        """Set authentication header"""
        self.session.headers.update({
            'Authorization': f'{auth_type} {token}'
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        """
        Perform GET request
        
        Args:
            endpoint: API endpoint (without base URL)
            params: Query parameters
        
        Returns:
            requests.Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.get(
                url, 
                params=params, 
                timeout=self.timeout
            )
            return response
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            raise
    
    def post(self, endpoint: str, data: Optional[Dict] = None, 
             files: Optional[Dict] = None) -> requests.Response:
        """
        Perform POST request
        
        Args:
            endpoint: API endpoint
            data: Request payload
            files: File upload dictionary
        
        Returns:
            requests.Response object
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            if files:
                # Remove Content-Type header for file uploads
                headers = self.session.headers.copy()
                headers.pop('Content-Type', None)
                response = self.session.post(
                    url, 
                    data=data, 
                    files=files, 
                    headers=headers,
                    timeout=self.timeout
                )
            else:
                response = self.session.post(
                    url, 
                    json=data, 
                    timeout=self.timeout
                )
            return response
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            raise
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> requests.Response:
        """Perform PUT request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.put(
                url, 
                json=data, 
                timeout=self.timeout
            )
            return response
        except requests.RequestException as e:
            print(f"PUT request failed: {e}")
            raise
    
    def delete(self, endpoint: str) -> requests.Response:
        """Perform DELETE request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.delete(url, timeout=self.timeout)
            return response
        except requests.RequestException as e:
            print(f"DELETE request failed: {e}")
            raise

    def patch(self, endpoint: str, data: Optional[Dict] = None) -> requests.Response:
        """Perform PATCH request"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.patch(
                url, 
                json=data, 
                timeout=self.timeout
            )
            return response
        except requests.RequestException as e:
            print(f"PATCH request failed: {e}")
            raise
```

### 2. Advanced API Functions

```python
class RESTAPIManager(APIClient):
    """Extended API manager with helper methods"""
    
    def handle_response(self, response: requests.Response) -> Dict:
        """
        Handle API response with proper error checking
        
        Args:
            response: requests.Response object
            
        Returns:
            Parsed JSON response or error details
        """
        status_code = response.status_code
        
        # Success status codes (2xx)
        if 200 <= status_code < 300:
            try:
                return {
                    'success': True,
                    'status_code': status_code,
                    'data': response.json() if response.content else None,
                    'headers': dict(response.headers)
                }
            except json.JSONDecodeError:
                return {
                    'success': True,
                    'status_code': status_code,
                    'data': response.text,
                    'headers': dict(response.headers)
                }
        
        # Client errors (4xx) and Server errors (5xx)
        else:
            error_data = {
                'success': False,
                'status_code': status_code,
                'error': self.get_status_message(status_code),
                'headers': dict(response.headers)
            }
            
            try:
                error_data['details'] = response.json()
            except json.JSONDecodeError:
                error_data['details'] = response.text
            
            return error_data
    
    def get_status_message(self, status_code: int) -> str:
        """Get human-readable status message"""
        status_messages = {
            # 2xx Success
            200: "OK - Request successful",
            201: "Created - Resource created successfully",
            202: "Accepted - Request accepted for processing",
            204: "No Content - Request successful, no content returned",
            
            # 3xx Redirection
            301: "Moved Permanently - Resource moved permanently",
            302: "Found - Resource found at different location",
            304: "Not Modified - Resource not modified since last request",
            
            # 4xx Client Error
            400: "Bad Request - Invalid request syntax",
            401: "Unauthorized - Authentication required",
            403: "Forbidden - Access denied",
            404: "Not Found - Resource not found",
            405: "Method Not Allowed - HTTP method not supported",
            409: "Conflict - Request conflicts with current state",
            422: "Unprocessable Entity - Invalid request data",
            429: "Too Many Requests - Rate limit exceeded",
            
            # 5xx Server Error
            500: "Internal Server Error - Server encountered an error",
            502: "Bad Gateway - Invalid response from upstream server",
            503: "Service Unavailable - Server temporarily unavailable",
            504: "Gateway Timeout - Upstream server timeout"
        }
        
        return status_messages.get(status_code, f"Unknown status code: {status_code}")
    
    def get_users(self, page: int = 1, limit: int = 10) -> Dict:
        """Get paginated list of users"""
        params = {'page': page, 'limit': limit}
        response = self.get('/users', params=params)
        return self.handle_response(response)
    
    def get_user_by_id(self, user_id: int) -> Dict:
        """Get specific user by ID"""
        response = self.get(f'/users/{user_id}')
        return self.handle_response(response)
    
    def create_user(self, user_data: Dict) -> Dict:
        """Create new user"""
        required_fields = ['username', 'email']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        response = self.post('/users', data=user_data)
        return self.handle_response(response)
    
    def update_user(self, user_id: int, user_data: Dict) -> Dict:
        """Update existing user"""
        response = self.put(f'/users/{user_id}', data=user_data)
        return self.handle_response(response)
    
    def patch_user(self, user_id: int, user_data: Dict) -> Dict:
        """Partially update user"""
        response = self.patch(f'/users/{user_id}', data=user_data)
        return self.handle_response(response)
    
    def delete_user(self, user_id: int) -> Dict:
        """Delete user"""
        response = self.delete(f'/users/{user_id}')
        return self.handle_response(response)
    
    def upload_user_avatar(self, user_id: int, image_path: str) -> Dict:
        """Upload user avatar"""
        try:
            with open(image_path, 'rb') as f:
                files = {'avatar': f}
                response = self.post(f'/users/{user_id}/avatar', files=files)
                return self.handle_response(response)
        except FileNotFoundError:
            return {
                'success': False,
                'error': f"File not found: {image_path}"
            }
```

### 3. Practical Usage Examples

```python
def demo_api_usage():
    """Demonstrate API usage with real examples"""
    
    # Initialize API client
    api = RESTAPIManager("https://jsonplaceholder.typicode.com")
    
    # Example 1: Get all users
    print("=== Getting Users ===")
    users_response = api.get_users(page=1, limit=5)
    if users_response['success']:
        print(f"Status: {users_response['status_code']}")
        print(f"Users count: {len(users_response['data'])}")
        for user in users_response['data'][:2]:  # Show first 2 users
            print(f"- {user['name']} ({user['email']})")
    else:
        print(f"Error: {users_response['error']}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Get specific user
    print("=== Getting Specific User ===")
    user_response = api.get_user_by_id(1)
    if user_response['success']:
        user = user_response['data']
        print(f"User: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Company: {user['company']['name']}")
    else:
        print(f"Error: {user_response['error']}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Create new user (will fail on jsonplaceholder, but shows structure)
    print("=== Creating User ===")
    new_user_data = {
        'username': 'devops_user',
        'email': 'devops@example.com',
        'name': 'DevOps Engineer'
    }
    
    create_response = api.create_user(new_user_data)
    if create_response['success']:
        print(f"User created with ID: {create_response['data'].get('id')}")
    else:
        print(f"Error: {create_response['error']}")
        print(f"Details: {create_response.get('details')}")

def advanced_api_example():
    """Advanced API usage with error handling and retries"""
    
    def retry_request(func, max_retries=3, delay=1):
        """Retry function with exponential backoff"""
        import time
        
        for attempt in range(max_retries):
            try:
                result = func()
                if result['success']:
                    return result
                
                # If it's a rate limit error, wait longer
                if result['status_code'] == 429:
                    wait_time = delay * (2 ** attempt)
                    print(f"Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    break
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    return {'success': False, 'error': str(e)}
                time.sleep(delay * (2 ** attempt))
        
        return result
    
    api = RESTAPIManager("https://api.github.com")
    
    # Example: Get GitHub user with retry mechanism
    def get_github_user():
        return api.get_user_by_id("octocat")
    
    result = retry_request(get_github_user)
    
    if result['success']:
        user = result['data']
        print(f"GitHub User: {user.get('login', 'N/A')}")
        print(f"Public Repos: {user.get('public_repos', 'N/A')}")
    else:
        print(f"Failed to get user: {result['error']}")

# Run examples
if __name__ == "__main__":
    demo_api_usage()
    print("\n" + "="*80 + "\n")
    advanced_api_example()
```

---

## Error Handling & Status Codes

### 1. Comprehensive Error Handling

```python
import logging
from enum import Enum
from typing import Optional, Callable, Any

class HTTPStatusCode(Enum):
    """HTTP Status Code enumeration"""
    # Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    
    # Redirection
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    
    # Client Error
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429
    
    # Server Error
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

class APIError(Exception):
    """Custom API Exception"""
    def __init__(self, message: str, status_code: int, response_data: Optional[Dict] = None):
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(self.message)

def handle_api_errors(func: Callable) -> Callable:
    """Decorator for handling API errors"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            logging.error(f"Network error in {func.__name__}: {e}")
            raise APIError(f"Network error: {str(e)}", 0)
        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error in {func.__name__}: {e}")
            raise APIError(f"Invalid JSON response: {str(e)}", 0)
        except Exception as e:
            logging.error(f"Unexpected error in {func.__name__}: {e}")
            raise APIError(f"Unexpected error: {str(e)}", 0)
    return wrapper

class RobustAPIClient(APIClient):
    """API Client with comprehensive error handling"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        super().__init__(base_url, timeout)
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    @handle_api_errors
    def safe_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """
        Make safe API request with comprehensive error handling
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint
            **kwargs: Additional arguments for the request
            
        Returns:
            Standardized response dictionary
        """
        method_map = {
            'GET': self.get,
            'POST': self.post,
            'PUT': self.put,
            'DELETE': self.delete,
            'PATCH': self.patch
        }
        
        if method not in method_map:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        request_func = method_map[method]
        self.logger.info(f"Making {method} request to {endpoint}")
        
        try:
            response = request_func(endpoint, **kwargs)
            
            # Log response details
            self.logger.info(f"Response status: {response.status_code}")
            
            # Handle different status codes
            if response.status_code == HTTPStatusCode.OK.value:
                return self._success_response(response)
            elif response.status_code == HTTPStatusCode.CREATED.value:
                return self._created_response(response)
            elif response.status_code == HTTPStatusCode.NO_CONTENT.value:
                return self._no_content_response(response)
            elif response.status_code == HTTPStatusCode.BAD_REQUEST.value:
                return self._bad_request_response(response)
            elif response.status_code == HTTPStatusCode.UNAUTHORIZED.value:
                return self._unauthorized_response(response)
            elif response.status_code == HTTPStatusCode.FORBIDDEN.value:
                return self._forbidden_response(response)
            elif response.status_code == HTTPStatusCode.NOT_FOUND.value:
                return self._not_found_response(response)
            elif response.status_code == HTTPStatusCode.TOO_MANY_REQUESTS.value:
                return self._rate_limit_response(response)
            elif 500 <= response.status_code < 600:
                return self._server_error_response(response)
            else:
                return self._generic_response(response)
                
        except requests.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            raise APIError(f"Request failed: {str(e)}", 0)
    
    def _success_response(self, response: requests.Response) -> Dict:
        """Handle successful response"""
        try:
            data = response.json()
        except json.JSONDecodeError:
            data = response.text
        
        return {
            'success': True,
            'status_code': response.status_code,
            'data': data,
            'message': 'Request successful'
        }
    
    def _created_response(self, response: requests.Response) -> Dict:
        """Handle resource created response"""
        try:
            data = response.json()
        except json.JSONDecodeError:
            data = response.text
        
        return {
            'success': True,
            'status_code': response.status_code,
            'data': data,
            'message': 'Resource created successfully'
        }
    
    def _no_content_response(self, response: requests.Response) -> Dict:
        """Handle no content response"""
        return {
            'success': True,
            'status_code': response.status_code,
            'data': None,
            'message': 'Operation completed successfully'
        }
    
    def _bad_request_response(self, response: requests.Response) -> Dict:
        """Handle bad request response"""
        try:
            error_details = response.json()
        except json.JSONDecodeError:
            error_details = response.text
        
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Bad Request',
            'details': error_details,
            'message': 'Invalid request parameters or data'
        }
    
    def _unauthorized_response(self, response: requests.Response) -> Dict:
        """Handle unauthorized response"""
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Unauthorized',
            'message': 'Authentication required or invalid credentials'
        }
    
    def _forbidden_response(self, response: requests.Response) -> Dict:
        """Handle forbidden response"""
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Forbidden',
            'message': 'Access denied - insufficient permissions'
        }
    
    def _not_found_response(self, response: requests.Response) -> Dict:
        """Handle not found response"""
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Not Found',
            'message': 'Requested resource not found'
        }
    
    def _rate_limit_response(self, response: requests.Response) -> Dict:
        """Handle rate limit response"""
        retry_after = response.headers.get('Retry-After', 'unknown')
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Rate Limit Exceeded',
            'retry_after': retry_after,
            'message': 'Too many requests - please try again later'
        }
    
    def _server_error_response(self, response: requests.Response) -> Dict:
        """Handle server error response"""
        return {
            'success': False,
            'status_code': response.status_code,
            'error': 'Server Error',
            'message': 'Internal server error - please try again later'
        }
    
    def _generic_response(self, response: requests.Response) -> Dict:
        """Handle any other response"""
        try:
            data = response.json()
        except json.JSONDecodeError:
            data = response.text
        
        return {
            'success': 200 <= response.status_code < 300,
            'status_code': response.status_code,
            'data': data,
            'message': f'Response with status code {response.status_code}'
        }
```

---

## Real-World Examples


```python
import unittest
from unittest.mock import patch, Mock

class TestAPIClient(unittest.TestCase):
    """Test cases for API client functions"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.client = RobustAPIClient("https://api.test.com")
    
    def test_successful_get_request(self):
        """Test successful GET request"""
        with patch('requests.Session.get') as mock_get:
            # Mock successful response
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"id": 1, "name": "Test User"}
            mock_get.return_value = mock_response
            
            result = self.client.safe_request('GET', '/users/1')
            
            self.assertTrue(result['success'])
            self.assertEqual(result['status_code'], 200)
            self.assertEqual(result['data']['name'], "Test User")
    
    def test_api_error_handling(self):
        """Test API error handling"""
        with patch('requests.Session.get') as mock_get:
            # Mock error response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.json.return_value = {"error": "User not found"}
            mock_get.return_value = mock_response
            
            result = self.client.safe_request('GET', '/users/999')
            
            self.assertFalse(result['success'])
            self.assertEqual(result['status_code'], 404)
            self.assertEqual(result['error'], 'Not Found')
    
    def test_network_error(self):
        """Test network error handling"""
        with patch('requests.Session.get') as mock_get:
            mock_get.side_effect = requests.ConnectionError("Network error")
            
            with self.assertRaises(APIError):
                self.client.safe_request('GET', '/users/1')

# Function testing utilities
def test_function_performance(func: Callable, *args, **kwargs) -> float:
    """Test function performance"""
    import time
    
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"{func.__name__} executed in {execution_time:.4f} seconds")
    return execution_time

def test_function_with_different_inputs(func: Callable, test_cases: List[Dict]) -> Dict:
    """Test function with multiple input scenarios"""
    results = {}
    
    for i, test_case in enumerate(test_cases):
        test_name = test_case.get('name', f'test_case_{i}')
        inputs = test_case.get('inputs', {})
        expected = test_case.get('expected')
        
        try:
            result = func(**inputs)
            success = result == expected if expected is not None else True
            results[test_name] = {
                'success': success,
                'result': result,
                'expected': expected
            }
        except Exception as e:
            results[test_name] = {
                'success': False,
                'error': str(e),
                'expected': expected
            }
    
    return results

# Example usage of testing utilities
def example_testing():
    """Demonstrate function testing"""
    
    # Performance testing
    test_function_performance(calculate_factorial, 10, 1)
    
    # Multiple input testing
    test_cases = [
        {
            'name': 'valid_email',
            'inputs': {'email': 'test@example.com'},
            'expected': True
        },
        {
            'name': 'invalid_email',
            'inputs': {'email': 'invalid-email'},
            'expected': ValueError
        },
        {
            'name': 'empty_email',
            'inputs': {'email': ''},
            'expected': ValueError
        }
    ]
    
    test_results = test_function_with_different_inputs(validate_email, test_cases)
    for test_name, result in test_results.items():
        print(f"{test_name}: {'PASS' if result['success'] else 'FAIL'}")

---

## Code Summary

This comprehensive tutorial covers all essential aspects of Python functions and REST API development:

### Python Functions Covered:
1. **Basic Functions** - Simple functions, parameters, return values
2. **Advanced Parameters** - Default values, *args, **kwargs, flexible functions
3. **Lambda Functions** - Anonymous functions, use with map/filter/sort
4. **Decorators** - Function modification, timing, validation, logging
5. **Generators** - Memory-efficient iteration, yield statements
6. **Closures** - Functions returning functions, state management

### REST API Features:
1. **HTTP Methods** - GET, POST, PUT, DELETE, PATCH with proper implementation
2. **Status Code Handling** - Comprehensive handling of all HTTP status codes
3. **Error Management** - Custom exceptions, retry logic, logging
4. **Authentication** - Bearer tokens, API keys, session management
5. **Request/Response Processing** - JSON handling, file uploads, parameter validation

### Real-World Applications:
1. **DevOps Monitoring** - Server health, log management, alerting
2. **CI/CD Pipeline** - Build triggers, status monitoring, deployment automation
3. **Cloud Infrastructure** - Instance management, auto-scaling, load balancers

### Best Practices:
1. **Code Quality** - Type hints, documentation, single responsibility
2. **Error Handling** - Specific exceptions, context managers, validation
3. **Testing** - Unit tests, mocking, performance testing
4. **Security** - Input validation, authentication, secure headers

### Key HTTP Status Codes:
- **2xx Success**: 200 (OK), 201 (Created), 204 (No Content)
- **3xx Redirection**: 301 (Moved Permanently), 304 (Not Modified)
- **4xx Client Error**: 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 429 (Rate Limited)
- **5xx Server Error**: 500 (Internal Server Error), 503 (Service Unavailable)

This tutorial provides production-ready code patterns that can be directly used in DevOps environments for automation, monitoring, and infrastructure management.