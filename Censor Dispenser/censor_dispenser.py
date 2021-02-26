# ============================================
# Functions
# ============================================

def censor(string, forbidden, negative_words_list=None):
    if type(forbidden) == str:
        forbidden_list = forbidden.split()
    elif type(forbidden) == list:
        forbidden_list = forbidden

    string_list = string.split(' ')

    negative_count = 0

    for i in range(len(string_list)):
        # Censor
        for j in range(len(forbidden_list)):
            if string_list[i] == forbidden_list[j]:
                string_list[i] = '*'*len(forbidden_list[j])

        # Negative words
        if negative_words_list is not None:
            for n in range(len(negative_words_list)):
                if string_list[i] == negative_words_list[n]:
                    if negative_count <= 2:
                        negative_count += 1
                    else:
                        string_list[i] = '*'*len(negative_words_list[n])

    return " ".join(string_list)


# ============================================
# Import files
# ============================================
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


# ============================================
# Main calls
# ============================================
print(censor(email_one, ' '))
print(censor(email_two, ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]))
print(censor(email_three, ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]))