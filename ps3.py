# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
hand_Len=0
total_Score=0

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
second_component= 0

def get_word_score(word, n):
    # return (len(word) * sum(SCRABBLE_LETTER_VALUES[x] for x in word))+ (50 if len(word) == n else 0)
    first_component = 0
    s=word.lower()
    word_length=len(word)
    for letter in s:
        if  letter == '*':
            first_component = first_component + 0
        else:
            first_component = first_component + SCRABBLE_LETTER_VALUES[letter]
    if word_length> 2:
        second_component = 7 * word_length - 3 *(n-word_length)
    else:
        second_component= 1
    return  first_component * second_component



"""
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    #pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line



#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    
    return hand

#
# Problem #2: Update a hand by removing letters
#

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word_lower=word.lower()
    return dict((i,j-word_lower.count(i)) for i, j in hand.items())


    #pass  # TO DO... Remove this line when you implement this function

def get_hand(hand):
    words_in_hand= ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            words_in_hand += letter
    return words_in_hand

def Vowel_in_hand(hand):
    vowel_found=''
    for letter in hand:
        if letter in VOWELS:
            vowel_found +=letter
    return vowel_found


def Vowel_in_word(word):
    vowel_found=''
    for letter in word:
        if letter in VOWELS:
            vowel_found +=letter
    return vowel_found

def wild_char_found(hand, word):
    if "*" in word:
        return True
    elif "*" in word and "*" in hand.keys():
        return  True
    else:
        return False



def wildchar(hand,word):
    if len(Vowel_in_hand(get_hand(hand))) !=0 and '*' in word:
        return True
    elif '*' in  get_hand(hand) and '*' in word:
        return True
    elif '*' not in get_hand(hand) and '*' in word:
        return True
    elif '*' in get_hand(hand) and '*' not in word:
        return True
    else:
        return False



def Compare_hand_word(hand,word):
    count = 0
    for i in hand.keys():
        if i in word:
            count +=word.count(i)
    if count == len(word):
        return True
    else:
        return False



#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lower = word.lower()

    if word_lower in word_list  and all(hand.get(i, 0) >= j for i ,j in get_frequency_dict(word_lower).items()):
        return True
    elif wildchar(hand, word_lower):
        if word_lower not in word_list  and Compare_hand_word(hand,word_lower):
            return True
        elif not Compare_hand_word(hand,word_lower):
            return False
        else:
            return True
    else:
        return False

    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return  sum(i for i in hand.values())
    #pass  # TO DO... Remove this line when you implement this function

def unique_character(word):
    letter =0
    for i in get_frequency_dict(word).keys():
        if i in word:
            letter +=1
    return letter

def check_for_lower_cast(word):
    found_lower_cast = False
    for i in word:
        if i.islower():
            found_lower_cast=True
            break
    return found_lower_cast



def word_worth(word):
    worth = 0
    unique_char=unique_character(word)
    if unique_char == len(word) and word.islower():
        worth = 7
    elif unique_char == len(word) and not word.islower():
        if check_for_lower_cast(word):
            worth =7
        else:
            worth=4
    else:
        worth=6
    return worth

def swap_dict(hand):
    string =get_hand(hand)
    list=[]
    new_list= []
    for i in string:
        list.append(i)
    new_list =random.shuffle(list)
    return new_list
print(swap_dict(SCRABBLE_LETTER_VALUES))



def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    totalScore = 0
    output = "Ran out of letters."
    while calculate_handlen(hand) > 0:
        print("Current hand:" + get_hand(hand))
        word = input("Please enter a word or '!!' to indicate you are done:")
        if word == '!!':
            output = "Goodbye!"
            break
        else:
            if not is_valid_word(word, hand, word_list):
                print("That is not a valid word. Please choose another word")
                hand = update_hand(hand,word)

            else:
                n =word_worth(word)
                score = get_word_score(word, n)
                totalScore += score
                print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore))
                hand = update_hand(hand, word)
        print("\t")
    print(output)
    print('Total score for this hand: '+ str(totalScore) +' points.')
    print('------------------')
    global hand_Len
    global total_Score

    hand_Len =calculate_handlen(hand)
    total_Score=totalScore
    # dict1={'calculate_handlen':calculate_handlen(hand),'score':totalScore}
    # return dict1
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
#
# word_list = load_words()
# play_hand(SCRABBLE_LETTER_VALUES,word_list)

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    for i in hand.keys():
        if letter in get_hand(hand):
            count_letter_in_hand=get_hand(hand).count(letter)
            for j in range(count_letter_in_hand):
                hand=update_hand(hand,letter)
            print("Sorry the letter you choice is already in hand.")
            return hand
        else:
            input_letter=input("Which letter would you like to replace:")
            new_word=get_hand(hand).replace(input_letter,letter,get_hand(hand).count(input_letter))
            new_hand=get_frequency_dict(new_word)
            hand=new_hand
            return hand

    #pass  # TO DO... Remove this line when you implement this function

       
    
def play_game(word_list):
    initial_hand=0
    number_of_hand=int(input("Enter Total numer of hands:"))
    all_total=0
    while initial_hand < number_of_hand:
        initial_hand +=1
        hand=deal_hand(HAND_SIZE)
        play_hand(hand, word_list)
        all_total += total_Score
        if hand_Len>0:
            play_hand(hand, word_list)
            all_total += play_hand(hand, word_list)['score']
        else:
            user = input('Would you like to replay the hand (yes or no)?')
            if user == 'yes':
                play_hand(hand,word_list)
                all_total += total_Score
            elif user == 'no':
                hand = deal_hand(HAND_SIZE)
                print("Current hand:" + get_hand(hand))
                print('\n')
                substitute=input('Would you like to substitute a letter (yes or no)?')
                if substitute == 'yes':
                    letter = input("Enter the letter in your mind:")
                    hand1= substitute_hand(hand, letter)
                    play_hand(hand1, word_list)
                    all_total += total_Score
                else:
                    play_hand(hand, word_list)
                    all_total += total_Score
            else:
                print("Invalid command. Please input 'yes' or 'no' ")
                break
            print(" ")

        if initial_hand == number_of_hand:
            break

    print('\t')
    print("Total Score of all hand: "+ str(all_total))


    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
