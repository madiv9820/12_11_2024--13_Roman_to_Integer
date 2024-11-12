#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

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

int main() {
    string s; Solution sol;
    cin >> s;
    cout << sol.romanToInt(s = s) << endl;
}