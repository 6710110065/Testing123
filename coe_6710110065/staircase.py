def staircase(n, char="#"):
    if not (1 <= n <= 30):
        raise ValueError("n must be between 1 and 30")
    
    return "\n".join(char * i for i in range(1, n + 1))