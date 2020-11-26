from sys import argv

script, user_name = argv
prompt = 'ANSWER: '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Do you programming in Python?")
language = input(prompt)

print('''
Alright, so you said %r about linking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
And you said %r ...programming in Python.
''' % (likes, lives, computer, language))