import random
num=random.randint(1,5)
if num==1:
    answer="WARIO"
elif num==2:
    answer="WALUIGI"
elif num==3:
    answer="ZOMBIE"
elif num==4:
    answer="SOLARFLARE"
elif num==5:
    answer="ALCREMIE"
word="0"
hint=""
for start in range(len(answer)):
    hint=hint+"_"
while word!=answer:  
    print(f"Your hint: {hint}")
    word=input("Please input your word. ").upper()
    hint=""
    if len(word)>len(answer) or len(word)<len(answer):
        print("Not the correct length")
    elif word!=answer:
        print("INCORRECT")
        for process in range(len(answer)):
            if word[process]==answer[process]:
                hint=hint+(f"{(word[process]).upper()}")
            elif word[process]==answer[0] or word[process]==answer[1] or word[process]==answer[2] or word[process]==answer[3] or word[process]==answer[4] or word[process]==answer[5] or word[process]==answer[6] or word[process]==answer[7] or word[process]==answer[8] or word[process]==answer[9]:
                hint=hint+(f'{(word[process]).lower()}')
            else:
                hint=hint+"_"
print(f"Correct! The word is '{(answer.title())}'.")