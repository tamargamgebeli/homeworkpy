
def kilometers_to_meters(kilometers):
    meters=0.62*kilometers
    return meters
result=kilometers_to_meters(5)
print(result)

def calculate_volume(heigh=1,width=1,length=1):
    volume=heigh*width*length
    return volume
result=calculate_volume(5,2)
print(result)

def get_vowels(*args):
    vowels = 'aeiou'  
    result = []
    for string in args:
        if string[0] in vowels:
            result.append(string)
    return result  


print(get_vowels("iaragi", "asanti"))  
