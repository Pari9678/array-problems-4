print("TARGET TRACKER LAB")

numbers = [1, 3, 5, 2, 2, 5, 1]
print("PART 1: Main Array")
print("Array:", numbers)

print("PART 2: Slices and Sums")
index = 3
left_side = numbers[:index]
right_side = numbers[index + 1:]
print("Left Side:", left_side)
print("Left Sum:", sum(left_side))
print("Right Side:", right_side)
print("Right Sum:", sum(right_side))

print("PART 3: Left-Right Balance")
for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    print("Index:", i, "| Left Sum:", left_sum, "| Right Sum:", right_sum)

print("PART 4: Equilibrium Point")
found = False
for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    if left_sum == right_sum:
        print("Equilibrium Point Found at Index:", i)
        found = True
if not found:
    print("No Equilibrium Point Found")

print("PART 5: Subarray Window")
for end in range(1, len(numbers) + 1):
    window = numbers[:end]
    print(
        "Window:", window,
        "| Sum:", sum(window)
    )

print("PART 6: Target Sum Search")
target = 10
found = False
for start in range(len(numbers)):
    for end in range(start + 1, len(numbers) + 1):
        current_subarray = numbers[start:end]
        if sum(current_subarray) == target:
            print("Target Found!")
            print("Subarray:", current_subarray)
            print("Sum:", target)
            found = True
if not found:
    print("No Subarray Found with Sum =", target)

print("TARGET TRACKER LAB SUMMARY")
print("Arrays can be sliced into smaller sections.")
print("Left and right sums help find balance points.")
print("An equilibrium point has equal left and right sums.")
print("A subarray window grows step by step.")
print("Target sums can be found using nested loops.")