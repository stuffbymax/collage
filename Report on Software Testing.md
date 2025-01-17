# Report on Software Testing

**Prepared By:** Martin Petik
**Student Number:** 279832
**Date:** 16-01-2025

## Core Elements in Software Testing

This section will describe the key components that need to be considered in the software testing process. We will cover software, hardware, data, interfaces and the final product, as well as explain how they relate to testing.

### 1. Introduction

This report aims to explain the fundamental parts of a software system and describe the different types of software testing methodologies. This report will detail the core elements of software, hardware, data, interfaces, and the final product of development. The report will explain different testing methods, their purpose and how they are used in the testing process, to provide a better understanding of software testing and why it's an important part of the software development process.

### 2. Understanding Core Elements in Testing

**Basic Test Process:** Performing any test involves a basic set of actions which are to configure, operate, observe, and evaluate the system. Once this is done, the results must be documented and presented in a report, with what was tested, what the results were, and the final evaluation. When checking that something works as expected, this is a confirmatory approach to testing.

### 2.1 Software

**What it is:** Think of software as the instructions that tell a computer what to do. It's not the physical machine, but the code that makes it run. This includes things like:
    *   **Operating Systems (OS):** Like Windows, macOS, or Linux, which manage the computer's basic functions.
    *   **Applications:** Programs that help users with tasks, like web browsers, word processors, or games.
    *   **Utilities:** Tools that support the computer, such as antivirus or disk management software.
    *   **Code Libraries:** Reusable collections of code that make software development more efficient (e.g., libraries for graphics or network communication).

**In relation to testing:** Software is the main thing we test. We need to make sure the code is:
    *   **Correct:** Does it do what it's supposed to do?
    *   **Robust:** Can it handle errors or unexpected input without crashing?
    *   **Secure:** Is it protected from vulnerabilities?
    *   **Efficient:** Does it run smoothly and use resources well?
    *   **User Friendly:** Is the interface intuitive and easy to use for the target audience?

Essentially, we're looking for bugs, making sure the software meets the project requirements, and that it does what we want it to do. 

### 2.2 Hardware

**What it is:** Hardware is the physical parts of a computer system, including:
    *   **Processor (CPU):** The "brain" of the computer that performs calculations.
    *   **Memory (RAM):** Temporary storage that holds data the computer is actively using.
    *   **Storage Devices:** Hard drives, solid-state drives (SSDs), and other media for storing data permanently.
    *   **Input Devices:** Keyboard, mouse, touch screen, etc., that allow users to interact with the computer.
    *   **Output Devices:** Monitor, printer, speakers, etc., that display or convey the results.

**In relation to testing:** Software and hardware need to work together properly. Testing might involve:
    *   **Compatibility:** Making sure the software runs on different hardware configurations.
    *   **Performance:** Checking how well the software performs on different CPUs, amounts of RAM, etc.
    *   **Hardware Specific Issues:** Some applications need to interact with hardware (e.g. sensors), so testing that these interactions are correct is also important. For example, a medical scanner relies on its hardware sensors to work properly with the software.
    *   **Driver testing:** Ensuring correct operation of hardware that is managed via device drivers.

We need to ensure that the software works correctly on different machines to provide consistent user experiences and that the software works correctly with any specific hardware it needs to interface with.

### 2.3 Data

**What it is:** Data is the raw information that a software application processes. It can be stored in:
    *   **Databases:** Structured collections of data.
    *   **Files:** Documents, images, or other stored data.
    *   **Variables:** Data stored within the application itself.

**In relation to testing:** Data is crucial for testing. We test how the software handles:
    *   **Different Data Types:** Integers, text, dates, etc.
    *   **Data Formats:** CSV, JSON, XML, etc.
    *   **Data Volume:** Large or small datasets.
    *   **Valid Data:** Making sure the software correctly handles expected input.
    *   **Invalid Data:** Checking how the software deals with bad input data to ensure it doesn't crash or produce incorrect results. 
    *   **Edge Cases:** Values near the limits of what is accepted, to see if things break when they shouldn't, or don't break when they should. 
    *   **Data integrity:** Checking data storage, transfer and retrieval to make sure it's not changed or corrupted.

Proper testing of data handling will ensure that the application works correctly in many different scenarios.

### 2.4 Interfaces

**What it is:** Interfaces are the points of interaction between parts of a system. These can be:
    *   **User Interfaces (UI):** What the user sees and interacts with (e.g., buttons, menus, text boxes).
    *   **Application Programming Interfaces (APIs):** How different software components or systems communicate (e.g., a web server talking to a database).

**In relation to testing:** Interface testing involves verifying:
    *   **Communication:** Checking data exchange between components or systems.
    *   **Data Accuracy:** Ensuring the right data is being sent and received.
    *   **Data Consistency:** Making sure that data is not lost or corrupted during transfer.
    *   **Data formats:** Ensuring that the data being exchanged is in the expected format and that all data conforms to expectations.
    *   **API calls:** Making sure API calls return the correct results and error codes.

We need to make sure that different parts of the system work together correctly and without unexpected behaviour in the communication channels.

### 2.5 Resulting Service (Final Product)

**What it is:** This is the final software application, system, or service that end users will use. It's the culmination of all the development and testing efforts.

**In relation to testing:** We need to test:
    *   **Functionality:** Does it do everything it's supposed to do?
    *   **Performance:** Does it work smoothly and efficiently?
    *   **Usability:** Is it easy and intuitive for users?
    *   **Reliability:** Is it stable and does it work without fail?
    *   **User Satisfaction:** Does the application meet expectations of the user?

The final product should be a polished, stable, and reliable service that meets all the requirements of the project.

