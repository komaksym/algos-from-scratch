def solution(S: str) -> str:
    """
    Return the largest palindromic number that can be built from digits in S.

    Rules:
    - Use at least one digit.
    - You may reorder digits.
    - No leading zeros, except answer "0" itself.
    """

    counts = [0] * 10

    for ch in S:
        digit = int(ch)
        counts[digit] += 1

    left = []
    middle = ""

    for i in range(len(counts) - 1, -1, -1):
        while counts[i] > 1:
            left.append(str(i))
            counts[i] -= 2

        if not middle and counts[i] % 2 != 0:
            middle += str(i)

    if left and left[0] == "0":
        return "0" if not middle else middle

    return "".join(left) + middle + "".join(left[::-1])


def run_tests():
    tests = [
        ("39878", "898"),
        ("00900", "9"),
        ("0000", "0"),
        ("54321", "5"),
        ("8199", "989"),
        ("1001", "1001"),
        ("00011", "10001"),
        ("98766789", "98766789"),
        ("93333", "33933"),
    ]

    for S, expected in tests:
        got = solution(S)
        status = "OK" if got == expected else "FAIL"
        print(f"{status}: solution({S!r}) = {got!r}, expected {expected!r}")


if __name__ == "__main__":
    run_tests()
