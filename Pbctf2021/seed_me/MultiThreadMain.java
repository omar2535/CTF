import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.stream.LongStream;
import java.util.stream.Stream;
import java.util.stream.Collectors;

class MultiThreadMain {
    private static void printFlag() {
        try {
            System.out.println(Files.readString(Path.of("flag.txt")));
        }
        catch(IOException e) {
            System.out.println("Flag file is missing, please contact admins");
        }
    }

    public static void doGame(long seed) {
        int unlucky = 03777;
        int success = 0;
        int correct = 16;
    
        Random rng = new Random(seed);

        for(int i=0; i<correct; i++) {
            /* Throw away the unlucky numbers */
            for(int j=0; j<unlucky; j++) {
                rng.nextFloat();
            }

            /* Do you feel lucky? */
            if (rng.nextFloat() >= (7.331f*.1337f)) {
                success++;
            }
        }

        if (success == correct) {
            System.out.println("SEED: " + String.valueOf(seed));
            printFlag();
        }
        else {
            // System.out.println("Unlucky!");
        }
    }

    public static void main(String[] args) {
        for (long i=Long.MAX_VALUE; i>0; i--) {
            final long seed = i;
            doGame(seed);
        }
    }
}
