# Predictive Parsing Table based on the given grammar
parse_table = {
    'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
    'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
    'T': {'a': ['F', 'R'], '(': ['F', 'R']},
    'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
    'F': {'a': ['a'], '(': ['(', 'E', ')']}
}

terminals = ['a', '+', '-', '*', '/', '(', ')', '$']
non_terminals = ['E', 'Q', 'T', 'R', 'F']

def predictive_parse(input_string):
    stack = ['$', 'E']
    pointer = 0

    print(f"\nInput: {input_string}")
    print("-" * 50)

    while len(stack) > 0:
        top = stack.pop()
        current_input = input_string[pointer] if pointer < len(input_string) else None

        # Print the stack snapshot
        print(f"Stack: {' '.join(reversed(stack + [top]))}")
        print(f"Input Symbol: {current_input}")

        if top in terminals:
            if top == current_input:
                print(f"Action: Match '{top}'\n")
                pointer += 1
            else:
                print(f"Action: Error! Expected '{top}', got '{current_input}'")
                return "Output: String is NOT accepted (Invalid)."
        elif top in non_terminals:
            production = parse_table.get(top, {}).get(current_input)
            if production:
                if production != ['ε']:
                    for symbol in reversed(production):
                        stack.append(symbol)
                print(f"Action: Apply {top} → {' '.join(production)}\n")
            else:
                print(f"Action: Error! No rule for {top} with input '{current_input}'\n")
                return "Output: String is NOT accepted (Invalid)."
        else:
            print(f"Action: Error! Unknown symbol '{top}'")
            return "Output: String is NOT accepted (Invalid)."

    if pointer == len(input_string):
        return "Output: String is accepted (Valid)."
    else:
        return "Output: String is NOT accepted (Invalid)."

# Ask the user for input
while True:
    user_input = input("Enter a string ending with $: ").strip()

    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    # Remove all spaces before parsing
    user_input = user_input.replace(' ', '')

    if not user_input.endswith('$'):
        print("Error: String must end with '$'. Please try again.")
        continue

    result = predictive_parse(user_input)
    print(result)
    print("=" * 50)
