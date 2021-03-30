def print_array(ar):
    print(f'[{ar[0]}', end = '')
    for i in range(1, len(ar)):
        print(f', {ar[i]}', end = '')
    print(']')

def main():
    n = int(input())
    ar = []
    
    for _ in range(n):
        command = input().split()
        
        if command[0] == 'insert':
            nums = [int(i) for i in command[1:]]
            ar.insert(nums[0], nums[1])
        elif command[0] == 'print':
            print_array(ar)
        elif command[0] == 'remove':
            nums = int(command[1])
            ar.remove(nums)
        elif command[0] == 'append':
            nums = int(command[1])
            ar.append(nums)
        elif command[0] == 'sort':
            ar.sort()
        elif command[0] == 'pop':
            ar.pop()
        elif command[0] == 'reverse':
            ar.reverse()
    

if __name__ == '__main__':
    main()