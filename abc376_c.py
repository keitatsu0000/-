def main():
    n = int(input())
    a_list = sorted([int(a) for a in input().split()], reverse=True)
    b_list = sorted([int(b) for b in input().split()], reverse=True)
    ans = -1
    cou = 0
    j = 0

    for i, a in enumerate(a_list):
        if j == len(b_list):
            ans = a
        elif a > b_list[j]:
            ans = a
            cou += 1
            if cou > 1:
                ans = -1
                break
        else:
            j += 1

    print(ans)

if __name__ == "__main__":
    main()
