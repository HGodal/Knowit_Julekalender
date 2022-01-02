nums = [int(line) for line in open('numbers.txt').readline().split(',')]

totalsum = ((len(nums)+1)*(len(nums)+2))//2
print(f'Tallet som mangler er {totalsum - sum(nums)}')
