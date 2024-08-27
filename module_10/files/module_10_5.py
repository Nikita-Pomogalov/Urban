import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            strk = f.readline()
            if not strk:
                break
            all_data.append(strk.strip())


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start = datetime.datetime.now()
for i in range(len(files)):
    read_info(files[i])
end = datetime.datetime.now()
print(end - start)
# 0:00:02.255342

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, files)

    end = datetime.datetime.now()
    print(end - start)

# 0:00:00.787510
