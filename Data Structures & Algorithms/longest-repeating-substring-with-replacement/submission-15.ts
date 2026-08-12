class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        let counts = new Map();
        let maxLetterCount = 0;
        let start = 0;
        let end = 0;
        let result = 0;
        while (end < s.length){
            // Update counts
            if (counts.has(s[end])){
                counts.set(s[end], counts.get(s[end]) + 1);
            }
            else{
                counts.set(s[end], 1);
            }

            // Update maxLetterCount
            if (counts.get(s[end]) > maxLetterCount){
                maxLetterCount = counts.get(s[end]);
            }

            // Check if string applies
            while((end - start + 1) - maxLetterCount > k){
                counts.set(s[start], counts.get(s[start]) - 1)
                start += 1;
            }
            result = Math.max(result, (end - start + 1));

            end += 1;
        }
        return result;
    }
}
