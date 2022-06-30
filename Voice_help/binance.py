import websockets
import time
import asyncio
import json
import matplotlib.pyplot as plt


x_data = []
y_data = []

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()


def update_graph():
    ax.plot(x_data, y_data)
    fig.canvas.draw()
    plt.pause(0.1)

async def main():
    url = 'wss://stream.binance.com:9443/stream?streams=btcusdt@minTicker'
    async with websockets.connect(url) as websock:
        while True:
            data = json.loads(await websock.recv())['data']
            time_graph = time.localtime(data['E'] // 1000)  # change nanosec to sec
            time_graph = f"{time_graph.tm_hour}:{time_graph.tm_min}:{time_graph.tm_sec}"

            print(time_graph, '=>', data['s'], data['c'])

            x_data.append(time_graph)
            y_data.append(data['c'])
            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
