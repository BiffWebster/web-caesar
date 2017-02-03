def alphabet_position(letter):
    upperCase = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowerCase = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    if letter in upperCase:
        return upperCase.index(letter)
    else:
        return lowerCase.index(letter)
		
def rotate_character(char, rot): 
    
    upperCase = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowerCase = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #rot % 26 + char.index()
    if char.isalpha() == False:
        return char
    else:
        if char in upperCase:
            return upperCase[(alphabet_position(char) + rot) % len(upperCase)]
        else:
            return lowerCase[(alphabet_position(char) + rot) % len(lowerCase)]
			
def encrypt(text, rot):
    new_text = ""
    for eachChar in text:
        new_text += rotate_character(eachChar, rot)
        
    return new_text