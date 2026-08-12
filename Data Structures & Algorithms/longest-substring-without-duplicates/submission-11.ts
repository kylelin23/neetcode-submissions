class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let start = 0;
        let end = 0; 
        let chars = new Set();
        let result = 0;
        while (end < s.length){
            while(chars.has(s[end]) && start < end){
                chars.delete(s[start]);
                start += 1;
            }
            chars.add(s[end]);
            result = Math.max(result, chars.size);
            end += 1;
        }
        return result;

    }
}