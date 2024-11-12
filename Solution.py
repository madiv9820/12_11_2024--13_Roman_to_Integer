class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to integer values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the result variable to store the final integer
        total_value = 0
        
        # Index to keep track of our position in the string
        i = 0
        
        # Loop through the Roman numeral string
        while i < len(s):
            # Check if there's a next character to compare with
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                # If the current character value is less than the next character value,
                # it means this is a subtractive combination (e.g., IV = 4, IX = 9).
                total_value += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2  # Skip the next character as it's already processed
            else:
                # Otherwise, just add the current character's value to the total
                total_value += roman_to_int[s[i]]
                i += 1  # Move to the next character
        
        # Return the computed integer value
        return total_value