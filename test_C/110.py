def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return

    corresponds_t = {}
    corresponds_s = {}
    for s_letter, t_letter in zip(S, T):
        if t_letter not in corresponds_t:
            corresponds_t[t_letter] = s_letter
        if s_letter not in corresponds_s:
            corresponds_s[s_letter] = t_letter
        if corresponds_t[t_letter] != s_letter:
            print("No")
            return
        if corresponds_s[s_letter] != t_letter:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
