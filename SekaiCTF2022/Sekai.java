/*
 * Decompiled with CFR 0.150.
 */
import java.util.Scanner;

public class Sekai {
    private static int length = (int)Math.pow(2.0, 3.0) - 2;

    public static void main(String[] arrstring) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the flag: ");
        String string = scanner.next();
        System.out.println("Length of input string: " + string.length());
        System.out.println("Length variable: " + length);
        if (string.length() != 43) {
            System.out.println("Oops, wrong flag!");
            return;
        }
        String string2 = string.substring(0, length);
        String string3 = string.substring(length, string.length() - 1);
        String string4 = string.substring(string.length() - 1);
        System.out.println(string2 + " - " + string3 + " - " + string4);
        if (string2.equals("SEKAI{") && string4.equals("}")) {
            System.out.println(length);
            assert (string3.length() == length * length);
            if (Sekai.solve(string3)) {
                System.out.println("Congratulations, you got the flag!");
            } else {
                System.out.println("Oops, wrong flag!");
            }
        } else {
            System.out.println("Oops, wrong flag!");
        }
    }

    public static String encrypt(char[] arrc, int n) {
        int n2;
        char[] arrc2 = new char[length * 2];
        int n3 = length - 1;
        int n4 = length;
        for (n2 = 0; n2 < length * 2; n2+=2) {
            arrc2[n2] = arrc[n3--];
            arrc2[n2 + 1] = arrc[n4++];
        }
        System.out.println("Before xor Arr: " + String.valueOf(arrc2));
        n2 = 0;
        while (n2 < length * 2) {
            int n5 = n2++;
            arrc2[n5] = (char)(arrc2[n5] ^ (char)n);
        }
        System.out.println("After xor Arr: " + String.valueOf(arrc2));
        System.out.println("------");
        return String.valueOf(arrc2);
    }

    public static String decrypt(String str, int n) {
        // Copy into char array
        char[] arrc = new char[str.length()];
        for (int i = 0; i < str.length(); i++) {
            arrc[i] = str.charAt(i);
        }

        // Go through encrypt while loop
        int n2 = 0;
        while (n2 < length * 2) {
            int n5 = n2++;
            arrc[n5] = (char)(arrc[n5] ^ (char)n);
        }

        char[] arrc2 = new char[length * 2];
        arrc2[0] = arrc[10];
        arrc2[1] = arrc[8];
        arrc2[2] = arrc[6];
        arrc2[3] = arrc[4];
        arrc2[4] = arrc[2];
        arrc2[5] = arrc[0];
        arrc2[6] = arrc[1];
        arrc2[7] = arrc[3];
        arrc2[8] = arrc[5];
        arrc2[9] = arrc[7];
        arrc2[10] = arrc[9];
        arrc2[11] = arrc[11];
        System.out.println(String.valueOf(arrc2));
        return String.valueOf(arrc2);



    }

    public static char[] getArray(char[][] arrc, int n, int n2) {
        int n3;
        char[] arrc2 = new char[length * 2];
        int n4 = 0;
        for (n3 = 0; n3 < length; ++n3) {
            arrc2[n4] = arrc[n][n3];
            ++n4;
        }
        for (n3 = 0; n3 < length; ++n3) {
            arrc2[n4] = arrc[n2][length - 1 - n3];
            ++n4;
        }

        for (int i=0; i<length*2; i++) {
            System.out.print(arrc2[i] + "|");
        }
        System.out.println("");

        return arrc2;
    }

    public static char[][] transform(char[] arrc, int n) {
        char[][] arrc2 = new char[n][n];
        for (int i = 0; i < n * n; ++i) {
            arrc2[i / n][i % n] = arrc[i];
        }
        return arrc2;
    }

    public static boolean solve(String string) {
        char[][] arrc = Sekai.transform(string.toCharArray(), length);
        for (int i = 0; i <= length / 2; ++i) {
            for (int j = 0; j < length - 2 * i - 1; ++j) {
                char c = arrc[i][i + j];
                arrc[i][i + j] = arrc[length - 1 - i - j][i];
                arrc[Sekai.length - 1 - i - j][i] = arrc[length - 1 - i][length - 1 - i - j];
                arrc[Sekai.length - 1 - i][Sekai.length - 1 - i - j] = arrc[i + j][length - 1 - i];
                arrc[i + j][Sekai.length - 1 - i] = c;
            }
        }
        printMatrix(arrc);
        
        
        System.out.println(Sekai.decrypt("oz]{R]3l]]B#", 2) + Sekai.decrypt("50es6O4tL23E", 1) + Sekai.decrypt("tr3c10_F4TD2", 0));
        System.out.println("");

        System.out.println("------Running normal code again------");
        return "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2".equals(
            Sekai.encrypt(Sekai.getArray(arrc, 0, 5), 2)
            + Sekai.encrypt(Sekai.getArray(arrc, 1, 4), 1)
            + Sekai.encrypt(Sekai.getArray(arrc, 2, 3), 0)
        );
    }

    public static void printMatrix(char[][] arrc) {
        System.out.println("------ Printing the matrix ------");
        for (int i=0; i<length; i++) {
            for (int j=0; j<length; j++) {
                System.out.print("|" + arrc[i][j] + "|");
            }
            System.out.println("\n-----------------------");
        }
        System.out.println("------ Printing the matrix ------");
    }
}