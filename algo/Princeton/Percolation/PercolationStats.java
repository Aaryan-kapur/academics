import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {
    private Percolation test;
    private double[] ratio;


    public PercolationStats(int n, int trials) {
        // perform trials independent experiments on an n-by-n grid
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("argument not within range");
        }
        int size = n * n;
        double numberOfOpenSites;
        ratio = new double[trials];
        for (int i = 0; i < trials; i++) {
            test = new Percolation(n);
            while (!test.percolates()) {
                int row = StdRandom.uniform(1, n + 1);
                int col = StdRandom.uniform(1, n + 1);
                if (test.isOpen(row, col)) continue;
                test.open(row, col);
            }
            numberOfOpenSites = test.numberOfOpenSites();
            ratio[i] = numberOfOpenSites / size;
        }


    }

    public double mean() {
        // sample mean of percolation threshold
        return StdStats.mean(ratio);

    }

    public double stddev() {
        // sample standard deviation of percolation threshold
        return StdStats.stddev(ratio);
    }

    public double confidenceLo() {
        // low  endpoint of 95% confidence interval
        double mean = mean();
        double s = stddev();
        double tSqrt = Math.sqrt(ratio.length);
        return (mean - (1.96 * s / tSqrt));
    }

    public double confidenceHi() {
        // high endpoint of 95% confidence interval
        double mean = mean();
        double s = stddev();
        double tSqrt = Math.sqrt(ratio.length);
        return mean + (1.96 * s / tSqrt);
    }

    public static void main(String[] args) {
        // test client (described below)
        Stopwatch time;
        In in = new In(args[0]);      // input file
        int no = in.readInt();
        int trialsno = in.readInt();
        time = new Stopwatch();


        PercolationStats test2 = new PercolationStats(no, trialsno);
        System.out.printf("Mean value is         %f \n", test2.mean());
        System.out.printf("Standard deviation is %f \n", test2.stddev());
        System.out.printf("95 confidence interval =[ %f, %f ] \n", test2.confidenceLo(), test2.confidenceHi());
        System.out.println(time.elapsedTime());


    }
}
