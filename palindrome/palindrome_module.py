import re 

def palindrome(str):
    str = str.lower()
    str = re.sub(' ','',str)
    letters = list(str)
    palindrome = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            palindrome = False
            break

    return palindrome

def main():
   return palindrome

if __name__ == '__main__':
    main()
