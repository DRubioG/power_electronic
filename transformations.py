import numpy as np

def abc_2_ab(abc):
	mat_clarke = (2/3)*np.array([[1, -1/2,  -1/2],
								[0, np.sqrt(3)/2, -np.sqrt(3)/2]])#,
								#[1/2, 1/2, 1/2]])
	
	ab = np.matmul(mat_clarke, abc)
	return ab
	
def ab_2_abc(ab):
	mat_clarke_inv = [[1, 0, 1],
		   			  [-1/2, np.sqrt(3)/2, 1],
					  [-1/2, -np.sqrt(3)/2, 1]]
	
	abc = np.matmul(mat_clarke_inv, ab)
	
	return abc

def dq_2_ab(ab, theta):
	mat_park = [[np.cos(theta), np.sin(theta), 0],
	     		[-np.sin(theta), np.cos(theta), 0],
				[0, 0, 1]]

	dq = np.matmul(mat_park, ab)

	return dq

def ab_2_dq(dq, theta):
	mat_clark_inv = [[np.cos(theta), -np.sin(theta), 0],
		  			[np.sin(theta), np.cos(theta), 0],
					[0, 0, 1]]

	ab =np.matmul(mat_clark_inv, dq)

	return ab

def abc_2_dq(abc, theta):
	ab = abc_2_ab(abc)
	dq = dq_2_ab(ab, theta)

	return dq

def dq_2_abc(dq, theta):
	ab = dq_2_ab(dq, theta)
	abc = ab_2_abc(ab)

	return abc

