from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result = a/b
        logger.info("divide two nubers")
        return result
    except Exception as e:
        logger.error("error occured")
        raise CustomException("didivision by zero",e)
    

if __name__== "__main__":
    try:
        logger.info("starting main program")
        divide_number(10,0)
    except CustomException as c:
        logger.error(str(c))