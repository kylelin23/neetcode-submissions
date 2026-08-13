class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        let counts = new Map();
        let maxFreq = 0;
        let result = 0;
        let start = 0;

        // For loop of end pointer
        for (let end = 0; end < s.length; end++){
            // Update counts bc we are adding a new end character
            if(counts.has(s[end])){
                counts.set(s[end], counts.get(s[end]) + 1);
            }
            else{
                counts.set(s[end], 1);
            }
            
            // Update maxFreq
            maxFreq = Math.max(maxFreq, counts.get(s[end]));
            
            // Check if window is still valid
            while(end - start + 1 - maxFreq > k){
                // If not valid, update counts
                counts.set(s[start], counts.get(s[start]) - 1);
                // Increment start pointer by 1
                start += 1;
            }

            // Update result with window now that we checked its valid
            result = Math.max(result, end - start + 1)
        }
            
            
        // return the largest length
        return result;
    }
}
