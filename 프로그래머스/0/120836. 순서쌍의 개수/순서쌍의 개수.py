def solution(n):
    answer = 0
    # 주어진 수가 곱의 순서쌍인 경우의 수를 result로 반환
    # 순서쌍이라고 표현이 되어있지만 해당 수의 약수의 개수를 구하면 된다. 그것들의 짝궁들이 각자 다 알아서 있을테니
    for i in range(1, n+1):
        if n % i == 0:
            print('이 수는 약수')
            answer += 1
    return answer