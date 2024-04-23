try:
    numerator = float(input("Numerator:>"))
    denominator = float(input("denominator:>"))
    result = numerator / denominator
except ValueError as e:
    print(f"{e} occurred")
    print("Numbers only are required")
except ZeroDivisionError as e:
    print(f"{e} occurred")
    print("'0' cannot be entered as the denominator")
else:
    print(f"Result: {result:.3f}")
finally:
    print("You are always welcome")