def sum_two_numbers(a, b):
    return a + b

def main():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    
    result = sum_two_numbers(a, b)
    print("Tổng của a và b làa:", result)

if __name__ == "__main__":
    main()