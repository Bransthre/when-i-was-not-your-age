#import packages here

#SECTION 1: Dices

f_a_log = {}
def memoized(func):
    def lookup(*args):
        if (func, args) not in f_a_log:
            f_a_log[(func, args)] = func(*args)
        return f_a_log.get((func, args))
    return lookup

def six_sided(num):
    """Returns the probability a six sided dice rolls num.
    
    Args:
        num: The result of six sided dice the probability is returned for.

    Returns:
        A floating point number representing the probability.
    """
    return 1/6 if 1 <= num <= 6 else 0

@memoized
def probability_with_roll(score, roll_num, p=six_sided):
    """Returns probability of getting SCORE with ROLL_NUM rolls with probability function P.
    
    Args:
        score: Target score
        roll_num: Target number of rolls
        p: Probability function
    
    Returns:
        A floating-point representing the probability to get SCORE with ROLL_NUM rolls 
        given probability function P
    """
    assert score > 0
    if score == 1: return probability_one(roll_num, p)
    else: return probability_none_one(score, roll_num, p)

@memoized
def probability_one(roll_num, p=six_sided):
    """Returns probability of scoring 1 in ROLL_NUM rolls given probability function P.
    
    Args:
        roll_num: Target number of rolls
    
    Returns:
    A floating-point representing the probability that player scores 1 from rolling
    the dice ROLL_NUM times given probability function P.
    """
    if roll_num == 1:
        return p(1)
    return p(1) + (1 - p(1)) * probability_one(roll_num - 1, p)

@memoized
def probability_none_one(total, roll_num, p=six_sided):
    """Returns probability of scoring TOTAL in ROLL_NUM rolls given probability function P.
    
    Args:
        roll_num: Target number of rolls
    
    Returns:
        A floating-point representing the probability that player scores TOTAL 
        from rolling the dice ROLL_NUM times given probability function P.
    """
    if total == 0 and roll_num == 0: return 1
    if roll_num == 0: return 0
    total_probability = 0
    for i in range(2, 7):
        total_probability += p(i) * probability_none_one(total - i, roll_num - 1, p)
    return total_probability

@memoized
def probability_between_score(minimum, roll_num, maximum = 61, p=six_sided):
    """Returns probability of scoring in [MINIMUM, MAXIMUM) in ROLL_NUM rolls given probability function P.
    
    Args:
        minimum: The lower bound of desired score
        roll_num: Target number of rolls
    
    Returns:
        A floating-point representing the probability that player scores at [MINIMUM, MAXIMUM)
        from rolling the dice ROLL_NUM times given probability function P.
    """
    total_probability = 0
    for score in range(minimum, maximum):
        total_probability += probability_with_roll(score, roll_num, p)
    return total_probability

@memoized
def optimal_rolls(target_score):
    """Returns the optimal number of rolls to get at least TARGET_SCORE.

    Args:
        target_score: the minimum target score desired.
    
    Returns:
        The number of rolls that has the highest probability in scoring at least TARGET_SCORE
    """
    roll_num_probability_arr = [probability_between_score(target_score, i) for i in range(2, 11)]
    print("DEBUG", roll_num_probability_arr)
    return max([i for i in range(2, 11)], key = lambda i: roll_num_probability_arr[i - 2])


#SECTION 2: Strategy

def final_stragey(score, opp_score):
    """ A deterministic pure function that returns the optimal number of roll based on SCORE and OPP_SCORE.

    Args:
        score: the current score of self
        opp_score: the opponent score
    
    Returns:
        An integer representing the best number of rolls to provide now
    """
    