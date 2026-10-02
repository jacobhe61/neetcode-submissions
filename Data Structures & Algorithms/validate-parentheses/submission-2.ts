class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        let stack: string[] = [];
        for (const c of s) {
            if (c === "(") {
                stack.push("(");
            }
            else if (c === "[") {
                stack.push("[");
            }
            else if (c === "{") {
                stack.push("{");
            }
            else if (c === ")") {
                if (stack.length === 0 || !(stack[stack.length-1] === "(")) {
                    return false;
                }
                stack.pop();
            }
            else if (c === "}") {
                if (stack.length === 0 || !(stack[stack.length-1] === "{")) {
                    return false;
                }
                stack.pop();
            }
            else if (c === "]") {
                if (stack.length === 0 || !(stack[stack.length-1] === "[")) {
                    return false;
                }
                stack.pop();
            }
        }
        if (!(stack.length === 0)) {
            return false;
        }
        return true;
    }
}
