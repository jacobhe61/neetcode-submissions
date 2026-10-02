class Solution {
    /**
     * @param {number[][]} triplets
     * @param {number[]} target
     * @return {boolean}
     */
    mergeTriplets(triplets: number[][], target: number[]): boolean {
        let res = [0, 0, 0];
        let swap: boolean;
        for (const tr of triplets) {
            swap = true;
            for (let i = 0; i < 3; i++) {
                if (Math.max(res[i], tr[i]) > target[i]) {
                    swap = false;
                    break;
                }
            }
            if (swap) {
                res = [Math.max(res[0], tr[0]), Math.max(res[1], tr[1]), Math.max(res[2], tr[2])];
            }
        }
        return res.every((elem, i) => elem === target[i]);
    }
}
