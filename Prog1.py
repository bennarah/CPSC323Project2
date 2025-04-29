def trace_input(input_string, alphabet, end_marker='$'):
    print(f"Tracing input: {input_string}")
    print(f"Allowed alphabet (excluding end marker): {alphabet}")
    print("-" * 50)

    if not input_string.endswith(end_marker):
        print(f"Error: String must end with '{end_marker}'!")
        return

    # Remove the end marker for tracing
    core_string = input_string[:-1]

    for index, char in enumerate(core_string):
        if char in alphabet:
            print(f"Character {index}: '{char}' -> OK (in alphabet)")
        else:
            print(f"Character {index}: '{char}' -> NOT OK (NOT in alphabet)")

    print(f"End marker '{end_marker}' found -> OK")

# Example usage
alphabet = {'i', '+', '-', '*', '/', '(', ')'}
input_string = input("Enter a string: ")  # Example: (i+i)*i$
trace_input(input_string, alphabet)
