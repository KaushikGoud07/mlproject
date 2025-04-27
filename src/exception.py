import sys
#import logger, logging

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details, and returns a formatted string with the error message.
    """
    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    #exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    

    return error_message

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It takes an error message and its details, and formats them using the error_message_detail function.
    """
    def __init__(self, error_message, error_detail: sys):
        #The : sys type hint indicates that the error_detail argument is expected to be an instance of the sys module
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
