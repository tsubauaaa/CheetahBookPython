def count_strings(s):
    hm = {}
    for i in range(len(s)):
        if not s[i] in hm:
            hm[s[i]] = 0
        hm[s[i]] += 1
    for k, v in hm.items():
        print(f"{k} {v}")


# count_strings("aaabbcddd")
