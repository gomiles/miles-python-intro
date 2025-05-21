import time

def decode(secret):
    return secret[::-1]  # reverses the string

def reveal_the_secret():
    print("🔐 Accessing encrypted system logs...")
    time.sleep(5)
    print("🧠 Decoding messages from the Python realm...\n")
    time.sleep(2)

    messages = [
        "!pu tes gnihtyrevE 👏 .nohtyP dna rosruC pu gnittes boj dooG",
        "!ti edam uoy ,snoitalutargnoC 🎉",
        ".tsissa ot ydaer si rosruC 🤖",
        "!ecitnerppa draziw gnidoc a flesruoy llac yllaciffo nac uoY ✅"
    ]
    
    for secret in messages:
        print(decode(secret))
        time.sleep(1)

reveal_the_secret()
