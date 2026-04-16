package com.library;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {

    static final int MAX_DAYS_ALLOWED = 14;
    static final double FINE_PER_DAY = 2.0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("========================================");
        System.out.println("   LIBRARY MANAGEMENT SYSTEM");
        System.out.println("========================================");

        // User Details
        System.out.print("Enter User Name     : ");
        String userName = scanner.nextLine().trim();

        System.out.print("Enter User ID       : ");
        String userId = scanner.nextLine().trim();

        // Number of books
        System.out.print("Enter number of books issued: ");
        int numBooks = Integer.parseInt(scanner.nextLine().trim());

        List<String> books = new ArrayList<>();
        for (int i = 1; i <= numBooks; i++) {
            System.out.print("  Enter Book " + i + " name : ");
            books.add(scanner.nextLine().trim());
        }

        // Days borrowed
        System.out.print("Enter number of days borrowed: ");
        int daysBorrowed = Integer.parseInt(scanner.nextLine().trim());

        // Calculate fine
        double totalFine = calculateFine(daysBorrowed);

        // Display Summary
        System.out.println("\n========================================");
        System.out.println("         BORROWING SUMMARY");
        System.out.println("========================================");
        System.out.printf("User Name    : %s%n", userName);
        System.out.printf("User ID      : %s%n", userId);
        System.out.printf("Days Borrowed: %d%n", daysBorrowed);
        System.out.printf("Max Allowed  : %d days%n", MAX_DAYS_ALLOWED);

        System.out.println("\nBooks Issued:");
        for (int i = 0; i < books.size(); i++) {
            System.out.printf("  %d. %s%n", i + 1, books.get(i));
        }

        System.out.println("\nBorrowing Status:");
        if (daysBorrowed <= MAX_DAYS_ALLOWED) {
            System.out.println("  Status : ON TIME");
            System.out.println("  Fine   : No fine. Return within the due date.");
        } else {
            int extraDays = daysBorrowed - MAX_DAYS_ALLOWED;
            System.out.println("  Status : OVERDUE");
            System.out.printf("  Extra Days : %d day(s)%n", extraDays);
            System.out.printf("  Total Fine : Rs. %.2f%n", totalFine);
        }

        System.out.println("========================================");
        scanner.close();
    }

    /**
     * Calculates the fine based on days borrowed.
     *
     * @param daysBorrowed number of days the books were borrowed
     * @return total fine amount (0 if within allowed limit)
     */
    public static double calculateFine(int daysBorrowed) {
        if (daysBorrowed <= MAX_DAYS_ALLOWED) {
            return 0.0;
        }
        int extraDays = daysBorrowed - MAX_DAYS_ALLOWED;
        return extraDays * FINE_PER_DAY;
    }

    /**
     * Determines borrowing status string.
     *
     * @param daysBorrowed number of days borrowed
     * @return "ON TIME" or "OVERDUE"
     */
    public static String getBorrowingStatus(int daysBorrowed) {
        return (daysBorrowed <= MAX_DAYS_ALLOWED) ? "ON TIME" : "OVERDUE";
    }
}
