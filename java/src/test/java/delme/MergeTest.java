/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package delme;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

class MergeTest {
    @Test
    void testMerge() {
        var merged = Merge.merge(List.of(1, 3, 5), List.of(2, 4, 6));
        assertEquals(List.of(1, 2, 3, 4, 5, 6), merged);
    }
}