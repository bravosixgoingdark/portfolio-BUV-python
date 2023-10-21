import random 



def card_generation():
    number = random.randint(1, 13)
    match number:
        case 1:
            return "Ace"
        case 11: 
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case default:
            return number

while True:
    