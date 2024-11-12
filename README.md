# Roman to Integer Conversion

- ### Intuition
    The Roman numeral system is made up of specific symbols (e.g., `I`, `V`, `X`, `L`, `C`, `D`, `M`) that correspond to integer values. Some Roman numeral combinations use **subtractive notation** to represent smaller values before larger values, such as:

    - `IV = 4` (5 - 1)
    - `IX = 9` (10 - 1)
    - `XC = 90` (100 - 10)

    Given a Roman numeral string, our goal is to convert it into its corresponding integer value by considering both **additive** and **subtractive** cases. 

    For example:
    - `VII = 7` (5 + 1 + 1)
    - `IV = 4` (5 - 1)

- ### Approach

    1. **Mapping Roman Numerals to Integer Values**:
        - We create a dictionary (or map) where each Roman numeral character (e.g., `I`, `V`, `X`) is associated with its corresponding integer value (e.g., `I = 1`, `V = 5`, `X = 10`, etc.).

    2. **Iterating Through the String**:
        - We loop through the characters of the Roman numeral string:
            - For each character, we check if the next character represents a larger numeral. If true, we subtract the current character's value from the next character's value (i.e., subtractive notation).
            - If no subtraction is necessary (i.e., the current numeral is smaller or equal to the next one), we add its value to the total.

    3. **Edge Case Handling**:
        - The algorithm handles cases like `IV`, `IX`, `XL`, etc., by checking the value of each character against the next one.
        - We process each character efficiently, skipping over already-processed characters in the case of subtractive pairs like `IV`.

- ### Time Complexity

    - **Time Complexity: O(n)**
        - The time complexity is **O(n)**, where `n` is the length of the Roman numeral string `s`.
        - We iterate through the string exactly once, processing each character in constant time (lookup, comparison, and addition/subtraction).
        - Therefore, the overall time complexity is linear with respect to the length of the string.

- ### Space Complexity

    - **Space Complexity: O(1)**
        - The space complexity is **O(1)** because:
            - The dictionary holding the Roman numeral values has a fixed size (7 entries for the Roman symbols).
            - Only a few integer variables (`total_value`, `i`) are used for computation, and they do not depend on the input size.
        - As such, the space complexity is constant.

- ### Code

    - **Python Code**

        ```python3 []
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
        ```
    
    - **C++ Solution**

        ```C++ []
        class Solution {
            public:
                int romanToInt(string s) {
                    // Initialize an unordered map to store the Roman numeral characters and their corresponding integer values
                    unordered_map<char, int> roman_To_Int = {
                        {'I', 1},    // 'I' corresponds to 1
                        {'V', 5},    // 'V' corresponds to 5
                        {'X', 10},   // 'X' corresponds to 10
                        {'L', 50},   // 'L' corresponds to 50
                        {'C', 100},  // 'C' corresponds to 100
                        {'D', 500},  // 'D' corresponds to 500
                        {'M', 1000}  // 'M' corresponds to 1000
                    };
                    
                    // Initialize a variable to hold the total integer value
                    int total_Value = 0;
                    
                    // Iterate through the Roman numeral string
                    for(int i = 0; i < s.length(); ) {
                        // Check if the current character's value is less than the next character's value
                        // This is the case for subtractive notation (e.g., IV = 4, IX = 9)
                        if(i + 1 < s.length() && roman_To_Int[s[i + 1]] > roman_To_Int[s[i]]) {
                            // If subtractive notation is found, subtract the current character's value
                            // from the next character's value and add it to the total
                            total_Value += (roman_To_Int[s[i + 1]] - roman_To_Int[s[i]]);
                            i += 2; // Skip the next character, since it's already processed
                        }
                        else {
                            // If no subtractive notation is found, just add the value of the current character
                            total_Value += roman_To_Int[s[i]];
                            i += 1; // Move to the next character
                        }
                    }

                    // Return the computed total value
                    return total_Value;
                }
        };
        ```

- ### Summary of Time and Space Complexities

    | **Language**   | **Time Complexity** | **Space Complexity** |
    |----------------|---------------------|----------------------|
    | **C++**        | O(n)                | O(1)                 |
    | **Python**     | O(n)                | O(1)                 |