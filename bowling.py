def bowling_score(rolls):
    total = 0 # Total score
    pins = 0 # Pins knocked down
    ball = 0 # Ball counter
    frames = 0 # Frame counter
    upcoming_rolls = []

    for roll in rolls:
        total += roll
        if upcoming_rolls:
            total += roll * len(upcoming_rolls)
            upcoming_rolls = [x -1 for x in upcoming_rolls if x > 1]

        pins += roll
        ball += 1

        # if frames < 10 and (pins == 10 or ball == 2):  # Strike or end of frame
        #     if pins == 10:  # Strike
        #         upcoming_rolls.append(2 if ball == 1 else 1)  # Add bonus for strike or spare
        #     pins = 0
        #     ball = 0
        #     frames += 1

        # # elif frames == 10:
        # #     if ball == 1 and pins == 10:
        # #         pins = 0
        # #     elif ball == 2:
        # #         if pins == 10:
        # #             pins = 0
        # #             # ball = 0
        # #         elif ball == 3:
        # #             ball = 0

        # elif frames == 10:
        #     if ball < 1 and pins == 10:
        #         pins = 0
        #         upcoming_rolls.append(2 if ball == 1 else 0)
        #         print(ball)
        #     elif ball == 2:
        #         if pins == 10:
        #             pins = 0
        #             upcoming_rolls.append(1 if ball == 2 else 0)
        #             print(ball)
        #         elif ball == 3:
        #             ball = 0
        #             print(ball)

        if frames <= 9:  # Frames 1-9
            if pins == 10:  # Strike or spare
                upcoming_rolls.append(2 if ball == 1 else 1)
                pins = 0
                ball = 0
                frames += 1
            elif ball == 2:  # End of frame
                pins = 0
                ball = 0
                frames += 1
        else:  # Frame 10
            if ball == 1 and pins == 10:  # Strike
                pins = 0
                upcoming_rolls.append(2)
            elif ball == 2:
                if pins == 10:  # Spare
                    pins = 0
                    upcoming_rolls.append(1)
                elif ball == 3:  # End of frame
                    ball = 0
                    pins = 0
                    frames += 1

        if frames == 10 and ball == 3:
            break

        # 10th frame outcomes
        # User input -> error handling

    return total, ball, frames