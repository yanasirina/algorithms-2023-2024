class Order:
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    @property
    def summa(self):
        return self.price * self.count

    def __str__(self):
        return f"Заказ {self.code}: Цена - {self.price}, Количество - {self.count}"


class OptOrder(Order):
    @property
    def summa(self):
        base_summa = super().summa
        if self.count > 500:
            return 0.9 * base_summa
        else:
            return 0.95 * base_summa

    def __str__(self):
        return f"Оптовый заказ {self.code}: Цена - {self.price}, Количество - {self.count}"


class RetailOrder(Order):
    def __str__(self):
        return f"Розничный заказ {self.code}: Цена - {self.price}, Количество - {self.count}"


if __name__ == "__main__":
    big_opt_order = OptOrder("A001", 100, 600)
    small_opt_order = OptOrder("A001", 100, 60)
    retail_order = RetailOrder("B002", 120, 200)

    print(big_opt_order)
    print("Стоимость заказа:", big_opt_order.summa)

    print(small_opt_order)
    print("Стоимость заказа:", small_opt_order.summa)

    print(retail_order)
    print("Стоимость заказа:", retail_order.summa)
