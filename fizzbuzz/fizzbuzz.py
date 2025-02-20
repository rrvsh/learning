for n in range(100):
    numberToEvaluate = n + 1
    if numberToEvaluate % 3 == 0 and numberToEvaluate % 5 == 0:
        print "FizzBuzz"
    elif numberToEvaluate % 3 == 0:
        print "Fizz"
    elif numberToEvaluate % 5 == 0:
        print "Buzz"
    else:
        print numberToEvaluate
