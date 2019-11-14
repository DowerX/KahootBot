from bot import Bot
#from threading import Thread

count = 10
prefix = "Bot"
pin = "536700"

threadCount = 4

bots = []

def main():
    global count, bots, prefix, pin
    for i in range(0, 10):
        bots.append(Bot())
        bots[i].login(pin, prefix + str(i))

    while True:
        v = input("vote for: ")
        if v != "":
            for b in bots:
                b.vote(int(v))
        else:
            for b in bots:
                b.quit()
            break

if __name__ == "__main__":
    main()