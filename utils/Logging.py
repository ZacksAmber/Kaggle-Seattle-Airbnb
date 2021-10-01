import logging
import functools
import os

def Logging(logfile=None):
    """Custom logging function.
    
    Args:
        logfile: The name of log files. Log will be stored in logs_dir.
    
    Returns:
        The same output of the call function with logging information.
    """
    # Create logs_dir if the directory logs is not exist.
    logs_dir = 'logs'
    if os.path.isdir(logs_dir) is False:
        os.mkdir(logs_dir)
    
    def Logging_decorator(func):
        # Define logger, set the logger name as func.__name__
        logger = logging.getLogger(func.__name__) # run logger.name to check
        
        # Set level for logger
        logger.setLevel(logging.DEBUG)

        # Define the handler and formatter for console logging
        consoleHandler = logging.StreamHandler() # Define StreamHandler
        consoleHandler.setLevel(logging.DEBUG) # Set level
        concolsFormatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s') # Define formatter
        consoleHandler.setFormatter(concolsFormatter) # # Set formatter
        logger.addHandler(consoleHandler) # Add handler to logger
        
        # Define the handler and formatter for file logging
        if logfile is not None:
            fileHandler = logging.FileHandler(f'{logs_dir}/{logfile}.log') # Define FileHandler
            fileHandler.setLevel(logging.WARNING) # Set level
            fileFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Define formatter
            fileHandler.setFormatter(fileFormatter) # Set formatter
            logger.addHandler(fileHandler) # Add handler to logger
        
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            # Before running func
            #logger.debug(f"{func.__name__} - {args} - {kwargs}")
            logger.debug(f"{func.__name__}({args}, {kwargs})")
            
            try:
                output = func(*args,**kwargs)
            except:
                logger.exception(f"{func.__name__}({args}, {kwargs})")

            # After running func

            return output
        return wrapper_decorator
    return Logging_decorator