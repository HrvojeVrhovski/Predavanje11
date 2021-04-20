import random
import datetime
import json

current_time = datetime.datetime.now()
secret = random.randint(1, 30)
attempts = 0
wrong = []
ime=input("Unesi svoje ime: ")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    score_text = "{0} {1} attempts {2}. Secret number was {3}. Wrong were: {4}".format(score_dict.get("ime"),
               str(score_dict.get("attempts")), score_dict.get("date"), score_dict.get("secret"), score_dict.get("wrong"))
    print(score_text)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "ime": ime,
                               "secret": secret, "wrong": wrong})
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong.append(guess)