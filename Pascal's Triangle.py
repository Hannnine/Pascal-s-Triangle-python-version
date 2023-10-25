# 用户输入
uipt = input("How many rows you want to print? [1,9]")
v_ipt = "0123456789"    #有效输入
if uipt in v_ipt:       #防止输入不为数字导致int()报错
    n = int(uipt)
    if n < 1 or n > 9:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")     #非数字输入
    exit()

# 阶乘
def plus(n):
    a = i = 1
    while i < n:
        a *= (i + 1)
        i += 1
    return a

# 返回值
def trfun_ret(i, j):
    m = i - 1
    n = j - 1
    ans = plus(m) // (plus(n) * plus(m - n))
    ans = int(ans)
    # if ans == 1:
    #     ans = "01"
    # elif ans == 2:
    #     ans = "02"
    # elif ans == 3:
    #     ans = "03"
    # elif ans == 4:
    #     ans = "04"
    # elif ans == 5:
    #     ans = "05"
    # elif ans == 6:
    #     ans = "06"
    # elif ans == 7:
    #     ans = "07"
    # elif ans == 8:
    #     ans = "08"
    # elif ans == 9:
    #     ans = "09"
    if ans < 10:
        print("0",end="")
    print(ans,end="")

# 空间
def space(i, n):
    a = 1
    while a <= n - i:
        a += 1
        print("  ",end="")

# 杨辉三角数
def trfun(n):
    i = j = 1
    cnt = 1
    while i <= n:
        space(i, n)
        while j <= cnt:
            trfun_ret(i, j)
            j += 1
            if (j != cnt+1):
                print("  ",end="")
        print()
        j = 1
        i += 1
        cnt += 1

#主函数
trfun(n)
