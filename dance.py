def min_moves(n, instructions):
    # List of possible positions: up, down, left, right
    positions = ["up", "down", "left", "right"]
    
    # Initialize DP table: dp[(f1, f2)] stores minimum moves to reach foot1 at f1 and foot2 at f2
    dp = {}
    
    # Initialize base case: We can start with any pair of positions without any moves
    for p1 in positions:
        for p2 in positions:
            dp[(p1, p2)] = 0
    
    # Process each instruction
    for instruction in instructions:
        # Temporary dictionary to store new states for this instruction
        new_dp = {}
        
        # For each pair of foot positions (f1, f2), check which foot to move to the instruction
        for (f1, f2), moves in dp.items():
            # Move the first foot (f1) to the instruction, if it's not already there
            if f1 != instruction:
                new_dp[(instruction, f2)] = min(new_dp.get((instruction, f2), float('inf')), moves + 1)
            
            # Move the second foot (f2) to the instruction, if it's not already there
            if f2 != instruction:
                new_dp[(f1, instruction)] = min(new_dp.get((f1, instruction), float('inf')), moves + 1)
        
        # Update the dp table to the new_dp after processing this instruction
        dp = new_dp
    
    # The final result is the minimum number of moves from all possible final states
    return min(dp.values())

# Input processing
try:
    n = int(input())  # Number of instructions
    instructions = [input().strip() for _ in range(n)]  # List of instructions

    # Output the result
    print(min_moves(n, instructions))

except ValueError:
    print("Invalid input. Please make sure the first input is an integer, followed by strings of directions.")
