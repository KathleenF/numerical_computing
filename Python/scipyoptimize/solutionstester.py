import scipy.optimize as opt
import numpy as np
import solutions as sol


prob2=5.488168656962328

prob3=np.array([-0.39965477, -1.21959745,  0.81994268])

prob4=np.array([0.56263117, 132.61958892, -116.26997494])



x=sol.Problem2()

if(np.allclose(prob2,x)):
	print("Problem2 Passed")
else:
	print("Problem2 Falied")
	print("Your answer:")
	print(x)
	print("Correct answer:")
	print(prob2)

x=sol.Problem3()

if(np.allclose(prob3,x)):
	print("Problem3 Passed")
else:
	print("Problem3 Falied")
	print("Your answer:")
	print(x)
	print("Correct answer:")
	print(prob3)

x=sol.Problem4()

if(np.allclose(prob4,x)):
	print("Problem4 Passed")
else:
	print("Problem4 Falied")
	print("Your answer:")
	print(x)
	print("Correct answer:")
	print(prob4)