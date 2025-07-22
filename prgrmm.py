from tabulate import tabulate
header = ["Name", "Age", "City"],
data = [["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"],
        ["Dave", 28, "Miami"]]
print(tabulate(data, headers=header, tablefmt="html"))