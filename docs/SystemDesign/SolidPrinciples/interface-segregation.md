---
title: Interface Segregation Principle
tags:
  - Design Principles
  - System Design
  - Basics
  - SOLID
---

## Introduction

The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use. It promotes the idea of segregating interfaces into smaller, more focused ones to avoid unnecessary dependencies and provide a clear contract for specific functionality.

## Example

In the context of a payment system, we can demonstrate the ISP as follows:

#### Interfaces

- `OnlinePayment`: Declares the `processOnlinePayment()` method, representing the behavior of processing payments online.

```java
public interface OnlinePayment {
    void processOnlinePayment();
}
```

- `OfflinePayment`: Declares the `processOfflinePayment()` method, representing the behavior of processing payments offline.

```java
public interface OfflinePayment {
    void processOfflinePayment();
}
```

#### Implementing Classes

- `CreditCardPayment`: Implements the `OnlinePayment` interface, as credit card payments are typically processed online. It provides the implementation for the `processOnlinePayment()` method.

```java
public class CreditCardPayment implements OnlinePayment {
    public void processOnlinePayment() {
        // Process credit card payment online
    }
}
```

- `CashPayment`: Implements the `OfflinePayment` interface, as cash payments are processed offline. It provides the implementation for the `processOfflinePayment()` method.

```java
public class CashPayment implements OfflinePayment {
    public void processOfflinePayment() {
        // Process cash payment offline
    }
}
```

- `BankTransferPayment`: Implements both the `OnlinePayment` and `OfflinePayment` interfaces, as bank transfer payments can be processed both online and offline. It provides the implementations for both the `processOnlinePayment()` and `processOfflinePayment()` methods.

```java
public class BankTransferPayment implements OnlinePayment, OfflinePayment {
    public void processOnlinePayment() {
        // Process bank transfer payment online
    }

    public void processOfflinePayment() {
        // Process bank transfer payment offline
    }
}
```

By segregating the interfaces based on their functionality, we ensure that clients only need to implement the interfaces that are relevant to them. This promotes a more focused and cohesive design, as clients are not forced to depend on methods they don't need.

The ISP allows for better maintainability, extensibility, and flexibility in the payment system. Clients can depend on the specific interfaces that they require, avoiding unnecessary dependencies and providing a clear contract for their specific needs. This leads to a more robust and scalable system that can accommodate various types of payments.
