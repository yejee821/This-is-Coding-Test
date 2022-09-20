if __name__ == '__main__':

    s=input()
    alpha=s[0]
    number=int(s[1])

    # print(alpha)
    # print(number)

    x=0
    if alpha=='a':
        x=1
    elif alpha=='b':
        x=2
    elif alpha=='c':
        x=3
    elif alpha=='d':
        x=4
    elif alpha=='e':
        x=5
    elif alpha=='f':
        x=6
    elif alpha=='g':
        x=7
    elif alpha=='h':
        x=8

    y=number

    count=0

    move=[(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

    for i in range(8):
        p=x+move[i][0]
        q=y+move[i][1]

        if p<=8 and p>=1 and q<=8 and q>=1:
            count+=1

    print(count)

