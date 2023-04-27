# BOJ-STS-
백준/ 단계별로 풀어보기 / https://www.acmicpc.net/step

## 새로 알게된 것, 모르는 것 정리

- 배열의 insert() 함수의 경우 데이터가 없다면, pos는 자동으로 맨 끝의 index가 할당되게 된다.

- reverse()함수의 경우 리스트 자체를 반환 시키며, None을 리턴한다.
  - 예시
    - a.reverse()를 하게되면 a를 호출시 뒤집힌 list를 반환
    
- reverse()는 배열에만 적용가능하다.

- reversed() 함수는 역순으로 변환한 메소드를 반환하며, 딕셔너리, 집합, 튜플 등 폭넓게 사용가능하다.
  - 예시
    - a = reversed(a) 역순으로 정렬된 리스트를 반환
    
- 리스트의 문자열을 함치거나 하고싶은 경우 .join()함수를 이용
  - 예시
    - "".join([a,b,c]) -> abc
