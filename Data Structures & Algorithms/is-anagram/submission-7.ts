class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        let counts = new Map<string, number>()
        if (s.length != t.length){
            return false;
        }
        for (let c of s){
            counts.set(c, (counts.get(c) ?? 0) + 1);
        }

        for(let c of t){
            if (counts.get(c) == undefined || counts.get(c) <= 0){
                return false
            }
            counts.set(c, (counts.get(c) ?? 0) - 1)
        }
        return true
    }
}
