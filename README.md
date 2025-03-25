# Let's Learn Testing in python

Here's what you'll learn. If you already know the basics direct;ly jump to the resources page- the last section of the file

# Software Testing and It's Types

Software testing is the process of evaluating an application to ensure it works correctly, efficiently, and securely. The goal is to find bugs, performance issues, or security vulnerabilities before the software is released.

## Unit Testing

Unit testing is the process of testing individual components or functions of a program in isolation. It ensures that each part of the program works correctly independently.

Suppose we have a function that ads two numbers:

```bash
#example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

```

Now, create a unit test for this function:

```bash
# Test file (test_example.py)
import pytest
from example import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
```

You can run these unit tests using `pytest`:

```bash
pytest test_example.py

```

## Integration Testing

Integration testing focuses on testing the interaction between components. It ensures that when individual units or components are integrated together, they work as expected. This can involve testing database interactions, API calls, or service-to-service communication.

Let’s assume we have two functions that interact with a database. We’ll test the integration of these functions.

```bash
# Code to test (example.py)
import sqlite3

def connect_to_db():
    conn = sqlite3.connect(':memory:')  # In-memory database
    return conn.cursor()

def insert_user(cursor, name):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    return cursor.lastrowid

def get_user_by_name(cursor, name):
    cursor.execute("SELECT * FROM users WHERE name=?", (name,))
    return cursor.fetchone()
```

Here’s the integration test:

```bash
# Test file (test_integration.py)
import pytest
from example import connect_to_db, insert_user, get_user_by_name

@pytest.fixture
def db_cursor():
    cursor = connect_to_db()
    yield cursor
    cursor.connection.close()

def test_insert_and_get_user(db_cursor):
    user_id = insert_user(db_cursor, "Alice")
    user = get_user_by_name(db_cursor, "Alice")
    assert user is not None
    assert user[0] == "Alice"
```

In this test:

We integrate `insert_user()` and `get_user_by_name()` functions.

We use an in-memory SQLite database to test how the system interacts with the database.

## System Testing

System testing tests the entire application as a whole, ensuring that it meets the specified requirements. It is the final level of testing before the product is ready for deployment.
This doesnot come under the scope of a developer so lets not go into it.

## SOME BASIC CONCEPT TO LEARN

Here are some basic topics I have prepared. Note that the given examples are just the basics to understand the terminologies. Since Testing in python hover around these terms only there are many more subtopics inside each of these topics. I have provided with the resources at the end of this file.

### 1. Assertions in Pytest

Assertions are used in tests to verify that the actual result matches the expected result. When an assertion fails, pytest reports the test as failed.

**Common Assertions:**

- `assert a == b` – Verifies that a is equal to b.
- `assert a != b` – Verifies that a is not equal to b.
- `assert a < b` – Verifies that a is less than b.
- `assert isinstance(a, Type)` – Verifies that a is an instance of the given type.

```bash
def test_add():
    assert add(2, 3) == 5
    assert isinstance(add(2, 3), int)
```

### 3. Setup and Teardown Functions

These functions are used to prepare the test environment before a test starts (setup) and clean up after the test is finished (teardown).

- **`Setup:`** Used to set up the necessary state before tests run.

- **`Teardown:`** Used to clean up any resources or state after the test completes.

```bash
import pytest

@pytest.fixture
def setup_teardown():
    # Setup
    db = connect_to_database()
    yield db  # This is where the test happens
    # Teardown
    db.close()

def test_query(setup_teardown):
    db = setup_teardown
    result = db.query("SELECT * FROM users")
    assert result == expected
```

### Fixtures in Pytest

Fixtures in pytest are a powerful way to set up and tear down conditions that your tests depend on. They help in creating a consistent testing environment and allow code reuse. Fixtures allow you to manage common preconditions like database connections, setting up mock objects, or even preparing data needed across multiple tests.

#### Basic Fixture Example

A fixture in pytest is a function that is decorated with @pytest.fixture. The fixture can be used by tests, and pytest ensures it is called before the test executes.

```bash
import pytest

@pytest.fixture
def setup_data():
    # Setup: Prepare the data or environment
    data = {"name": "Alice", "age": 30}
    yield data  # Return the data for use in tests
    # Teardown (optional): Clean up after the test
    print("Cleaning up...")

def test_user_name(setup_data):
    assert setup_data["name"] == "Alice"

def test_user_age(setup_data):
    assert setup_data["age"] == 30
```

- The `setup_data` fixture will be executed before both `test_user_name()` and `test_user_age()`.

- The `yield` keyword separates the setup code from the teardown code. The code after `yield` is executed when the test is finished (after the test has run).

### Mocking

Mocking replaces real objects or functions with fake versions for the purpose of testing. It helps isolate tests by simulating external dependencies.

- Mocking can be used to mock functions, methods, classes, or even external services.

- `unittest.mock` is typically used for mocking in Python.

```bash
from unittest.mock import patch

def test_function():
    with patch("module_name.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert some_function() == expected_result
```

### Parameterized Testing

Parameterized testing allows you to run the same test with multiple sets of input data, without having to duplicate the test code.

```bash
import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply(input, expected):
    assert input * 2 == expected
```

- This will run `test_multiply` three times with different inputs and expected outputs.

### Factory Boy

Factory Boy is a Python library for generating fake data, typically used in tests. It helps create objects (e.g., models) for testing purposes with random or default data.

```bash
from factory import Factory, Faker

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserFactory(Factory):
    class Meta:
        model = User
    name = Faker('name')
    email = Faker('email')

# Create a fake user
user = UserFactory()
print(user.name, user.email)
```

- `Faker` is used to generate realistic names, emails, etc.

## Resources

### [Pytest Tutorial – How to Test Python Code](https://www.youtube.com/watch?v=cHYq1MRoyI0)

- a comprehensive guide to complete testing basics in python

### [PPyTest • REST API Integration Testing with Python](https://www.youtube.com/watch?v=7dgQRVqF1N0)

- Integration Testing in python (API integration with a working api)

### [Professional Python Testing with Mocks](https://www.youtube.com/watch?v=-F6wVOlsEAM)

- A deep dive into mocking

### [Pytest Tutorial – How to Test Python Code](https://www.youtube.com/watch?v=cHYq1MRoyI0)

- a comprehensive guide to complete testing basics in python

### [DjangoCon 2022 | factory_boy: testing like a pro](https://www.youtube.com/watch?v=-C-XNHAJF-c)

- How to test complex objects using the library factory_boy. Best Practices
