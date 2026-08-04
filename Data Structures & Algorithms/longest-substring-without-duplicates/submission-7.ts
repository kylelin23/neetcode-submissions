class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let start = 0;
        let end = 0;
        let result = 0;
        let window = new Set();
        while (end < s.length){
            while(window.has(s[end])){
                window.delete(s[start]);
                start += 1;
            }
            window.add(s[end])
            result = Math.max(result, end - start + 1);
            end += 1;
        }
        return result;
    }
}