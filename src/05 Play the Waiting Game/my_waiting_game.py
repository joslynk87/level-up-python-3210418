import random
import time

def waiting_game():
  wait_time = random.randint(2,4)
  user_input = input(f"Your target time is {wait_time} seconds. \r\n ---Press Enter to Begin---")

  if user_input == "":
    start_time = time.perf_counter()

    user_input = input(f"...Press Enter again after {wait_time} seconds...")
    end_time = time.perf_counter() - start_time
    time_diff = end_time - wait_time
    print(f"\nElapsed time: {end_time :.3f} seconds")
    if (time_diff > 0):
      print(f'({time_diff :.3f} seconds too slow)')
    elif (time_diff < 0):
      print(f'({abs(time_diff) :.3f} seconds too fast)')
    else:
      print('right on target)')


waiting_game()