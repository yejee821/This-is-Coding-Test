# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    size=int(input())

    move=input()
    move=list(move.split())

    # move의 개수만큼 for문 실행

    l=1
    r=1
    for i in range(len(move)):
       if move[i]=='L':
           if(r==1):
               pass
           else:
                r-=1
       elif move[i]=='R':
            if(r==size):
                pass
            else:
                r+=1
       elif move[i]=='U':
            if(l==1):
                pass
            else:
                l-=1
       else:
           if(l==size):
               pass
           else:
                l+=1

    print(l, r)

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
