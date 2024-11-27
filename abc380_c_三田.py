def main():
    n, k = (int(i) for i in input().split(" "))
    s = input()
    prev_c = None
    c_list = []
    c_set = ""
    
    for c in s:
        if prev_c is None:
            c_set = c
            prev_c = c
            continue
        elif prev_c == c:
            c_set += c
            prev_c = c
            continue
        c_list.append(c_set)
        c_set = c
        prev_c = c
    c_list.append(c_set)
    
    one_cou = 0
    replace_target = None
    for i, char in enumerate(c_list):
       if "1" in char:
           one_cou += 1
           if k == one_cou:
               replace_target = i
               break
    
    c_list[replace_target-1], c_list[replace_target] = c_list[replace_target], c_list[replace_target-1]
    print("".join(c_list))
    
if __name__ == "__main__":
    main()
