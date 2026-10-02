class Solution {
    /**
     * @param {string} S
     * @return {number[]}
     */
    partitionLabels(S: string): number[] {
        const ends = new Map<string, number>();
        for (let i = 0; i < S.length; i++) {
            ends.set(S[i], i);
        }

        const res: number[] = [];
        let i = 0;
        let j = 0;
        let count: number;
        while (i < S.length) {
            count = 0;
            while (i <= j) {
                j = Math.max(ends.get(S[i]), j);
                i++;
                count++;
            }
            j = i;
            res.push(count);
        }

        return res;
    }
}
