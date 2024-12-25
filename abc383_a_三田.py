def main():
    n = int(input())
    t_v_list = [[int(a) for a in input().split()] for _ in range(n)]
    
    water = 0
    pre_time = 0
    
    for i, t_v in enumerate(t_v_list):
        if i == 0:
            water += t_v[1]
            pre_time = t_v[0]
            continue
        if water < t_v[0] - pre_time:
            water = 0
        else:
            water -= t_v[0] - pre_time
        water+= t_v[1]
        pre_time = t_v[0]
    
    print(water)

if __name__ == "__main__":
    main()
