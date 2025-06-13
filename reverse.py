orig = "hello"
length = len(orig)
count = 0
result = ""

# 文字列を逆順にするループ
while True:
    result = orig[count] + result  # 文字を逆順に追加
    count += 1  # インデックスを増加
    if count >= length:  # インデックスが文字列の長さに達したら終了
        break

print(result)  # 出力: olleh


def reverse(s):
    result = ""
    for char in s:
        result = char + result
    return result
    
orig = "good"
result = reverse(orig)
print(result) # doog
