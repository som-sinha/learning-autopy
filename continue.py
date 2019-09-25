# Continue skips anything after it and starts the next iteration of the loop

count = 0

while count < 5:
    count = count + 1
    if count == 3:
        continue
    print('count is ' + str(count))
print('Fin.')
