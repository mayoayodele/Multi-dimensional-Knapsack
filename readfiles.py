import numpy as np
file_path = 'Weing//WEING8.npz'
loaded_file = np.load(file_path)
qubo_size = loaded_file['n']
objective = loaded_file['objective']
constraint = loaded_file['constraint']


def convert_1d_qubo_to_2d(qubo, n):
    if (len(qubo)!= (n) * ((n+1) * 0.5)   + 1):
        print('check that n is the correct size')
        return None, None
    constant = qubo[0]
    linear_terms = np.array(qubo[1:(n + 1)])
    no_of_quadratic_terms = len(qubo) - len(linear_terms) -1
    quadratic_terms = np.array(qubo[-no_of_quadratic_terms:])
    k = 0
    qubo_coeffs = []
    for i in range(n):
        coeffs = []
        for j in range(n):
            if(i == j):
                coeffs.append(linear_terms[i])
            elif(j>i):
                coeffs.append(quadratic_terms[k])
                k+=1
            else:
                coeffs.append(0)
        qubo_coeffs.append(coeffs)
    qubo_coeffs = np.array(qubo_coeffs)

    return qubo_coeffs, constant
    
    
    
    obj_qubo, obj_constant = convert_1d_qubo_to_2d(objective, qubo_size)
    
    con_qubo,con_constant = convert_1d_qubo_to_2d(constraint, qubo_size)
    
    
    
    