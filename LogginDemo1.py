import logging

logging.basicConfig(filename=r"D://Naushad//SeleniumLogs//test.txt",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG
           T         )

logging.debug("This is a debug message")
logging.info("This is a info message")

logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")



