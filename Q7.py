students = ["Alice", "Bob", "Charlie", "David", "Eva"]

for i in range(3):
    name = input("Enter a student name: ")
    
    if name in students:
        print(f"✅ Student {name} is enrolled.")
    else:
        print(f"❌ Student {name} is not found.")
