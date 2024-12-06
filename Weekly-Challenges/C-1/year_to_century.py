def yearToCentury(year: int) -> int:   
    return round(year / 100)

if __name__ == "__main__":
    try:
        year = int(input("Year: "))
        print(yearToCentury(year))
    except ValueError:
        print("Year has to be a number")