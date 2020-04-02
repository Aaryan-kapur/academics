import java.util.*;

class Main {
    public static void main(String[] args) {
        int x[] = new int[] { 100, 90, 0, 21 };
        int y[] = new int[] { 0, 17, 100, 80 };

        double d[] = new double[4];
        String a = "Action";
        String b = "Comedy";
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array :: ");
        int size = sc.nextInt();
        int x1[] = new int[size];
        int y1[] = new int[size];
        String movieName[] = new String[size];

        for (int i = 0; i < size; i++) {
            System.out.println("Enter name of movie :: " + i);
            movieName[i] = sc.next();
            System.out.println("Enter number of the action scenes of movie number :: " + i);
            x1[i] = sc.nextInt();
            System.out.println("Enter number of the comedy scenes of movie number :: " + i);
            y1[i] = sc.nextInt();

        }
        System.out.format("%30s %25s %22s %33s \n", "Movie Name", "Action_Scenes", "Comedy_Scenes", "Category");
        System.out.println(
                "----------------------------------------------------------------------------------------------------------------------------");
        for (int j = 0; j < size; j++) {

            int x_test = x1[j];
            int y_test = y1[j];
            for (int i = 0; i < 4; i++) {
                d[i] = Math.pow((Math.pow(x[i] - x_test, 2)) + (Math.pow(y[i] - y_test, 2)), 0.5);
            }
            double temp = d[0];
            int s = 0;
            for (int i = 0; i < 4; i++) {
                if (d[i] < temp) {
                    temp = d[i];
                    s = i;
                }
            }
            if (s == 0 || s == 1) {

                System.out.format("%30s %20s %20s %40s \n", movieName[j], x_test, y_test, a);
                System.out.println(
                        "----------------------------------------------------------------------------------------------------------------------------");

            } else {
                System.out.println(
                        "----------------------------------------------------------------------------------------------------------------------------");

                System.out.format("%30s %20s %20s %40s \n", movieName[j], x_test, y_test, b);
                System.out.println(
                        "----------------------------------------------------------------------------------------------------------------------------");

            }

        }
    }
}
