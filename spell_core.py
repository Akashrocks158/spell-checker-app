
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [word.strip().lower() for word in file.readlines()]

def edit_distance(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

def suggest(word, dictionary, max_suggestions=5):
    word = word.lower()

    # ✅ Filter dictionary to words within length ±2
    filtered_dict = [w for w in dictionary if abs(len(w) - len(word)) <= 2]

    # ✅ Calculate edit distances only on filtered words
    distances = [(edit_distance(word, dict_word), dict_word) for dict_word in filtered_dict]
    distances.sort()

    return [word for _, word in distances[:max_suggestions]]

