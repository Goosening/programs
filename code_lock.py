nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
code = []

def main():
    def check_conditions():
        if len(code) == 4:
            if code[0] % 2 == 0 and code[3] < 5:
                if sum(code) == 21:
                    return True

    def brute_force():
        for i in nums:
            for j in nums:
                for k in nums:
                    for l in nums:
                        code.append(i)
                        code.append(j)
                        code.append(k)
                        code.append(l)
                        if check_conditions():
                            print(f"code found: {code}")
                        code.clear()
    brute_force()

if __name__ == "__main__":
    main()