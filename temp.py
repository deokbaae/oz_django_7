
# 하위호환성

def add_ints(a: int, b: int, c: int = 0) -> int:
    return a + b + c


# 클라이언트 코드
print(add_ints(1, 3))  # 결과는? 4

# 에러의 타입은?

