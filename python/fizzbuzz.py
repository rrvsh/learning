for numberToEvaluate in range(1, 101): # 101 is inclusive
    buffer = ""
    if numberToEvaluate % 3 == 0:
        buffer += "Fizz"
    if numberToEvaluate % 5 == 0:
        buffer += "Buzz"
    if numberToEvaluate % 7 == 0:
        buffer = "Bazz" # We overwrite here since we don't want to combine it.
    if buffer == "":
        print numberToEvaluate
    else:
        print buffer
