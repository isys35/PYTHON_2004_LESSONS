TABLE_HEADER = ["Начальная цена", "Скидка", "Цена со скидкой"]
COLUMN_SPACING_LENGTH = 6
COLUMN_SPACING = " " * COLUMN_SPACING_LENGTH

discount = .6
base_prices = [4.95, 14244.95, 144444.95, 19.95, 24.95, 333333]

table = [COLUMN_SPACING.join(TABLE_HEADER), ]

for price in base_prices:
    table_row_base_price = f"{price:.2f}$"
    table_row_discount = f"{discount:.0%}"
    table_row_discount_price = f"{price - price * discount:.2f}$"

    position_discount = " " * (len(TABLE_HEADER[0]) + COLUMN_SPACING_LENGTH - len(table_row_base_price))
    position_discount_price = " " * (len(TABLE_HEADER[1]) + COLUMN_SPACING_LENGTH - len(table_row_discount))
    table_row = "".join(
        [
            table_row_base_price,
            position_discount,
            table_row_discount,
            position_discount_price,
            table_row_discount_price
        ]
    )
    table.append(table_row)

print("\n".join(table))
