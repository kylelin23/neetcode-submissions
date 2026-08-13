class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1: string, s2: string): boolean {
        // Initialize start and end
        let start = 0;
        let end = start + s1.length - 1;

        // Initialize counts with counts of s1
        let s1Counts = Array(26).fill(0);
        for(let c of s1){
            s1Counts[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        // Initialize counts with counts of s2
        let s2Counts = Array(26).fill(0);
        for(let c of s2.slice(0, s1.length)){
            s2Counts[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        // slide window through s2
        while (end < s2.length){
            console.log(s2Counts)
            // Check if window counts are same as s1 counts
            let cond = true;
            for(let i = 0; i < 26; i++){
                if(s1Counts[i] != s2Counts[i]){
                    cond = false;
                }
            }
            if(cond){
                // If so, return true
                return true;
            }

            // Update window pointers
            s2Counts[s2[start].charCodeAt(0) - 'a'.charCodeAt(0)] -= 1;
            start += 1;
            end += 1;
            if(end < s2.length){
                s2Counts[s2[end].charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }
            
        }
        return false;
        // return false
    }
}
