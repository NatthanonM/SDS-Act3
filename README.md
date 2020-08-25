# SDS-Act3

# Activity 3: Storage system performance

The goal of this activity is to understand which storage systems have better performance and why.
Many of the storage systems we test in this activity are software-defined storage systems, thus their
performance is tightly related to their software-based implementations and protocols.

You will write 2 short programs (test_fs.py and test_s3.py) to test the storage performance on
several storage systems. Both programs will perform similar tasks. The programs will differ only
by their implementation of read and write on the target storage systems. That is, both programs will
- read a set of random bytes "r" to memory from a specified file "source_data" (read once)
- loop "n" times writing the same "r" bytes to "n" differently named files on the target storage
  - each loop requires performing open, write, and close file system operations
- the target storage systems are file system (test_fs.py) and Amazon S3 (test_s3.py).
- measure how long it takes to perform the write task in seconds. make sure you log the time
right before you start the loop and end the loop. the program can simply get the current time
by either calling
  - time.time_ns() on Python 3.7+ for Windows or
  - time.time() on older versions of Python for other OS'es
  
# Write test_fs.py
Your program should take 2 arguments
- the source_data filename containing the random bytes
- the number of iterations to write new files
You may use typical file system operations such as open, read, write, and close.

# Write test_s3.py
You will need to set up your credentials according to this link:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
(we will do this together in class).

Your program should take 2 arguments
- source_data, the filename containing the random bytes
- n, the number of iterations to write new files

You may use the AWS SDK for Python called boto3. To start, first install it using on your
notebook
```pip install boto3```
or on EC2
```sudo pip install boto3```

Code snippets of how to use boto3 for S3 are at
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

# Running experiments
You will run your code under 6 scenarios and record the time it takes to complete these tasks:
1. Run test_fs.py to test EBS on an Amazon EC2 t2.micro instance, using the source data
file "random_small.txt", and n=300 iterations.
2. Run test_fs.py to test EBS on an Amazon EC2 t2.micro instance, using the source data
file "random_large.txt", and n=3 iterations.
3. Run test_s3.py to test S3 from an Amazon EC2 t2.micro instance in the same region,
using the source data file "random_small.txt", and n=300 iterations.
4. Run test_s3.py to test S3 from an Amazon EC2 t2.micro instance in the same region,
using the source data file "random_large.txt", and n=3 iterations.
5. Run test_fs.py to test the file system on your notebook computer, using the source data file
"random_small.txt", and n=300 iterations.
6. Run test_fs.py to test the file system on your notebook computer, using the source data file
file "random_large.txt", and n=3 iterations.

Notice the difference in performance between all 6 scenarios.
