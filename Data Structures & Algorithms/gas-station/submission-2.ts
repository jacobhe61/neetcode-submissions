class Solution {
    /**
     * @param {number[]} gas
     * @param {number[]} cost
     * @return {number}
     */
    canCompleteCircuit(gas: number[], cost: number[]): number {
        if (gas.reduce((a, b) => a + b, 0) < cost.reduce((a, b) => a + b, 0)) {
            return -1;
        }

        let total = 0;
        let start = 0;
        for (let i = 0; i < gas.length; i++) {
            total = total + gas[i] - cost[i];
            if (total < 0) {
                total = 0
                start = i + 1;
            }
        }

        if (start === gas.length) {
            return -1;
        }
        return start;
    }
}
