import numpy as np

def linevo(operator, initial_probabilistic_state, n_iterations):
    '''
    A function that calculates the final probabilistic state of a given classical 
    random experiment.
    operator: any valid probabilistic operator representing the experiment
    n_iterations: number of times the experiment is conducted
    initial_probabilistic_state: initial probabilistic state of the experiment
    
    return: final probabilistic state of the experiment after multiple applications of the operator
    '''
    # Initialize the final probabilistic state
    final_probabilistic_state = initial_probabilistic_state

    # Apply the operator n_iterations times
    for _ in range(n_iterations):
        final_probabilistic_state = operator @ final_probabilistic_state

    return final_probabilistic_state

# testing the function
A = np.array([[0.25, 0.25, 0.25, 0.25],
              [0.25, 0.25, 0.25, 0.25],
              [0.25, 0.25, 0.25, 0.25],
              [0.25, 0.25, 0.25, 0.25]])

initial_state = np.array([1, 0, 0, 0])

q = 3
final_state = linevo(A, initial_state, q)

# asserting that the final state is correct
correct_final_state = A @ A @ A @ initial_state

assert np.allclose(final_state, correct_final_state)
print('Test passed!')
print()
print(final_state) 