ABCs = [int(input()) for i in range(3)]
sort = sorted(ABCs)[::-1]
for ABC in ABCs:
    print(sort.index(ABC)+1)