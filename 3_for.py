"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


sold_phones = [
    {
        "product": "iPhone 12",
        "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
    },
    {
        "product": "Xiaomi Mi11",
        "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
    },
    {
        "product": "Samsung Galaxy 21",
        "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
    },
]


def count_sold_products(items_sold):
    items_sold_sum = 0
    for sold_item in items_sold:
        items_sold_sum += sold_item
    return items_sold_sum


total_sale_sum = 0
total_avg_sum = 0
for item in sold_phones:
    sale_sum = count_sold_products(item["items_sold"])
    sale_avg = round(sale_sum / len(item.get("items_sold")), 2)
    total_sale_sum += sale_sum
    total_avg_sum += sale_avg
    print(f'суммарное количество продаж для товара {item["product"]}: {sale_sum}')
    print(f'Среднее количество продаж для товара {item["product"]}: {sale_avg}')
    print()

print(f"Общее количество проданных товаров: {total_sale_sum}")
print(f"Среднее количество продаж всех товаров: {total_avg_sum}")


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass


if __name__ == "__main__":
    main()
