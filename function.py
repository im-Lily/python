# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:47:48 2021

@author: jeong
"""

''' 파이썬 내장함수 '''

# dir 내장함수 목록 출력

# a가 쓸 수 있는 내장함수 목록 출력
a=3.14159283
dir(a)

b='good morning'
dir(b)

# 도움말
help(abs)

# abs() : 절댓값 반환함수
print(abs(-12))
print(abs(12))

a = [13,8,15,7,9,12]
for i in a :
    print("10과",i,"의 차이=",abs(10-i))

# max, min : 최댓값, 최솟값
d = [12, 4 , 21, 66, 98, 47]
print("최대값=",max(d))
print("최솟값=",min(d))

d = [33, 27, 45, 56, 70, 89]
a = input("값을 입력하세요")
if int(a) > max(d):
    print("가장 큰 값")
else:
    print("숫자를 높혀보세요")
    
# sum : 합계
d = [5, 12, 13, 21, 30]

''' sum을 변수로 이용
sum = 0
for i in d :
    sum=sum+i
print("합계",sum)
'''

print(sum(d)) ### python에서는 되는데 spyder환경에서 실행안됨

# eval : 문자열을 파이썬 수식으로 변환
a = input("계산식을 입력하세요")
print("계산결과",eval(a)*5)

# len : 문자열 길이 반환
a = input("값 입력")
print("입력한 문자열의 길이=",len(a))

x=['a','b','c','d','e','f']
print(len(x))

''' 사용자 정의함수 '''
# 사용자정의함수와 메인부분 매개변수 이름은 달라도 되지만 형식은 같아야함
# 직육면체 부피 계산
def mVolume(a, b, c) :
    return a*b*c

w = int(input('가로값을 입력하세요 : '))
h = int(input('세로값을 입력하세요 : '))
h2 = int(input('높이값을 입력하세요 : '))
V = mVolume(w,h,h2)
print('직육면체 부피는 %d 세제곱센티미터' %(V))














