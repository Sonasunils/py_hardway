
#define function and pass argument
def print_two(*args):
    arg1, arg2 ,arg3= args
    print(f"arg1: {arg1}, arg2: {arg2}")
#hold two parameters 
def print_two_agin(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
# function hold one parameter and print
def print_one(arg1):
    print(f"arg1: {arg1}")
#without parameter
def print_none():
    print("i got nothing")

print_two("zed","shaw")
print_two_agin("zed","shaw")
print_one("first")
print_none()