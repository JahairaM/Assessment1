students = ["Bob", "John", "Sally"]
list1 = [1, "car", False, 20.1]
print(list1)
print(students)

word_list = ["Python", "is", "great!"]
phrase = " ".join(word_list)
print(phrase)

jap_car = ["Toyota", "Honda", "Mitsubishi"]
am_car = ["Chevy", "Ford", "Telsa"]
for car in am_car:
    if car[-1] == "a":
        print(car)
for car in jap_car:
    if car[-1] == "a":
        print(car)

character_string = "abcdefghijk"
for_loop_character_list = []

vowels = "aeiou"
for character in character_string:
    
