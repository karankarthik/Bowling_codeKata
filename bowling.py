def bowling_score(rolls):
    total = 0 #Total score
    pins = 0 #Pins knocked down
    ball = 0 
    frames = 0
    upcoming_rolls = []

    for roll in rolls:
        total += roll
        pins += roll
        ball += 1

        if upcoming_rolls:
            total += sum(roll for _ in range(len(upcoming_rolls)))
            upcoming_rolls = [x -1 for x in upcoming_rolls if x > 1] # will subtract the balls after counted for bonus

        if pins == 10: #if strike
            upcoming_rolls.append(2)
            pins = 0 #Pins get reset
            ball = 0 #Ball gets reset
            frames += 1 #goes to next frame

        elif ball == 2:
            if pins == 10:
                upcoming_rolls.append(1)
            pins = 0 #Pins get reset
            ball = 0 #Ball gets reset
            frames += 1 #Frame is incremented

    return total, ball, frames