class A:
    def __init__(obj, name):
        obj.name =  name
def show(obj):
    print(obj.name)

a = A('title')

print(a)