def main():
    n, q = (int(s) for s in input().split())
    ht_list = []
    for i in range(q):
        h ,t = input().split()
        ht_list.append((h, int(t)))
    hands = {"L": 1, "R": 2}
    ans = 0
    
    for h, t in ht_list:
        l = hands["L"]
        r = hands["R"]

        if hands[h] == t:
            continue
        elif (l > t  > r) or (r > t  > l): # 両手の間に移動先がある場合
            ans += int(abs(t - hands[h]))
        elif (t > l and t > r): # 両手よりも移動先の数字が大きい場合
            if l > r:
                if h == "L":
                    ans += t - l
                else:
                    ans += (hands[h] - 1) + 1 + (n - t)
            else:
                if h == "R":
                    ans += t - r
                else:
                    ans += (hands[h] - 1) + 1 + (n - t)
        elif (l > t and r > t):
            if l > r:
                if h == "L":
                    ans += (n - hands[h]) + 1 + (t - 1)
                else:
                    ans += r - t
            else:
                if h == "R":
                    ans += (n - hands[h]) + 1 + (t - 1)
                else:
                    ans += l - t
        
        hands[h] = t
    print(ans)

if __name__ == "__main__":
    main()
