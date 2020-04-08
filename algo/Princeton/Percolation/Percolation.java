import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[] state;
    private WeightedQuickUnionUF grid, altGrid;
    private int n;
    private int count = 0;

    public Percolation(int n) {
        //create n-by-n grid, with all sites blocked
        if (n <= 0) {
            throw new IllegalArgumentException("Out of bounds");
        }
        this.n = n;
        int size = n * n;
        grid = new WeightedQuickUnionUF(size + 2);
        altGrid = new WeightedQuickUnionUF(size + 1);
        state = new boolean[size + 2];

        for (int i = 1; i < size; i++)
            state[i] = false;

        state[0] = true;
        state[size + 1] = true;
    }

    public void open(int row, int col) {
        //open site (row, col) if it is not open already
        int index = xytoIndex(row, col);
        if (!state[index]) {
            state[index] = true;
            count++;
        }

        //connect all open sites
        if (row != 1 && isOpen(row - 1, col)) {
            grid.union(index, xytoIndex(row - 1, col));
            altGrid.union(index, xytoIndex(row - 1, col));
        }
        if (row != n && isOpen(row + 1, col)) {
            grid.union(index, xytoIndex(row + 1, col));
            altGrid.union(index, xytoIndex(row + 1, col));

        }
        if (col != 1 && isOpen(row, col - 1)) {
            grid.union(index, xytoIndex(row, col - 1));
            altGrid.union(index, xytoIndex(row, col - 1));

        }
        if (col != n && isOpen(row, col + 1)) {
            grid.union(index, xytoIndex(row, col + 1));
            altGrid.union(index, xytoIndex(row, col + 1));

        }
        if (row == 1) {
            grid.union(0, index);
            altGrid.union(0, index);
        }
        if (row == n) {
            grid.union(state.length - 1, index);
        }
    }

    public boolean isOpen(int row, int col) {
        //is site (row, col) open?
        int index = xytoIndex(row, col);
        return state[index];

    }

    public boolean isFull(int row, int col) {
        //is site (row, col) full?
        int index = xytoIndex(row, col);
        return grid.connected(0, index) && altGrid.connected(0, index);
    }

    public int numberOfOpenSites() {
        //number of open sites
        return count;


    }

    public boolean percolates() {
        //does the system percolate?
        return grid.connected(0, state.length - 1);
    }

    private int xytoIndex(int x, int y) {
        if (x <= 0 || x > n) {
            throw new IllegalArgumentException("Out of bounds");
        }
        if (y <= 0 || y > n) {
            throw new IllegalArgumentException("Out of bounds");
        }
        return (x - 1) * n + y;

    }

    public static void main(String[] args) {
        //test client (optional)
        In in = new In(args[0]);      //input file
        int N = in.readInt();         //N-by-N percolation system

        Percolation test = new Percolation(N);
        while (!in.isEmpty()) {
            int i = in.readInt();
            int j = in.readInt();
            test.open(i, j);
        }
        System.out.println(test.percolates());
        System.out.println(test.numberOfOpenSites());

    }

}

