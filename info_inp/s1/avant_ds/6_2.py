maxi = 1.01
mini = 0
guess = 0.5
count_guess = 1
stop = False

print("Je vais deviner un réel entre 0 et 1 auquel vous pensez (à 10**-2 près)")
while not stop :
    answer = input(f"Est-ce {guess} ? ")
    if answer == '+':
        mini = guess
        guess = (guess + maxi) /2
        count_guess += 1
    elif answer == "-":
        maxi = guess
        guess = (guess + mini) /2
        count_guess += 1
    else : 
        stop = True
        print(f"J’ai trouvé en {count_guess} questions.")
