import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lower + upper + numbers +symbols
len=10
password ="".join(random.sample(string,len))
print("your new password IS:" + password)