## 3. Testing Methodologies

**What it is:** Testing methodologies are different approaches or strategies used to test an application and ensure it meets requirements. These help ensure the software behaves and looks as expected and that unexpected behaviour is handled safely and without side-effects. It covers front-end (what the user sees and interacts with) and back-end (the hidden data management and processes), along with the complete system from individual units to complete system testing.

### 3.1 Concept Testing

**What it is:** This is about testing the *idea* for a software product. It involves seeing if there's demand for it and if it is something people would find useful, before a single line of code has been written.

**How it is used:** We test by:
    *   **Gathering User Feedback:** Getting feedback from potential users.
    *   **Surveys & Focus Groups:** Asking questions about the idea and gauging interest.
    *   **Simulations:** Creating mockups to give people a sense of how the product would work.
    *   **Market Research:** Seeing if there's a need for the product, or if there are existing similar products.

Concept testing helps us avoid spending time and resources on ideas that won't work, or that will not be used. It allows us to determine the initial, core features that the software must have to be successful.

### 3.2 Unit Testing

**What it is:** Unit testing involves testing individual pieces of code (like functions or classes) *in isolation*.

**How it is used:** Developers write unit tests to:
    *   **Verify Logic:** Check that each unit of code works correctly.
    *   **Catch Bugs Early:** Find problems at the lowest level of the application.
    *   **Improve Code Quality:** Ensure code is robust and easy to maintain.

It's a fundamental part of development, that ensures that each part of the code is working before it is incorporated into the larger application. The purpose is to catch bugs as early as possible.

### 3.3 Boundary Testing

**What it is:** Boundary testing focuses on testing the edge cases for data input. It involves using the maximum and minimum values to see how the system behaves with these inputs.

**How it is used:**
    *   **Valid Boundary values:** Testing the maximum and minimum value that is valid.
    *   **Invalid boundary values:** Testing values that are just outside of the range of valid values.

For example, if the software accepts values from 1 to 100. We'd test 0, 1, 100, and 101 to see how it behaves. This helps to catch errors arising from logic that doesn't correctly handle edge cases.

### 3.4 Integration Testing

**What it is:** Integration testing is when we start to put the different modules of code together and test them to ensure they work with each other correctly.

**How it is used:** After unit testing, we:
    *   **Combine Modules:** Gradually integrate the different parts of the software.
    *   **Verify Communication:** Ensure data flows correctly between the modules.
    *   **Identify Integration Issues:** Catch bugs that arise when different parts work together.

This stage helps to ensure that modules that work fine individually, also work together as a single functional entity.

### 3.5 Performance Testing

**What it is:** Performance testing focuses on speed, stability and scaling of the application under various conditions.

**How it is used:**
    *   **Identify Bottlenecks:** Finding slow or inefficient parts of the system.
    *   **Measure Response Times:** Checking how quickly the system reacts to user inputs.
    *   **Check Scalability:** Seeing how well the system handles increased loads of users or data.
    *   **Measure resource usage:** Checking memory usage and CPU load.

This type of testing helps ensure that the software performs well under normal or high load conditions.

### 3.6 System Testing

**What it is:** System testing tests the complete software application as a whole, making sure that all modules are properly integrated and the software performs in accordance with expectations.

**How it is used:**
    *   **Verify Functionality:** Check that all functional requirements of the system are met from the end user perspective.
    *   **Non-functional testing:** Testing that requirements such as performance, availability, security and usability are also met.
    *   **End-to-end user workflows:** Testing typical user tasks or behaviours.

System testing is typically done by testers, rather than developers.

### 3.7 Acceptance and Usability Testing

**What it is:** Acceptance testing is used to confirm that the software meets the acceptance criteria defined by the client or the stakeholders. Usability testing focuses on how easy and intuitive the software is for the end user.

**How it is used:**
    *   **Acceptance Testing:**
        *   Done by Users or Stakeholders: They test the software to see if it meets their needs.
        *   Checks for Compliance: Ensures all requirements are met.
    *   **Usability Testing:**
        *   Users Interact with Software: Testers observe users working with the software.
        *   Feedback on Ease of Use: Gather information on effectiveness and satisfaction.

This ensures the software meets user needs and is easy to use.

### 3.8 Regression Testing

**What it is:** Regression testing is when a test that was done previously, is repeated again, after changes or updates to the code have been made. The purpose is to make sure that the existing software features haven't been broken by the new code.

**How it is used:**
    *   **Retest Key Features:** Making sure old features still work fine.
    *   **Catch Unintended Consequences:** Find new bugs introduced by code changes.
    *   **Automate Tests:** Often done automatically for efficiency.

This is extremely important as unexpected bugs could appear after code updates.

### 3.9 Load/Stress Testing

**What it is:**
    *   **Load Testing:** Simulates a normal anticipated level of usage to see how the system performs.
    *   **Stress Testing:** Pushes the system to its absolute limit and beyond, to see when it starts to fail or break.

**How it is used:**
    *   **Load tests:** check performance under normal levels of users and data.
    *   **Stress tests:** determines the breaking point of the system and allows for effective scaling of the application.

This is used to ensure that the system is stable and can cope with a high level of use.

## 4. Conclusion

Software testing is critical to the software development process. By having a clear understanding of the different testing methodologies and the core elements of the software being tested, teams can deliver software that is bug free, reliable and meets all user requirements. The overall goals of testing are to: identify and fix bugs, make sure that the software meets requirements, provide a good user experience, and ensure that the software is stable and resilient. This report provides a solid overview of the key testing concepts and helps give a good grounding in these key ideas.

I hope this expanded report with explanations is more helpful! Let me know if you have any other questions.
