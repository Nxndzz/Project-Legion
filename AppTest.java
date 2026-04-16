package com.library;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {

    // Test 1: No fine when returned on time
    @Test
    public void testNoFine() {
        double fine = App.calculateFine(10);
        assertEquals(0.0, fine, 0.001);
    }

    // Test 2: No fine at exactly 14 days (boundary)
    @Test
    public void testNoFineAtLimit() {
        double fine = App.calculateFine(14);
        assertEquals(0.0, fine, 0.001);
    }

    // Test 3: Fine for 1 extra day (15 - 14 = 1 day * 2.0 = 2.0)
    @Test
    public void testFineOneExtraDay() {
        double fine = App.calculateFine(15);
        assertEquals(2.0, fine, 0.001);
    }

    // Test 4: Fine for 5 extra days (19 - 14 = 5 days * 2.0 = 10.0)
    @Test
    public void testFineFiveExtraDays() {
        double fine = App.calculateFine(19);
        assertEquals(10.0, fine, 0.001);
    }

    // Test 5: Status is ON TIME
    @Test
    public void testStatusOnTime() {
        String status = App.getBorrowingStatus(7);
        assertEquals("ON TIME", status);
    }

    // Test 6: Status is OVERDUE
    @Test
    public void testStatusOverdue() {
        String status = App.getBorrowingStatus(20);
        assertEquals("OVERDUE", status);
    }

    // Test 7: Fine is never negative
    @Test
    public void testFineNotNegative() {
        double fine = App.calculateFine(5);
        assertTrue(fine >= 0);
    }

    // Test 8: Fine is greater than zero when overdue
    @Test
    public void testFineIsPositiveWhenOverdue() {
        double fine = App.calculateFine(16);
        assertTrue(fine > 0);
    }
}
