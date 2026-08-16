class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1: string, s2: string): boolean {
        // Initialize counts of s1
        let s1Counts = new Array(26).fill(0);
        let s2Counts = new Array(26).fill(0);
        for(let c of s1){
            s1Counts[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        // Initialize window counts of s2
        for(let c of s2.slice(0, s1.length)){
            s2Counts[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        let start = 0;
        let end = start + s1.length - 1;

        // Slide window
        while(end < s2.length){
            // check if permutation matches
            console.log(s1Counts)
            console.log(s2Counts)
            let cond = true;
            for(let i = 0; i < 26; i++){
                if(s1Counts[i] != s2Counts[i]){
                    cond = false;
                }
            }
            if(cond){
                return true;
            }

            // shift window and update counts
            s2Counts[s2[start].charCodeAt(0) - 'a'.charCodeAt(0)] -= 1;
            start += 1;
            end += 1;
            if (end < s2.length){
                s2Counts[s2[end].charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }
        }
        return false;
    }
}
