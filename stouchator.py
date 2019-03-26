from modules import logger, fileoperations, config
import os
import shutil
import time

# Start logger
log = logger.setup_custom_logger('stouchator')
log.info('Starting new run')

# Create queue ready for input
ocrqueue = fileoperations.FileQueue()

# Load configuration with paths to folders
configuration = config.ConfigurationProperties()


# Load all files in input folder to queue
# TODO create limit to prevent clogging
# TODO add multithreading so files can be done simultaneously with ocr process
for file in os.listdir(configuration.getinputdir()):
    ocrfile = fileoperations.OcrFile(file, configuration.getinputdir())
    ocrqueue.enqueue(item=ocrfile)

# start processing until queue is is empty
while ocrqueue.isempty() is False:
    currentitem = ocrqueue.getfront()
    log.info('Sending {} to OCR input'.format(ocrqueue.getfront().name))
    shutil.copy(currentitem.fullpath(), configuration.getocrinput())

    timer_start = time.time()
    log.info('Waiting for OCR to finish')
    # wait until the file is done before loading another
    while currentitem.name not in os.listdir(configuration.getocroutput()):
        time.sleep(2)
        # TODO prevent waiting too long for ocr to finish
    timer_stop = time.time()
    elapsedtime = round(timer_stop-timer_start, 2)
    log.info('Done, total time elapsed: {}'.format(elapsedtime))

    # update item path and make backup
    currentitem.path = configuration.getocroutput()
    shutil.copy(currentitem.fullpath(), configuration.getoutputdir())
    ocrqueue.dequeue()

print('Run finished...')
