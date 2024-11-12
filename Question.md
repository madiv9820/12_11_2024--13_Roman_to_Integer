# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer?envType=study-plan-v2&envId=top-interview-150)

__Type:__ Easy <br>
__Topics:__ Hash Table, Math, String <br>
__Companies:__ Google, Amazon, Microsoft, Bloomberg, Oracle, IBM, tcs, Accenture, DeltaX, Meta, Adobe, Uber, LinkedIn, Goldman Sachs, Zoho, Wix, Yahoo, Apple, Wipro, Citadel, Visa, Yandex, Cognizant, eBay, Intel, Salesforce, Twilio
<hr>

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

<table>
    <tr><th>Symbol</th> <th>Value</th></tr>
    <tr><td>I</td> <td>1</td></tr>
    <tr><td>V</td> <td>5</td></tr>
    <tr><td>X</td> <td>10</td></tr>
    <tr><td>L</td> <td>50</td></tr>
    <tr><td>C</td> <td>100</td></tr>
    <tr><td>D</td> <td>500</td></tr>
    <tr><td>M</td> <td>1000</td></tr>
</table>

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ s = "III" <br>
__Output:__ 3 <br>
__Explanation:__ III = 3.

- __Example 2:__ <br>
__Input:__ s = "LVIII" <br>
__Output:__ 58 <br>
__Explanation:__ L = 50, V= 5, III = 3.

- __Example 3:__ <br>
__Input:__ s = "MCMXCIV" <br>
__Output:__ 1994 <br>
__Explanation:__ M = 1000, CM = 900, XC = 90 and IV = 4.
<hr>

### Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is __guaranteed__ that `s` is a valid roman numeral in the range `[1, 3999]`.
<hr>

### Hints
- Problem is simpler to solve by working the string from back to front and using a map. 