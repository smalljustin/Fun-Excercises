import random
import plotly.express as px
import pandas

def sockSim():
    def sockTest(socks):
        if not socks:
            return False

        for sock in socks:
            # print(socks)
            testSocks = socks.copy()
            testSocks.remove(sock)
            # print(testSocks)
            if sock in testSocks:
                return True
        else:
            return False
    sockDrawer = []
    for i in range(10):
        sockDrawer.append(i+1)
        sockDrawer.append(i+1)
    chosenSocks = []

    while not sockTest(chosenSocks):
        # print(chosenSocks)
        # print(sockDrawer)
        chosenSocks.append(random.choice(sockDrawer))
        sockDrawer.remove(chosenSocks[-1])

    return len(chosenSocks)

results = [sockSim() for x in range(100000)]

df = pandas.DataFrame(data={"Socks Pulled": results})
fig = px.histogram(df, x="Socks Pulled")
fig.show()
print(sum(results)/len(results))
