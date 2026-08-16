class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        let endToStart = new Map<string, string>([
            [')', '('], 
            ['}', '{'], 
            [']', '[']
        ]);

        let stack = [];

        // iterate through s
        for(let c of s){
            console.log(stack)
            if(endToStart.has(c)){ // If c is an ending char
                if(endToStart.get(c) != stack[stack.length - 1]){
                    return false;
                }
                stack.pop();
            }
            else{
                stack.push(c);
            }

        }
        return stack.length == 0;

    }
}
