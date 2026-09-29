# DecodeLabs - Project 2: Expense Tracker
# Concept: State-Preserving Accumulator Loop

def main():
    print("=== EXPENSE TRACKER ===")
    print("Enter your expense amount (or type 'quit' to exit).\n")

    # 1. Accumulator Pattern: Total ko initialize kar rahe hain
    total_spent = 0.0

    # 2. Continuous Audit Loop: Continuous user input ke liye
    while True:
        user_input = input("Enter expense amount: ").strip()

        # 3. Sentinel Value Check: 'quit' Type karne par loop exit hoga
        if user_input.lower() == 'quit':
            break

        # 4. Input Transformation & Validation
        try:
            expense = float(user_input)
            if expense < 0:
                print("Expense amount negative nahi ho sakta. Dobara try karein.")
                continue

            # Accumulator Logic: state(new) = state(old) + input
            total_spent += expense
            print(f"Added ${expense:.2f} | Current Total: ${total_spent:.2f}\n")

        except ValueError:
            print("Invalid input! Kripya number ya 'quit' enter karein.\n")

    # 5. Output Stream: Final Summary Display
    print("\n=========================")
    print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
    print("=========================")

if __name__ == "__main__":
    main()