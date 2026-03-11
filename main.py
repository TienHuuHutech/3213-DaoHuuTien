def sum_two_numbers(a, b):
    return a + b

def main():
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    
    result = sum_two_numbers(a, b)
    print("Tổng của a và b là:", result)

if __name__ == "__main__":
    main()