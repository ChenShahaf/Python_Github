#This is example to logger
import logging

'''
DEBUG	 Detailed information, typically of interest only when diagnosing problems.

INFO	 Confirmation that things are working as expected.

WARNING	 An indication that something unexpected happened, or indicative of some problem in the near future 
         (e.g. ‘disk space low’). The software is still working as expected.

ERROR	 Due to a more serious problem, the software has not been able to perform some function.

CRITICAL A serious error, indicating that the program itself may be unable to continue running.
'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s ")

file_handler = logging.FileHandler('TestFileHandler.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logging.basicConfig(filename='ExampleLogTest.log', level=logging.DEBUG,
                    format="%(asctime)s : %(levelname)s : %(message)s "
                    )

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def divide(x,y):
    return x/y

num1 = 10
num2 = 5

add_result = add(num1,num2)
logger.info('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = sub(num1,num2)
logging.debug('Substruct: {} - {} = {}'.format(num1, num2, sub_result))

mult_result = mult(num1,num2)
logging.debug('Multiply: {} * {} = {}'.format(num1, num2, mult_result))

div_result = divide(num1, num2)
logging.debug('Divide: {} / {} = {}'.format(num1, num2, div_result))