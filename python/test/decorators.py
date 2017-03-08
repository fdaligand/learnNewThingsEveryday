import pdb


def pain(func):
    def wrapper(*args,**kwargs):
        print("<:::::::::::::>")
        func(*args,**kwargs)
        print("<=============>")
    return wrapper

def ingredient(func):
    def wrapper(*args,**kwargs):
        print("#...tomates...#")
        func(*args,**kwargs)
        print("#...salade....#")
    return wrapper

@pain
@ingredient
def burger(viande="jambon"):
    print("#---{}---#".format(viande))



print("burger par défaut")
burger("jambon")

print("burger au poulet")
burger("poulet")
