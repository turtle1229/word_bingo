import numpy as np


S = int(input())
A = np.array([input().split() for i in range(S)])

# 勝利条件flagをFalseとする
flag = False

N = int(input())
w_list = np.array([input().split() for i in range(N)])

# Aの中に入力した値と一致する値があればその値を「*」として印をつける
for w in w_list:
    if w in A:
        num = np.where(A == w)
        A[num] = "＊"

for i in range(len(A)):
    # 縦のいずれかで「＊」がそろえば勝利条件flagをTrueとする
    if all(A[:, i] == "＊"):
        flag = True
    # 横のいずれかで「＊」がそろえば勝利条件flagをTrueとする
    elif all(A[i] == "＊"):
        flag = True

# 斜めで「＊」がそろえば勝利条件flagをTrueとする
if all(np.diag(A) == "＊"):
    flag = True

if (flag):
    print("yes")
else:
    print("no")
