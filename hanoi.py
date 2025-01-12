def hanoi(n, source, x, o):
    global count 
    if n == 1:
        count += 1
        print(f"Move disk 1 from {source} to {x}")
        return
    hanoi(n - 1, source, o, x)
    count += 1
    print(f"Move disk {n} from {source} to {x}")
    hanoi(n - 1, o, x, source)

num_disks = 3 
count = 0

hanoi(num_disks, "A", "C", "B")

print(f"moves: {count}")
