from hestia_simulation import Sum

if __name__ == "__main__":
    sum_op = Sum([1, 2, 3, 4, 5])
    print(f"Sum([1, 2, 3, 4, 5]) = {sum_op.compute()}")
