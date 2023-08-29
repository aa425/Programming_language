from simpleeval import simple_eval

# Dictionary to store variables and their values
variables = {}

# Dictionary to store user-defined functions
functions = {}

def evaluate_expression(expression):
    return simple_eval(expression, names=variables)

while True:
    input_line = input("Enter a line of code (or 'exit' to quit): ")
    
    if input_line.lower() == "exit":
        break

    tokens = input_line.split()

    if tokens[0] == "define":
        if len(tokens) >= 5 and tokens[2] == "(" and tokens[-2] == ")":
            function_name = tokens[1]
            parameters = tokens[3:-2]
            function_body = input("Enter function body: ")
            functions[function_name] = (parameters, function_body)
            print(f"Function '{function_name}' defined with parameters {parameters}")

        else:
            print("Invalid function definition syntax")

    elif tokens[0] in functions:
        function_name = tokens[0]
        function_params = functions[function_name][0]
        args = tokens[1:]
        
        if len(args) != len(function_params):
            print(f"Error: Function '{function_name}' expects {len(function_params)} arguments.")
        else:
            for i, param in enumerate(function_params):
                variables[param] = simple_eval(args[i])
            function_body = functions[function_name][1]
            lines = function_body.split("\n")
            for line in lines:
                line_tokens = line.split()
                if line_tokens[0] == "print":
                    print(" ".join(line_tokens[1:]))
                # Add more command handling as needed

    elif tokens[0] == "for":
        if len(tokens) >= 8 and tokens[2] == "in" and tokens[4] == "range":
            variable_name = tokens[1]
            start = evaluate_expression(tokens[5])
            stop = evaluate_expression(tokens[7])
            step = evaluate_expression(tokens[8]) if len(tokens) > 8 else 1

            for value in range(start, stop, step):
                variables[variable_name] = value
                for i in range(9, len(tokens)):
                    if tokens[i] in functions:
                        function_name = tokens[i]
                        args = tokens[i+1:]
                        if len(args) != len(functions[function_name][0]):
                            print(f"Error: Function '{function_name}' expects {len(functions[function_name][0])} arguments.")
                        else:
                            for j, param in enumerate(functions[function_name][0]):
                                variables[param] = simple_eval(args[j])
                            result = evaluate_expression(functions[function_name][1])
                            print(f"Function '{function_name}' result:", result)
                    else:
                        print("Unknown command or expression")
        else:
            print("Invalid 'for' loop syntax")

    elif tokens[0] == "while":
        if len(tokens) >= 3:
            condition = " ".join(tokens[1:3])
            while evaluate_expression(condition):
                for i in range(3, len(tokens)):
                    if tokens[i] in functions:
                        function_name = tokens[i]
                        args = tokens[i+1:]
                        if len(args) != len(functions[function_name][0]):
                            print(f"Error: Function '{function_name}' expects {len(functions[function_name][0])} arguments.")
                        else:
                            for j, param in enumerate(functions[function_name][0]):
                                variables[param] = simple_eval(args[j])
                            result = evaluate_expression(functions[function_name][1])
                            print(f"Function '{function_name}' result:", result)
                    else:
                        print("Unknown command or expression")
        else:
            print("Invalid 'while' loop syntax")

    elif tokens[0] == "say":
        print(" ".join(tokens[1:]))

    elif tokens[0] == "print":
        output = " ".join(tokens[1:])
        for var_name in variables:
            output = output.replace(var_name, str(variables[var_name]))
        print(output)

    elif tokens[0] == "that":
        print(" ".join(tokens[1:]))

    elif tokens[0] == "word2dec":
        word = " ".join(tokens[1:])
        decimal_value = sum(ord(char) for char in word)
        print(f"Decimal value of '{word}': {decimal_value}")

    elif tokens[0] == "set":
        variable_name = tokens[1]
        if tokens[3] in functions:
            function_name = tokens[3]
            args = tokens[4:]
            if len(args) != len(functions[function_name][0]):
                print(f"Error: Function '{function_name}' expects {len(functions[function_name][0])} arguments.")
            else:
                for j, param in enumerate(functions[function_name][0]):
                    variables[param] = simple_eval(args[j])
                result = evaluate_expression(functions[function_name][1])
                variables[variable_name] = result
                print(f"Variable '{variable_name}' assigned with value '{variables[variable_name]}'")
        else:
            variable_value = " ".join(tokens[3:])
            variables[variable_name] = evaluate_expression(variable_value)
            print(f"Variable '{variable_name}' assigned with value '{variables[variable_name]}'")

    # ... (rest of the interpreter code)
