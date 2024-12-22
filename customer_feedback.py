def p_f_per(ratings):
    if not ratings:
        return "No ratings available."
    p_feedback = [rating for rating in ratings if rating >= 4]
    percentage = (len(p_feedback) / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.2f}%"


ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(p_f_per(ratings))
