import Reporter
import numpy as np
from Initialisation import Initialisation
from Parameters import Parameters
from TravellingSalesMan import TravellingSalesMan

# Modify the class name to match your student number.
class r0799028:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		parameters = Parameters()

		initialisation = Initialisation(distanceMatrix, parameters.get_population_size())
		population = initialisation.get_initial_population()

		tsm = TravellingSalesMan(distanceMatrix, parameters)

		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			# float, float, np.array
			meanObjective, bestObjective, bestSolution = tsm.run(population)

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
