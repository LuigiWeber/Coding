import ex5

points = 0

#Test 1
try:
    assert ex5.VowelSum("Do I get the correct output?") == 10
    points += 2
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    assert ex5.VowelSum("Neon Genesis Evangelion") == 21
    points += 2
except:
    print("Test 2 failed")
    points += 0

#Test 3
try:
    assert ex5.VowelSum("You are a pirate!") == 19
    points += 2
except:
    print("Test 3 failed")
    points += 0

print("You got: " + str(points) + "/6 points")