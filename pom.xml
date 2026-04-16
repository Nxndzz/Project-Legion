<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <!-- ===================== Project Identity ===================== -->
    <groupId>com.library</groupId>
    <artifactId>library-management-system</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>Library Management System</name>
    <description>
        A Maven-based Library Management System that allows users to borrow
        books, tracks borrowing duration, and computes late fines.
    </description>

    <!-- ===================== Properties ===================== -->
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>4.13.2</junit.version>
        <maven.surefire.version>3.0.0</maven.surefire.version>
        <maven.compiler.plugin.version>3.11.0</maven.compiler.plugin.version>
        <maven.jar.plugin.version>3.3.0</maven.jar.plugin.version>
    </properties>

    <!-- ===================== Dependencies ===================== -->
    <dependencies>

        <!-- JUnit 4 for unit testing -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>

    </dependencies>

    <!-- ===================== Build Configuration ===================== -->
    <build>
        <plugins>

            <!-- Compiler Plugin: enforce Java 11 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${maven.compiler.plugin.version}</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                    <encoding>${project.build.sourceEncoding}</encoding>
                </configuration>
            </plugin>

            <!-- Surefire Plugin: run JUnit tests and generate reports -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${maven.surefire.version}</version>
                <configuration>
                    <!-- Fail build if no tests found -->
                    <failIfNoTests>true</failIfNoTests>
                    <!-- Generate XML reports for Jenkins JUnit publisher -->
                    <reportsDirectory>${project.build.directory}/surefire-reports</reportsDirectory>
                </configuration>
            </plugin>

            <!-- JAR Plugin: produce an executable JAR with Main-Class manifest -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>${maven.jar.plugin.version}</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.library.App</mainClass>
                        </manifest>
                    </archive>
                    <finalName>library-management-system</finalName>
                </configuration>
            </plugin>

        </plugins>
    </build>

    <!-- ===================== Reporting ===================== -->
    <reporting>
        <plugins>
            <!-- Surefire Report: HTML test report via mvn site -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-report-plugin</artifactId>
                <version>${maven.surefire.version}</version>
            </plugin>
        </plugins>
    </reporting>

</project>
