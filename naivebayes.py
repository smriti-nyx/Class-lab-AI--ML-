import math

# Training data
# Features: [Free, Win, Hello]
X = [
    [1, 1, 0],  # spam
    [1, 0, 0],  # spam
    [0, 0, 1],  # not spam
    [0, 1, 1]   # not spam
]

y = ["spam", "spam", "not_spam", "not_spam"]

n = len(X)
features = len(X[0])

# Count classes
spam_count = y.count("spam")
notspam_count = y.count("not_spam")

# Prior probabilities
P_spam = spam_count / n
P_notspam = notspam_count / n

# Count feature occurrences
spam_feature_count = [0] * features
notspam_feature_count = [0] * features

for i in range(n):
    for j in range(features):
        if y[i] == "spam":
            spam_feature_count[j] += X[i][j]
        else:
            notspam_feature_count[j] += X[i][j]

# Function  prediction
def predict(test):
    prob_spam = math.log(P_spam)
    prob_notspam = math.log(P_notspam)

    for j in range(features):
        # Laplace smoothing
        p1_spam = (spam_feature_count[j] + 1) / (spam_count + 2)
        p1_notspam = (notspam_feature_count[j] + 1) / (notspam_count + 2)

        if test[j] == 1:
            prob_spam += math.log(p1_spam)
            prob_notspam += math.log(p1_notspam)
        else:
            prob_spam += math.log(1 - p1_spam)
            prob_notspam += math.log(1 - p1_notspam)

    return "SPAM" if prob_spam > prob_notspam else "NOT SPAM"


# Test example
test_email = [1, 1, 0]  # Free=1, Win=1, Hello=0
print("Prediction:", predict(test_email))