Q = int(input())

list_n = []

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
      list_n.append(query[1])
    else:
      k = int(query[1])
      list_str = []
      for i in range(1,k+1):
        if i > len(list_n):
          break
        list_str.append(list_n[-i])
      print(' '.join(list_str))