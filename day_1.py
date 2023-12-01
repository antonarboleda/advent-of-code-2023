# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to 
# take a look. The Elves have even given you a map; on it, they've used stars to
# mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, 
# you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each
#  day in the Advent calendar; the second puzzle is unlocked when you complete
#  the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine
#  ("not powerful enough") and where they're even sending you ("the sky") and 
# why your map looks mostly blank ("you sure ask a lot of questions") and hang
#  on did you just say the sky ("of course, where do you think snow comes from")
#  when you realize that the Elves are already loading you into a trebuchet 
# ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration
#  document (your puzzle input) has been amended by a very young Elf who was 
# apparently just excited to show off her art skills. Consequently, the Elves
#  are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line 
# originally contained a specific calibration value that the Elves now need to 
# recover. On each line, the calibration value can be found by combining the 
# first digit and the last digit (in that order) to form a single two-digit
#  number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, 
# and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the 
# calibration values?
# Part 1

# Use a Trie so that when encounter a potential integer spelled out as a word
# we can see if it is a word. I.e. if we encounter a "o", the next letters
# could be "ne" and "one" == 1

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False
        self.int_value = -1
    def __repr__(self):
        return f"{self.children} {self.end_word} {self.int_value}"

def sum_values():
    try:
        with open("./values.csv", "r") as f:
            result = 0
            for raw_line in f.readlines():
                line = raw_line.strip()
                digits = []
                i = 0
                
                while i < len(line):
                    if line[i].isdigit():
                        digits.append(line[i])
                        break
                    i += 1

                i = len(line) - 1
                while i >= 0:
                    if line[i].isdigit():
                        digits.append(line[i])
                        break
                    i -= 1
                result += int("".join(digits))
            return result
    except Exception as e:
        print(e)

def word_exists(i, line, root):
    cur = root
    for j in range(i, len(line)):
        char = line[j]
        if char not in cur.children:
            return -1
        cur = cur.children[char]
        if cur.end_word:
            return cur.int_value
        
    return -1

def word_exists_reversed(i, line, root):
    cur = root
    for j in range(i, -1, -1):
        char = line[j]
        if char not in cur.children:
            return -1
        cur = cur.children[char]
        if cur.end_word:
            return cur.int_value
    return -1

def get_value(line, prefix_root, suffix_root):
    i = 0
    digits = []
    while i < len(line):
        if line[i].isdigit():
            digits.append(line[i])
            break
        elif line[i] in prefix_root.children:
            value = word_exists(i, line, prefix_root)
            if value >= 0:
                digits.append(str(value))
                break
        i += 1
    
    i = len(line) - 1
    while i >= 0:
        if line[i].isdigit():
            digits.append(line[i])
            break
        elif line[i] in suffix_root.children:
            value = word_exists_reversed(i, line, suffix_root)
            if value >= 0:
                digits.append(str(value))
                break
        i -= 1    
    return int("".join(digits))
            


def buildTries():
    prefix_root = TrieNode()
    suffix_root = TrieNode()    
    int_mapping = {
        0: "zero",
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four",
        5: "five",
        6: "six",
        7: "seven", 
        8: "eight",
        9: "nine"
    }
    
    for n in range(10):
        cur = prefix_root
        word = int_mapping[n]
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_word = True
        cur.int_value = n

        cur = suffix_root
        for char in reversed(word):
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_word = True
        cur.int_value = n
    return prefix_root, suffix_root

def sum_values_spelled():
    prefix_root, suffix_root = buildTries()
    try:
        with open("./values.csv", "r") as f:
            result = 0
            for raw_line in f.readlines():
                result += get_value(raw_line.strip(), prefix_root, suffix_root)
            return result
    except Exception as e:
        raise e


if __name__ == "__main__":
    print(sum_values_spelled())
