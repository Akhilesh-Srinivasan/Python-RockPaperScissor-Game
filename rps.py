import random
print("Welcome to Rock, Paper, Scissors game")
print("Type 'exit' to exit")
us=0
cs=0
cc=random.randint(0,2)

while True:
    uc=input("Rock(0) or Paper(1) or Scissors(2) : ").lower()
    if uc=="0":
        if cc==0:
            pass
        if cc==1:
            cs+=1
        if cc==2:
            us+=1
    if uc=="1":
        if cc==0:
            us+=1
        if cc==1:
            pass
        if cc==2:
            cs+=1
    if uc=="2":
        if cc==0:
            cs+=1
        if cc==1:
            us+=1
        if cc==2:
            pass
    if uc=="score":
        print("Computer =",cs)
        print("User =",us)
    if uc=="exit":
        exit()
