import sys
import os
import shutil
import time


def main(args):
    if len(args) != 3:
        print("Expected 3 arguments: filename, number and result filename (received %i)" % len(args))
        exit(1)

    (filename, iteration, resultFilename) = args
    iteration = int(iteration)
    basename = os.path.splitext(filename)[0]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    writting_path = os.path.join(dir_path, basename)

    # WARNING
    print("WARNING!!")
    print("The directory: %s and its contents will be removed" % basename)
    confirm = input("Continue? (Y/n):")
    if confirm != "Y":
        exit(0)

    # Read random file
    try:
        f = open(filename, "r")
    except:
        print("Error: %s file not found" % filename)

    # Manage path
    if os.path.exists(writting_path):
        try:
            shutil.rmtree(writting_path)
        except OSError as e:
            print("Error: %s : %s" % (writting_path, e.strerror))
        finally:
            os.makedirs(writting_path)
    else:
        os.makedirs(writting_path)

    # Timer
    timestamps = []
    start = time.perf_counter_ns()

    for i in range(iteration):
        f1 = open(os.path.join(writting_path, "random_copy_%i.txt" % i), "w")
        f.seek(0)  # cursor back to the beginning
        f1.writelines(f)
        f1.close()

        diffTime = str(time.perf_counter_ns()-start)
        # Format time stamp
        if len(diffTime) > 9:
            diffTime = diffTime[:-9]+"."+diffTime[-10:]
        else:
            diffTime = "0." + diffTime.rjust(9, "0")

        timestamps.append(
            str(i) + ", " + diffTime)

    f.close()

    f = open(resultFilename, "w")
    for e in timestamps:
        f.write(e+"\n")
    f.close()

    print("Done")


if __name__ == "__main__":
    main(sys.argv[1:])
