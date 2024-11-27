def main():
    n = input()
    
    for i in range(1, 4):
        if i != n.count(str(i)):
            print("No")
            return
    
    print("Yes")

if __name__ == "__main__":
    main()
