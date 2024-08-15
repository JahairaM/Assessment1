def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for a {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month..."
    else:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for a {min_beds} bedroom apartments, all within a budget of ${max_rent} per month.."
    return result

print(apt_search1("Detroit", 2000,2, True))
print(apt_search1("Southfield", 2300,2, False))

def apt_search2(city, max_rent, min_beds= 1, pets_allowed= False):
    if pets_allowed:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for a {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month..."
    else:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for a {min_beds} bedroom apartments, all within a budget of ${max_rent} per month.."
    return result
print(apt_search2("Detroit", 2000))
print(apt_search2("Detroit",1800, min_beds=2))
print(apt_search2("Detroit",1750, pets_allowed=True))

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x * x
concatente = lambda d: "-"+ d
divide_by_three = lambda x: x/3


print(plus_one_hundred(30))
print(square_num(4))
print(concatente("hello"))
print(divide_by_three(9))
