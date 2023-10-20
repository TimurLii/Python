strs = ["flower", "flow", "flight"]
ans = ""
for i in strs:
    for j in i:
        if j == i:
            ans += i
    print(ans)
