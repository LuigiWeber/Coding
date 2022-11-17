import ex3

points = 0

#Test 1
try:
    assert ex3.GetPositions("Abba",'a') == [0,3]
    points += 2
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    assert ex3.GetPositions("1996", '9') == [1,2]
    points += 2
except:
    print("Test 2 failed")
    points += 0

#Test 3
try:
    assert ex3.GetPositions([0,0], 9) == False
    points += 2
except:
    print("Test 3 failed")
    points += 0

print("You got: " + str(points) + "/6 points")