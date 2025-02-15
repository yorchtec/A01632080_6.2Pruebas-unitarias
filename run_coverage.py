import unittest
import coverage

# Start coverage measurement
cov = coverage.Coverage()
cov.start()

# Import the test modules
import test_hotel
import test_customer
import test_reservation

# Run the tests
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_hotel))
suite.addTests(loader.loadTestsFromModule(test_customer))
suite.addTests(loader.loadTestsFromModule(test_reservation))

runner = unittest.TextTestRunner()
runner.run(suite)

# Stop coverage measurement and save the report
cov.stop()
cov.save()

# Report the coverage
cov.report()