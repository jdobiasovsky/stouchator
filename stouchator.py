#!/usr/bin/python
"""
Python script for loading large batches of documents to OCR recogniton server.

No extra libraries needed, tested on python 3.7.1
You can specify input and output paths into config.json file. See sample.
"""

import os
import shutil
import time
from modules import logger, fileoperations, config


def main():
    """Create a queue and oversees picking up finished ocr."""
    # Start logger
    log = logger.setup_custom_logger('stouchator')
    log.info('Starting new run')

    # Create queue ready for input
    ocrqueue = fileoperations.FileQueue()
    log.info('Started a new queue')

    # Load configuration with paths to folders
    configuration = config.ConfigurationProperties()

    # Load all files in input folder to queue
    # TODO create limit to prevent clogging
    # TODO add multithreading so files can be done simultaneously with ocr
    for file in os.listdir(configuration.getinputdir()):
        ocrfile = fileoperations.OcrFile(file, configuration.getinputdir())
        ocrqueue.enqueue(item=ocrfile)

    # start processing until queue is is empty
    while ocrqueue.isempty() is False:
        currentitem = ocrqueue.getfront()
        log.info('Sending %s to OCR input', ocrqueue.getfront().name)
        shutil.copy(currentitem.fullpath(), configuration.getocrinput())

        timer_start = time.time()
        log.info('Waiting for OCR to finish')
        # wait until the file is done before loading another
        while currentitem.name not in os.listdir(configuration.getocroutput()):
            time.sleep(2)
            timer_stop = time.time()
            if (timer_stop-timer_start) > 1200:
                log.warning('File %s is taking too long to finish',
                            ocrqueue.getfront().name)
                log.warning('Assuming server error or out of license.')
                exit()

        timer_stop = time.time()
        elapsedtime = round(timer_stop-timer_start, 2)
        log.info('Done, total time elapsed: %s', elapsedtime)

        # update item path and make backup
        currentitem.path = configuration.getocroutput()
        shutil.copy(currentitem.fullpath(), configuration.getoutputdir())
        ocrqueue.dequeue()

    print('Run finished...')


if __name__ == '__main__':
    main()
