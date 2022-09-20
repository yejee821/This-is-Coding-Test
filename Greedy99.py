if __name__ == '__main__':

    # N을 사용자에게 입력받는다.
    NK=input()
    NK=list(map(int,NK.split()))
    N=NK[0]
    K=NK[1]

    count=0

    while N>=K:
        while N%K!=0:
            N-=1
            count+=1
        N=N/K
        count+=1

    while N>1:
        N-=1
        count+=1


    print(count)

