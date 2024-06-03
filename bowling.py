# def bowling_score(rolls):
#     total = 0 # Total score
#     pins = 0 # Pins knocked down
#     ball = 0 # Ball counter
#     frames = 0 # Frame counter
#     upcoming_rolls = []

#     for roll in rolls:
#         total += roll
#         if upcoming_rolls:
#             total += roll * len(upcoming_rolls)
#             upcoming_rolls = [x -1 for x in upcoming_rolls if x > 1]

#         pins += roll
#         ball += 1

#         if frames < 9 and (pins == 10 or ball == 2):
#             if pins == 10:
#                 upcoming_rolls.append(2 if ball == 1 else 1) 
#             pins = 0
#             ball = 0
#             frames += 1

#         # elif frames == 10:
#         #     if ball == 1 and pins == 10:
#         #         pins = 0
#         #     elif ball == 2:
#         #         if pins == 10:
#         #             pins = 0
#         #             # ball = 0
#         #         elif ball == 3:
#         #             ball = 0

#         elif frames == 9:
#             if ball == 1 and pins == 10:
#                 pins = 0
#                 upcoming_rolls.append(2)
#             elif ball == 2:
#                 if pins == 10 or sum(rolls[-3:-1]) == 10:
#                     pins = 0
#                     # ball += 1
#                     upcoming_rolls.append(1)
#                 elif ball == 3:
#                     ball = 0

#     return total, ball, frames

def bowling_score(rolls):
    total = 0
    pins = 0
    ball = 0
    frames = 0
    upcoming_rolls = []

    for i, roll in enumerate(rolls):
        total += roll
        if upcoming_rolls:
            if frames < 9:
                total += roll * upcoming_rolls[0]
                upcoming_rolls = upcoming_rolls[1:]
            else:
                upcoming_rolls.append(2 if ball == 1 else 1)

        pins += roll
        ball += 1

        if frames < 9 and (pins == 10 or ball == 2):
            if pins == 10:
                upcoming_rolls.append(2 if ball == 1 else 1)
            pins = 0
            ball = 0
            frames += 1

        elif frames == 9:
            if ball == 1 and pins == 10:
                pins = 0
                upcoming_rolls.append(2)
            elif ball == 2:
                if pins == 10 or sum(rolls[i-1:i+1]) == 10:
                    pins = 0
                    upcoming_rolls.append(1)
                elif ball == 3:
                    ball = 0
                    frames += 1

    return total, ball, frames