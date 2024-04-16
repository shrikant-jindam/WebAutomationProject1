import logging

class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename="C:\\Users\\Admin\\PycharmProjects\\WebAutomationProject1\\Logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',force=True)
        print(logging)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
