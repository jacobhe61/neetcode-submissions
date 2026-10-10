class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals: number[][]): number[][] {
        intervals.sort((a, b) => a[0] - b[0]);

        let res = [];
        let curr = intervals[0];
        for (let i = 0; i < intervals.length; i++) {
            if (curr[1] < intervals[i][0]) {
                res.push(curr);
                curr = intervals[i];
            }
            else {
                curr = [Math.min(curr[0], intervals[i][0]), Math.max(curr[1], intervals[i][1])];
            }
        }
        res.push(curr);
        return res;
    }
}
