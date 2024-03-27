def main():
    S = input().split('+')
    ans = 0
    for i in S:
        if '0' not in i:
            ans += 1
    print(ans)
            
    
if __name__ == '__main__':
    main()