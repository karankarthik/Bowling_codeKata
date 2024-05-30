def bowling_score(rolls):
    total = 0
    pins = 0
    ball = 0
    frames = 0

    for roll in rolls:
        total += roll
        pins += roll
        ball += 1

        if pins == 10:
         frames += 1
         pins = 0
         ball = 0
        elif ball == 2:
             ball = 0
             frames += 1
             pins = 0 

    return total, ball, frames

