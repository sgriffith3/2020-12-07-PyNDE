

def basic_func(name, greeting="Hi"):
    return f"{greeting} {name}!"


def test_basic_func():
    assert basic_func("steve") == "Hi steve!"

def test_basic_func_failure():
    assert basic_func("becky") != "Hi Becky!"

#result = basic_func("steve")
#if result == "Hi steve!":
#    print("Success!!!")
#print(result)
#
#result2 = basic_func("Becky")
#if result2 != "Hello Becky!":
#    print("The code broke appropriately")
#
#print(result2)
#
#
