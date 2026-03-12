import time

print("AI Mind Reader")
time.sleep(1)

print("\nThink of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100

while low <= high:
    mid = (low + high) // 2
    
    answer = input(f"\nIs your number greater than {mid}? (y/n): ")

    if answer.lower() == "y":
        low = mid + 1
    else:
        high = mid - 1

print("\nAI Prediction Complete")
print("Your number is:", low)

