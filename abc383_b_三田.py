def main():
    h, w, d = (int(i) for i in input().split())
    s_list = [input() for _ in range(h)]
    
    max_kasitu = 0
    
    for ia in range(h):
        for ja in range(w):
            for ib in range(h):
                for jb in range(w):
                    if s_list[ia][ja] == "." and s_list[ib][jb] == ".":
                        kasitu_cou = 0
                        for i in range(h):
                            for j in range(w):
                                if s_list[i][j] == ".":
                                    if (abs(ia - i) + abs(ja - j) <= d) or (abs(ib - i) + abs(jb - j) <= d):
                                        kasitu_cou += 1
                        max_kasitu = max(max_kasitu, kasitu_cou)
    
    print(max_kasitu)

if __name__ == "__main__":
    main()
