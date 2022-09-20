if __name__ == '__main__':
    # N에는 0~23까지의 숫자 중 하나가 입력된다.
    N=int(input())

    num=0

    for i in range(N+1):
        for j in range(60):
            for p in range(60):
                if '3' in str(i)+str(j)+str(p):
                    num+=1

    print(num)
