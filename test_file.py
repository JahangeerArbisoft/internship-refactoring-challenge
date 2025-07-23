# Test file with various formatting issues

def test_function():
    print("This uses 4 spaces")
	print("This uses tabs")  # This line uses tabs instead of spaces
  print("This uses 2 spaces")
        print("This uses 8 spaces")

class TestClass:
	def __init__(self):
		self.value = 42
    
	def method1(self):
	    return self.value * 2
	    
    def method2(self):  # Mixed indentation in class
        return self.value + 10

# Function with no docstring and poor practices
def badly_formatted_function(x,y,z):
    if x>0:
        if y>0:
            if z>0:
                result=x+y+z
                return result
            else:
                return 0
        else:
            return 0
    else:
        return 0

# Long line that should be split
def long_line_function():
    return "This is a very long string that exceeds the recommended line length and should be split across multiple lines for better readability"

if __name__=="__main__":
    test_function()
    obj=TestClass()
    print(obj.method1())
    print(obj.method2())
    print(badly_formatted_function(1,2,3))
    print(long_line_function()) 