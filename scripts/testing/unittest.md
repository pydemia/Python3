# Unittest

## Run test in order

In testing, you need to execute the test methods in order,
just in case of testing `save` first and `load` later.

First, create an ordering function in your `unittest.TestCase` class and
assign it to `unittest.defaultTestLoader.sortTestMethodsUsing` to execute test methods in order.
At the following:
    - `order`: normal order as your code is.
    - `reverse`: reversed order

### Example 1:

```python
class DummyTestCase(unittest.TestCase):
    def order(a, b):
        return ((a > b) - (a < b))
    
    def reverse(a, b):
        return -((a > b) - (a < b))

    unittest.defaultTestLoader.sortTestMethodsUsing = order
```

### Example 2:

1. run `save`
2. run `load`

```python
import unittest

class DummyTestCase(unittest.TestCase):
    def order(a, b):
        return ((a > b) - (a < b))
    
    def reverse(a, b):
        return -((a > b) - (a < b))

    unittest.defaultTestLoader.sortTestMethodsUsing = order

    def save(self):
        ...

    def load(self):
        name = "test"
        compare = "test2"

        self.assertNotEqual(name, compare)
```
