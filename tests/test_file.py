class TestClass:
    '''A test class with two simple methods.'''
    def __init__(self):
        self.value = 42
    
    def method_1(self):
        return self.value * 2
	    
    def method_2(self):  
        return self.value + 10


def test_function():
    print("This uses 4 spaces.")
    print("This uses tabs.")  # This line uses tabs instead of spaces
    print("This uses 2 spaces.")
    print("This uses 8 spaces.")




def badly_formatted_function(x, y, z):
    '''Adds x, y, z only if all are positive. Returns 0 otherwise.'''

    if (x > 0) and (y > 0) and (z > 0):
        return x + y + z
    return 0
         
def long_line_function():
    '''Returns a long string split across multiple lines for readability.'''
    return (
        'This is a very long string that exceeds the recommended line length'
        'and should be split across multiple lines for better readability.'
    )

if __name__ == '__main__':
    test_function()

    obj = TestClass()
    print(obj.method1())
    print(obj.method2())

    print(badly_formatted_function(1, 2, 3))
    print(long_line_function()) 