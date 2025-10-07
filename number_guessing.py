import random

secret_number = random.randint(1, 100)
attempts = 0

print("1-100 arası bir sayı tuttum! Tahmin et!")

while True:
    guess = int(input("Tahminin: "))
    attempts += 1
    
    if guess < secret_number:
        print("Daha BÜYÜK bir sayı tahmin et!")
    elif guess > secret_number:
        print("Daha KÜÇÜK bir sayı tahmin et!")
    else:
        print(f"TEBRİKLER! {attempts}. denemede bildin! 🎉")
        break