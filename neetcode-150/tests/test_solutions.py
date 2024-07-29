import unittest
import importlib
import os
import inspect

class TestLeetCodeSolutions(unittest.TestCase):
    def test_solutions(self):
        solutions_dir = os.path.join(os.path.dirname(__file__), '..', 'solutions')
        for filename in os.listdir(solutions_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f'solutions.{filename[:-3]}'
                solution_module = importlib.import_module(module_name)
                solution_class = getattr(solution_module, 'Solution')
                
                # Get test cases for this solution
                test_cases = self.get_test_cases(filename[:-3])
                
                for test_case in test_cases:
                    solution = solution_class()
                    # Find the first method in the Solution class that isn't a magic method
                    method_name = next(name for name, func in inspect.getmembers(solution_class) 
                                       if callable(func) and not name.startswith('__'))
                    method = getattr(solution, method_name)
                    
                    # Ensure method is callable
                    if not callable(method):
                        self.fail(f"Method '{method_name}' in {filename} is not callable")
                    
                    inputs = test_case[0]
                    expected_output = test_case[1]
                    
                    if expected_output == "ERROR":
                        # We expect an error, but don't care about the specific message
                        with self.assertRaises(Exception):
                            if isinstance(inputs, tuple):
                                method(*inputs)
                            else:
                                method(inputs)
                    else:
                        try:
                            # Unpack the input tuple if it's a single element
                            if isinstance(inputs, tuple) and len(inputs) == 1:
                                inputs = inputs[0]
                            result = method(inputs)
                        except Exception as e:
                            self.fail(f"Unexpected error in {filename}: {str(e)}")
                        else:
                            self.assertEqual(result, expected_output, 
                                             f"Failed test case for {filename}: method={method_name}, "
                                             f"inputs={inputs}, expected={expected_output}, got={result}")

    def get_test_cases(self, problem_name):
        # Define test cases for each problem
        test_cases = {
            '217': [
                (([1,2,3,1]), True),
                (([1,2,5,7,89328, 989, 898,2,34,5,6,1,92,9374,75783,3892,8374,883,74,475,75]), True),
                (([1,1,1,1,1,1,1,1,1,1]), True),
                (([20009,20009,3,1]), True),
                (([1]), False),
                (([1,2,3,4]), False),
                (([1,2,3,3748]), False),
                (([]), "ERROR"),  # We expect an error, but don't specify the message
                (([0] * 100001), "ERROR"),  # We expect an error, but don't specify the message
            ],
            # Add more test cases for other problems
        }
        return test_cases.get(problem_name, [])

if __name__ == '__main__':
    unittest.main()