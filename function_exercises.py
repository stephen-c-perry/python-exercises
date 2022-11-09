def is_vowel():
    char = input('Enter a letter: ')
    if type(char.lower()) in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def is_vowel():
    char = input('Enter a letter: ')
    if type(char.lower()) in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def is_consonant():

    char = input('enter a letter: ')

    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False



def is_word():

    word = str(input('Enter a single word: '))

    if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
        return word.capitalize()




def calculate_tip():
    tip = int(input('Enter the percentage you want to tip: '))
    total = int(input('Enter the total bill:$ '))

    return (float(tip / 100 + 1) * total)


def apply_discount(price, disc_perc):
    discount = price * disc_perc
    return price - discount



def handle_commas(string):
    string = string.replace(",", "")
    return string
    

def get_letter_grade():
    if (score < 60):
        return "F"
    if (score <70):
        return "D"
    
    

def remove_vowels(string):
    vowel = ['a', 'e', 'i', 'o', 'u']

    for x in string.lower():
        if x in vowel:
            string = string.replace(x,"")
    print(string)
    

def normalize_name(string):
    string = string.replace("$", "")
    string = string.replace("#", "")
    string = string.replace("!","")
    string = string.replace("?", "")
    string = string.replace("", "_")
    string = string.lower()
    return (string)
    


def cumulative_sum(nums):
    output= []
    total = 0 
    for num in nums:
        total += num
        output.append(total)
    return output

    