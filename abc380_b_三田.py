def main():
    s = input()
    ans = ""
    
    s_split = s.split("|")
    
    for s_ in s_split[1:-1]:
        ans += str(len(s_)) + " "
    
    print(ans[:-1])

if __name__ == "__main__":
    main()
