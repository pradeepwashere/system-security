import math
import time
import random
import hashlib
import random
import numpy

#====================================================================

# Using the in-built Random Function
# The Mersenne Twister is a pseudorandom number generator (PRNG).
# It is by far the most widely used general-purpose PRNG.
# It was the first PRNG to provide fast generation of high-quality
# pseudorandom integers


def CreateSequence1():
    seed = GetInputSeed()								# Set Seed
    toHash = u''.join(seed).encode('utf-8')				# Perform Hash Operation
    fromHashed = hashlib.sha1(toHash)					# Use the digest obtained as the seed
    random.seed(fromHashed.hexdigest())					
    a = random.getrandbits(32217)						# Required Length of Message
    sequence1 = bin(a)[2:]
    print sequence1
    # print hello


def GetInputSeed():
    seed = raw_input("Please Input the seed")
    return seed

CreateSequence1()

#====================================================================
