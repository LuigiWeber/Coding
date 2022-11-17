import ex4

points = 0

#Test 1
try:
    assert ex4.isHarshad(209) == True
    points += 2
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    assert ex4.isHarshad(12255) == True
    points += 2
except:
    print("Test 2 failed")
    points += 0

#Test 3
try:
    assert ex4.isHarshad(41) == False
    points += 2
except:
    print("Test 3 failed")
    points += 0

print("You got: " + str(points) + "/6 points")