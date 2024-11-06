import Reporter
import numpy as np
from Initialisation import Initialisation
from Parameters import Parameters
from TravellingSalesMan import TravellingSalesMan
import time
# Modify the class name to match your student number.
class r0799028:

	def __init__(self):
		filename = 'parameters.yaml'
		self.parameters = Parameters(filename)	
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()
		start_time = time.time()
		initialisation = Initialisation(self.parameters.get_population_size(), distanceMatrix)
		population = initialisation.get_initial_population(distanceMatrix)
		print(f"Init time run: {time.time() - start_time}")

		tsm = TravellingSalesMan(self.parameters, distanceMatrix)

		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			# float, float, np.array
			start_time = time.time()
			meanObjective, bestObjective, bestSolution = tsm.run(distanceMatrix, population)
			print(f"One cycle of tsm time run: {time.time() - start_time}")
			# Call the reporter with:
			#  - the mean objective function value of the population
			#  - the best objective function value of the population
			#  - a 1D numpy array in the cycle notation containing the best solution 
			#    with city numbering starting from 0
			timeLeft = self.reporter.report(meanObjective, bestObjective, bestSolution)
			if timeLeft < 0:
				break

		# Your code here.
		return 0

if __name__ == "__main__":
	student = r0799028()
	student.optimize("tour50.csv")