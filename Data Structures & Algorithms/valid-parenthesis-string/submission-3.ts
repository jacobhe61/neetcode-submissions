class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    checkValidString(s: string): boolean {
        const parens: [string, number][] = [];
        const asts: [string, number][] = [];

        for (let i = 0; i < s.length; i++) {
            if (s[i] == "(") {
                parens.push(["(", i]);
            }
            if (s[i] == "*") {
                asts.push(["*", i]);
            }
            if (s[i] == ")") {
                if (parens.length > 0) {
                    parens.pop();
                }
                else if (asts.length > 0) {
                    asts.pop();
                }
                else {
                    return false;
                }
            }
        }
        while (parens.length > 0) {
            if (asts.length === 0) {
                return false;
            }
            const [p, i] = parens.pop();
            const [a, j] = asts.pop();
            if (j < i) {
                return false;
            }
        }
        return true;
    }
}
