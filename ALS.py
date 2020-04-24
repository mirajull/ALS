import pandas as pd
import numpy as np


def als(alpha, k, user_no, item_no, data):
    u = np.zeros((user_no, k))                      # n*k
    vlist = []
    for i in range(0, user_no):
        for j in range(0, k):
            u[i][j] = np.random.uniform(0, 1, 1)
    for j in range(0, 1):
        v = np.zeros((k, k))
        for i in range(0, user_no):
            if data.iloc[i][j] != 99:
                v = np.add(v, np.dot(u[i].transpose(), u[i]))
        v = np.add(v, alpha*np.identity(k))         # k*1
        v = np.linalg.inv(v)
        temp = np.zeros((k, 1))
        #print(temp)
        for i in range(0, user_no):
            if data.iloc[i][j] != 99:
                temp = np.add(temp, (data.iloc[i][j]*u[i].transpose()))
        v = np.dot(v, temp)
        vlist.append(v)
    #print(vlist[0])
    return


def read():
    data = pd.read_csv('now.csv')
    user_no = data.shape[0]
    item_no = data.shape[1]
    als(0.1, 5, user_no, item_no, data)


def main():
    read()


if __name__ == '__main__':
    main()