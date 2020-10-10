import random

form guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
  guess_nachine = GuessMachine()
  while True :
    attempt = random.randint(MIN,MAX)
    result = guess_nachine.guess(attempt)
    print('tried %d : %s' %(attempt, result))
    if result == 'round':
      print('Finished in %d attempts.' %guess_nachine.number_of_attempt)
      break
