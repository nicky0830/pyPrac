colwidth = 61
rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}
# dictionary를 이용해서 사용할 생각 못함

half = colwidth // 2
line = '0' * half + '1' + '0' * half
print(line)

while line[1] == '0':
    prev = line
    # 이전 기준으로 새로운 line 만들 때 이렇게 넣어서 새로 사용
    line = '0' * colwidth
    # 기준
    for i in range(1, colwidth - 1):
        # 하나씩 돌면서 바꾸기
        line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
    print(line)
    