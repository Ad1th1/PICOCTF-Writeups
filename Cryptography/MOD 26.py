# Just used rot13.com to get the flag and then decided to check out the python code for rot13, because, why not? lol!

def rot13(phrase):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ans = " "

    for char in phrase:
        ans += abc[(abc.find(char)+13)%26]
    return ans


phrase = raw_input('Enter a phrase: ')

print(rot13(phrase))
