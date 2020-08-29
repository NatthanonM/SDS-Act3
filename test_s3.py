import sys
import time
import os
import logging
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "natthanonsdsact3"


def main(args):
    if len(args) != 3:
        print("Expected 3 arguments: filename, number and result filename (received %i)" % len(args))
        exit(1)

    (filename, iteration, resultFilename) = args
    iteration = int(iteration)
    baseFilename = ".".join((filename.strip().split("."))[:-1])

    # WARNING
    # print("WARNING!!")
    # print("The folder name \"%s\" in bucket name \"%s\" on S3 and its contents will be removed" %
    #       (baseFilename, BUCKET_NAME))
    # confirm = input("Continue? (Y/n):")
    # if confirm != "Y":
    #     exit(0)

    # Read random file from s3
    print('Reading file from s3...')
    try:
        s3 = boto3.client('s3')
        with open(filename, 'wb') as f:
            s3.download_fileobj(BUCKET_NAME, filename, f)
        f.close()
        print('Read file from s3 completed')

    except ClientError as e:
        logging.error(e)
        exit(1)

    # Timer
    timestamps = []

    # Write random file to s3
    print('Writing file to s3...')
    for i in range(iteration):
        f = open(filename, "rb")
        start = time.perf_counter_ns()
        s3.upload_fileobj(
            f, BUCKET_NAME, "%s/random_copy_%i.txt" % (baseFilename, i))

        diffTime = str(time.perf_counter_ns()-start)
        # Format time stamp
        if len(diffTime) > 9:
            diffTime = diffTime[:-9]+"."+diffTime[-10:]
        else:
            diffTime = "0." + diffTime.rjust(9, "0")

        timestamps.append(
            str(i) + ", " + diffTime)

    f.close()
    print('Write file to s3 completed')

    f = open(resultFilename, "w")
    for e in timestamps:
        f.write(e+"\n")
    f.close()

    print('Write result completed')
    print("Done")
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
