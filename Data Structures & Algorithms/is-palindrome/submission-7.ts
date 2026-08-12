class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphaNumeric(c: string): boolean{
        return (c.charCodeAt(0) >= 'a'.charCodeAt(0) && c.charCodeAt(0) <= 'z'.charCodeAt(0)) || (c.charCodeAt(0) >= 'A'.charCodeAt(0) && c.charCodeAt(0) <= 'Z'.charCodeAt(0)) || (c.charCodeAt(0) >= '0'.charCodeAt(0) && c.charCodeAt(0) <= '9'.charCodeAt(0))
    }

    isPalindrome(s: string): boolean {
        let p1 = 0;
        let p2 = s.length - 1;
        while(p1 < p2){
            while(!this.isAlphaNumeric(s[p1]) && p1 < p2){
                p1 += 1;
            }
            while(!this.isAlphaNumeric(s[p2]) && p1 < p2){
                p2 -= 1;
            }
            if(s[p1].toLowerCase() != s[p2].toLowerCase()){
                return false;
            }
            p1 += 1;
            p2 -= 1;

        }
        return true;
    }
}
