from bot import Bot
from threading import Thread

count = 20
prefix = "Bot"
pin = "628188"

threadCount = count

threads = []
bots = []

def creatBots(ids):
    global pin, prefix, bots
    _bots = []
    for i in range(0, len(ids)):
        _bots.append(Bot())
        _bots[i].login(pin, prefix + str(ids[i]))
    bots += _bots

def voteBots(ids, v):
    global bots
    for i in range(0, len(ids)):
        bots[i].vote(v)

def quitBots(ids):
    global bots
    for i in range(0, len(ids)):
        bots[i].quit()

def main():
    global count, threadCount, threads
    for i in range(0, threadCount):
        ids = []
        for x in range(0, int(count/threadCount)):
            ids.append(i*int(count/threadCount)+x)
        Thread(target=creatBots, args=[ids]).start()
        print(f"Started thread No. {i} with {int(count/threadCount)} bots with these ids: {ids}")

    while True:
        v = input("vote for: ")
        if v != "":
            for b in bots:
                b.vote(int(v))
            # for i in range(0, threadCount):
            #     ids = []
            #     for x in range(0, int(count/threadCount)):
            #         ids.append(i*int(count/threadCount)+x)
            #     Thread(target=voteBots, args=[ids, int(v)]).start()
            #     print(f"Stopped thread No. {i} with {int(count/threadCount)} bots with these ids: {ids}")
        else:
            for b in bots:
                b.quit()
            # for i in range(0, threadCount):
            #     ids = []
            #     for x in range(0, int(count/threadCount)):
            #         ids.append(i*int(count/threadCount)+x)
            #     Thread(target=quitBots, args=[ids]).start()
            #     print(f"Stopped thread No. {i} with {int(count/threadCount)} bots with these ids: {ids}")
            break

if __name__ == "__main__":
    main()