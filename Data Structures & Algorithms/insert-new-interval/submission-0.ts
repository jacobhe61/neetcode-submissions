class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals: number[][], newInterval: number[]): number[][] {
        const res = [];
        for (let i = 0; i < intervals.length; i++) {
            if (newInterval[0] > intervals[i][1]) {
                res.push(intervals[i]);
            } else if (newInterval[1] < intervals[i][0]) {
                res.push(newInterval);
                return [...res, ...(intervals.slice(i))];
            } else {
                newInterval = [Math.min(newInterval[0], intervals[i][0]), Math.max(newInterval[1], intervals[i][1])];
            }
        }
        res.push(newInterval);
        return res;
    }
}
