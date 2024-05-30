def bowling_score(rolls):
    total = 0
    pins = 0
    ball = 0
    frames = 0

    for roll in rolls:
        pins += roll
        total += roll
        ball += 1
        
        if pins == 10:
         ball = 1
         frames += 1
        elif ball == 2:
             ball = 0
             frames += 1
             pins = 0
        else:
            total += pins 

    return total, ball, frames

