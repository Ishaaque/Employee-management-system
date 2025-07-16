import os

print("Checking current folder:", os.getcwd())
print("\nListing files and folders in current directory:\n")

for root, dirs, files in os.walk(".", topdown=True):
    level = root.count(os.sep)
    indent = " " * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
