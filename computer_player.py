import random

form guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    min =  MIN
    max = MAX
    guess_nachine = GuessMachine()
    while True :
        attempt = random.randint(min,max)
        result = guess_nachine.guess(attempt)
        print('tried %d : %s' %(attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' %guess_nachine.number_of_attempt)
        elif result == 'too low':
            min = attempt + 1
        else:
            max = attempt - 1
