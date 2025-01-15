def abc(a: bool, b: bool) -> int | None:
    if a:
        return 123
    if b:
        return 12
    return None


result = abc(True, False)
if result:
    print(456 + result)
