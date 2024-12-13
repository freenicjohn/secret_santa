import random

needs_gift = ['Nic', 'Audz', 'James', 'Grace', 'Edy', 'Allan']
needs_recipient = ['Nic', 'Audz', 'James', 'Grace', 'Edy', 'Allan']
secret_santa = {}

if __name__ == "__main__":
    for giver in needs_recipient:
        recipient = random.choice(needs_gift)
        while recipient == giver:
            recipient = random.choice(needs_gift)
        needs_gift.remove(recipient)
        secret_santa[giver] = recipient
    print(secret_santa)
