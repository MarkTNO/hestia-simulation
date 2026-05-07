from hestia_simulation import Add

if __name__ == "__main__":
    add_op = Add(2, 3)
    print(f"Add(2, 3) = {add_op.compute()}")
