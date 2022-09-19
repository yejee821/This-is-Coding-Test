# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    NMK=input()
    NMK=list(map(int,NMK.split()))

    # N=자연수들의 개수
    N=NMK[0]

    # M=숫자가 더해지는 횟수
    M=NMK[1]

    # K=연달아 더해질 수 있는 최대 횟수
    K=NMK[2]

    num=input()

    num=list(map(int,num.split()))

    #num에는 N개의 자연수들이 적혀있다.

    # N개의 자연수들을 가장 큰 순서대로 출력

    # N개의 숫자들을 큰 순서대로 정렬한다
    num.sort(reverse=True)

    # 6,5,4,4,2가 출력된다
    # print(num)

    add=0

    if num[0]!=num[1]:
        quit = 0
        while(quit!=M):
            for i in range(K):
                add+=num[0]
                quit+=1
            add+=num[1]
            quit+=1
            # if quit==M:
            #    break

    if num[0]==num[1]:
        quit=0
        while(quit!=M):
            for i in range(K-1):
                add+=num[0]
                quit+=1
            for i in range(K-1):
                add+=num[1]
                quit+=1

    print(add)


# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
