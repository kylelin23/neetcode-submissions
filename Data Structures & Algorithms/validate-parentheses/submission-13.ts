class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        let stack = [];
        let endToStart = new Map();
        endToStart.set(')', '(');
        endToStart.set('}', '{');
        endToStart.set(']', '[');
        for (let char of s){
            console.log(char);
            if(endToStart.has(char)){
                console.log(stack)
                if(stack[stack.length - 1] != endToStart.get(char)){
                    return false;
                }
                else{
                    stack.pop();
                }
            }
            else{
                stack.push(char);
            }
        }
        return stack.length == 0;
    }
}
