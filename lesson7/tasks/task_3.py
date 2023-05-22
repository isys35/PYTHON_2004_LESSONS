#  C · 1,8 + 32
MAX_CELSIUS = 100
STEP = 10
TABLE_HEADER = ["Градусы Цельсия", "Градусы по Форенгейту"]


table = ["    ".join(TABLE_HEADER)]

print(table)
for celsius in range(0, MAX_CELSIUS + STEP, STEP):
    forenheit = int(celsius * 1.8 + 32)
    table.append("   ".join([str(celsius), str(forenheit)]))
    print(table)


print("\n".join(table))